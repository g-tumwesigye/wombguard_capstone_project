# WombGuard

## Description
WombGuard is a web platform designed to support healthcare providers and patients in assessing pregnancy risk levels. It combines **predictive analytics** and a **Conversational ChatBot** to provide personalized guidance.  

The predictive component uses a trained Random Forest machine learning model to analyze patient data, including age, blood pressure, blood sugar, body temperature, BMI, and heart rate—to predict pregnancy risk as either low or high. Predictions include probability scores and confidence levels, giving users clear and actionable insights.  

The Conversational ChatBot, which is planned for future development and integration, will allow users to interactively ask questions, receive explanations for predictions, and obtain personalized guidance. This combination of predictive modeling and conversational AI will make the platform both informative and user-friendly, enabling more accessible healthcare support.  

## GitHub Repository
[https://github.com/wombguard_capstone_project](https://github.com/g-tumwesigye/wombguard_capstone_project)

## Project Structure
```

wombguard_capstone_project/
│── Data/
│   ├── wombguard_dataset.csv          
│   ├── local_pregnancy_dataset.csv
├─ README.md
├─ requirements.txt
├─ shap_analysis_insights.json
├─ main.py
├─ wombguard_pregnancy_model.pkl
└─ wombguard_predictive_models.ipynb

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

The WombGuard web platform will be deployed on [Render](https://render.com) for public access. Deployment includes:

1. Exposing FastAPI endpoints for the predictive model.
2. Using Swagger UI to demonstrate predictions.
3. Integrating the Conversational ChatBot for interactive guidance and explanations in the near future.
4. Expanding the platform to a complete web interface for patient input and prediction results display.

## Video Demo

[Click to Watch the Demo Video](https://www.youtube.com/watch?v=eSwuXgh3sZM)

The demo highlights:

* Running the FastAPI server
* Accessing the Swagger UI
* Making predictions with sample patient data
* Displaying predicted risk and confidence

## Notes

* This submission focuses on the initial software demo.
* The user interface is currently via **Swagger UI**, not a full web app.

```
