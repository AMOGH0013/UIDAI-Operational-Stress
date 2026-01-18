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
- Streamlit-based decision-support dashboard mock-up

## Project Structure
- `data/` : Raw UIDAI datasets (not committed to GitHub)
- `notebooks/` : Step-by-step analysis notebooks
- `dashboard/` : Streamlit dashboard mock-up
- `outputs/` : Clean analytical outputs
- `assets/` : Maps and dashboard screenshots

## How to Run Dashboard
```bash
pip install -r requirements.txt
streamlit run dashboard/dashboard_app.py
