import pandas as pd
import glob
import os

# --- PART 1: Find your data ---
# This part looks into the folders you made in Step 2
print("Phase 1: Finding your data folders...")
enrol_files = glob.glob("data/enrolment/*.csv")
bio_files = glob.glob("data/biometric/*.csv")

# --- PART 2: Read the files ---
# We are combining all those small CSV files into one big list
print("Phase 2: Reading all CSV files (this may take a minute)...")
df_enrol = pd.concat([pd.read_csv(f) for f in enrol_files])
df_bio = pd.concat([pd.read_csv(f) for f in bio_files])

# --- PART 3: Calculate the "Sync-Score" ---
# We group the data by District and compare Enrolments vs Updates
print("Phase 3: Calculating the Sync-Score (The 'Service Desert' Finder)...")

# Sum up the numbers for each district
enrol_grouped = df_enrol.groupby(['state', 'district'])['age_5_17'].sum().reset_index()
bio_grouped = df_bio.groupby(['state', 'district'])['bio_age_5_17'].sum().reset_index()

# Merge them together
final_data = pd.merge(enrol_grouped, bio_grouped, on=['state', 'district'])

# THE FORMULA: High Score = High Risk
# (Number of kids who need it / Number of kids who actually updated)
final_data['sync_score'] = final_data['age_5_17'] / (final_data['bio_age_5_17'] + 1)

# --- PART 4: Save the Result ---
# This creates a final Excel-ready file for you
final_data.sort_values(by='sync_score', ascending=False).to_csv("MY_PROJECT_RESULTS.csv", index=False)

print("\nSUCCESS! You did it.")
print("Look in your 'AadhaarSync' folder for a new file called: MY_PROJECT_RESULTS.csv")