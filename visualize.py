import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the results with YOUR specific filename
try:
    # I changed the filename here to match your result
    df = pd.read_csv("MY_PROJECT_RESULTS.csv") 
    print("✅ File found! Generating your chart...")
except FileNotFoundError:
    print("❌ Error: I couldn't find 'MY_PROJECT_RESULTS.csv'.")
    print("Make sure the filename in your folder is exactly the same!")
    exit()

# 2. Get the Top 10 "Service Deserts" (Highest Sync-Score)
# Sorting again just to be safe
top_10 = df.sort_values(by='sync_score', ascending=False).head(10)

# 3. Set the visual style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))

# 4. Create the Bar Chart
ax = sns.barplot(
    data=top_10, 
    x='sync_score', 
    y='district', 
    palette="Reds_r",
    hue='district',
    legend=False
)

# 5. Titles and Labels
plt.title('Top 10 Districts: Aadhaar Service Gap Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Sync-Score (Priority Level)', fontsize=12)
plt.ylabel('District Name', fontsize=12)

# Add the score numbers to the bars
for i in ax.containers:
    ax.bar_label(i, padding=3, fmt='%.2f')

# 6. Save and show
plt.tight_layout()
plt.savefig("my_sync_chart.png", dpi=300)
print("✅ Chart saved as 'my_sync_chart.png'")
plt.show()