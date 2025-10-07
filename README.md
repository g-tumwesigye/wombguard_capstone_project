# WombGuard

## Description
WombGuard is a web platform designed to support healthcare providers and patients in assessing pregnancy risk levels. It combines **predictive analytics** with a planned **Conversational ChatBot** to provide a comprehensive digital healthcare tool.  

The predictive component uses a trained Random Forest machine learning model to analyze patient data—including age, blood pressure, blood sugar, body temperature, BMI, and heart rate—to predict pregnancy risk as either low or high. Predictions include probability scores and confidence levels, giving users clear and actionable insights.  

The Conversational ChatBot, which is planned for future development and integration, will allow users to interactively ask questions, receive explanations for predictions, and obtain personalized guidance. This combination of predictive modeling and conversational AI will make the platform both informative and user-friendly, enabling more accessible healthcare support.  

## GitHub Repository
[https://github.com/YourUsername/wombguard_capstone_project](https://github.com/YourUsername/wombguard_capstone_project)

## Environment Setup and Project Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YourUsername/wombguard_capstone_project.git
   cd wombguard_capstone_project
````

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server locally**

   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API documentation (Swagger UI)**
   Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser to interact with the predictive API.

## Deployment Plan

The WombGuard web platform will be deployed on [Render](https://render.com) for public access. Deployment includes:

1. Exposing FastAPI endpoints for the predictive model.
2. Using Swagger UI to demonstrate predictions.
3. Integrating the Conversational ChatBot for interactive guidance and explanations in the near future.
4. Expanding the platform to a complete web interface for patient input and prediction results display.

