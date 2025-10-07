
```bash
# WombGuard Pregnancy Predictive Platform

## Description
WombGuard is a web-based predictive platform designed to assess pregnancy risk using patient clinical data. The platform uses a trained Random Forest machine learning model to provide risk predictions with confidence scores. The system also includes SHAP-based explainability to interpret model outputs.

This submission demonstrates the **initial software product**, including the predictive API and deployment-ready model.

## GitHub Repository
[Link to your GitHub repo](https://github.com/yourusername/wombguard_capstone_project)

## Project Structure
```

wombguard_capstone_project/
│
├─ README.md
├─ requirements.txt
├─ wombguard_pregnancy_model.pkl
├─ shap_analysis_insights.json
├─ main.py
├─ video_demo/
│    └─ wombguard_demo.mp4
└─ venv/  # Optional, not necessary to include in repo

````

## Environment Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/wombguard_capstone_project.git
cd wombguard_capstone_project
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Platform

Start the FastAPI app:

```bash
python -m uvicorn main:app --reload
```

Open your browser and go to:

```
http://127.0.0.1:8000
```

You can test the API endpoints via the **Swagger UI** available at:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

* `GET /` – Returns a success message if the API is running.
* `POST /predict` – Accepts patient data in JSON format and returns predicted pregnancy risk with probability and confidence score.

### Example JSON for `/predict`:

```json
{
  "features": {
    "Age": 28,
    "Systolic_BP": 118,
    "Diastolic": 78,
    "BS": 4.5,
    "Body_Temp": 36.8,
    "BMI": 23.5,
    "Heart_Rate": 80
  }
}
```

## Deployment Plan

* The model is saved with preprocessing and can be deployed as a web API using FastAPI.
* Swagger UI provides a simple interface for testing endpoints.
* Future plans: integrate with a full web interface or mobile app for clinical use.

## Video Demo

A demonstration of the platform is included in:

```
video_demo/wombguard_demo.mp4
```

The demo highlights:

* Running the FastAPI server
* Accessing the Swagger UI
* Making predictions with sample patient data
* Displaying predicted risk and confidence

## Notes

* This submission focuses on the initial software demo.
* The user interface is currently via **Swagger UI**, not a full web app.

```

I can also draft a **short script for your 5-minute video demo** so you can record it immediately. Do you want me to do that next?
```
