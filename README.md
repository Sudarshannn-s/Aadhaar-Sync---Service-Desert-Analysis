# AadhaarSync: Service Desert Analysis
**A Data-Driven Strategy for Optimizing Mobile Aadhaar Van Deployment.**

---

## Project Overview
**AadhaarSync** is a decision-support tool designed to identify **"Service Deserts"**—regions where there is a significant gap between new Aadhaar enrolments and mandatory biometric updates. 

In the 5–17 age demographic, citizens must update their biometrics to keep their IDs active. When enrolments are high but updates are low, it indicates a lack of accessible infrastructure. This project uses Python to analyze UIDAI datasets and calculate a **Sync-Score**, allowing governments to deploy **Mobile Aadhaar Vans** with mathematical precision.

## The Problem: The "Maintenance Gap"
* **Mandatory Requirements:** Children must update biometrics at ages 5 and 15 to ensure service continuity.
* **The Risk:** Without these updates, citizens face exclusion from school admissions, scholarships, and welfare benefits.
* **The Challenge:** Stationary Aadhaar centers are often concentrated in urban hubs, leaving rural or rapidly growing districts underserved.

## The Algorithm: The "Sync-Score"
We developed the **Sync-Score** to quantify district-level criticality. This metric identifies where the system is expanding (new enrolments) but the maintenance infrastructure (updates) is failing.

$$Sync\text{-}Score = \frac{Total\ Enrolments\ (Age\ 5\text{-}17)}{Biometric\ Updates\ (Age\ 5\text{-}17) + 1}$$

> **How to interpret the results:**
> * **High Sync-Score:** Represents a "Service Desert." These areas are the highest priority for Mobile Van intervention.
> * **Low Sync-Score:** Indicates healthy maintenance. Existing centers are meeting the population's needs.

---

## Tech Stack
* **Language:** Python 3.13
* **Data Science:** Pandas (Data Harmonization), NumPy
* **Visualization:** Seaborn, Matplotlib
* **Automation:** Glob (Recursive file searching and multi-dataset merging)

## Methodology
1.  **Data Ingestion:** Automatically crawls through nested data folders to find and merge Enrolment, Biometric, and Demographic CSV files.
2.  **Harmonization:** Standardizes district-level data to ensure accurate cross-state comparisons.
3.  **Risk Modeling:** Calculates the Sync-Score and ranks districts from "Critical" to "Stable."
4.  **Actionable Output:** Generates a **Van Deployment Schedule** that suggests the number of units required per district.


---

## Repository Structure
* `sync_analysis.py`: The core engine that processes raw CSV data.
* `visualize.py`: Script to generate analytical bar charts.
* `action_plan.py`: Logic to convert scores into a deployment schedule.
* `MY_PROJECT_RESULTS.csv`: The final processed priority list.
* `my_sync_chart.png`: Visual representation of the Top 10 Service Deserts.

---

## Impact
By implementing **AadhaarSync**, government agencies can:
* **Reduce Exclusion:** Ensure zero "drop-outs" from the Aadhaar ecosystem due to missed updates.
* **Optimize Resources:** Deploy expensive mobile assets (vans) based on real-time data demand rather than guesswork.
* **Scalable Solution:** The modular code is ready to process new monthly API data as soon as it is released.

**Developed by:** [Sudarshann-s]  
**Category:** Governance & Public Policy Innovation
