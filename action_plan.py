import pandas as pd

# Load your results
df = pd.read_csv("MY_PROJECT_RESULTS.csv")

# Create a "Deployment Schedule"
# We'll take the top 20 and add a 'Priority Level'
top_20 = df.sort_values(by='sync_score', ascending=False).head(20).copy()

def assign_priority(score):
    if score > top_20['sync_score'].median(): return "IMMEDIATE (Week 1)"
    return "HIGH (Week 2)"

top_20['Deployment_Window'] = top_20['sync_score'].apply(assign_priority)
top_20['Vans_Required'] = 2 # Recommendation: 2 vans per high-risk district

# Save it as an official-looking document
top_20[['state', 'district', 'sync_score', 'Deployment_Window', 'Vans_Required']].to_csv("VAN_DEPLOYMENT_SCHEDULE.csv", index=False)
print("✅ Created: VAN_DEPLOYMENT_SCHEDULE.csv")