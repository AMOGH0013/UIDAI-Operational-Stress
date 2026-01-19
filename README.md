# UIDAI Operational Stress & Predictive Analytics

This project was developed for the UIDAI Hackathon to identify patterns,
anomalies, and predictive indicators in Aadhaar enrolment, demographic,
and biometric update data.

## Problem Statement
Unlock societal and operational trends in Aadhaar enrolment and updates
to support informed decision-making and system improvements.

## Key Contributions
- Temporal anomaly detection in UIDAI activity
- District-level geographic stress analysis (India-wide map)
- Age-group behavioural analysis with policy-driven explanations
- 30-day forward predictive indicator (early-warning system)
- Operational escalation risk index

## Data Note

Raw UIDAI CSV data is intentionally excluded from this repository.

Reason:
- Large size
- Reproducible via API
- Follows best practices for open repositories

All notebooks expect data to be placed locally under the `/data` directory.
## How to Run

1. Clone the repository
2. Place UIDAI CSV files into:
   - data/enrolment/
   - data/demographic/
   - data/biometric/
3. Start with:
   - `Concat.ipynb`
4. Then run notebooks in this order:
   - TimeBasedUnderstanding
   - Age-Group Behaviour
   - Anomaly Detection
   - GeographicStress
   - ADVANCED LAYER

## Project Structure
- `data/` : Raw UIDAI datasets (not committed to GitHub)
- `notebooks/` : Step-by-step analysis notebooks
- `dashboard/` : Streamlit dashboard mock-up
- `outputs/` : Clean analytical outputs
- `assets/` : Maps and dashboard screenshots

