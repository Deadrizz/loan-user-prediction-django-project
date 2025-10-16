A Django web application that predicts whether a user’s **loan application will be approved** based on their personal and financial data.  
The project combines a **Machine Learning model (RandomForestClassifier)** with a **Django REST API** and a **simple front-end interface** for user interaction.

---

## 🚀 Features

✅ **User Authentication**
- Registration and login via Django forms  
- Session-based authentication for API requests

✅ **Loan Prediction**
- Trained ML model (`RandomForestClassifier`) saved as `model.pkl`  
- Integrated into Django — predictions are made on the fly  
- Returns probability and prediction result (approved / not approved)

✅ **REST API**
- Built with Django REST Framework (DRF)
- Endpoints:
  - `GET /api/loans/` — List all user loan applications
  - `POST /api/loans/` — Submit a new loan request and get a prediction
- Pagination, filtering, and ordering included

✅ **Front-End Integration**
- HTML + JavaScript (`fetch`) for form submission
- Real-time prediction displayed without page reload
- User can view all their previous loan requests

✅ **API Documentation**
- Swagger & Redoc via **drf-spectacular**
  - `/api/docs/` — Swagger UI  
  - `/api/redoc/` — Redoc view  
  - `/api/schema/` — OpenAPI JSON schema

---

## 🧩 Tech Stack

| Layer | Tools |
|-------|-------|
| **Language** | Python 3.12 |
| **Framework** | Django, Django REST Framework |
| **Machine Learning** | scikit-learn, pandas, numpy, joblib |
| **Database** | SQLite (can be switched to PostgreSQL) |
| **Front-End** | HTML, CSS (Bootstrap), JavaScript (Fetch API) |
| **Docs** | drf-spectacular (Swagger, Redoc) |
| **Version Control** | Git + GitHub |
| **IDE** | PyCharm |

---

## 🧠 Machine Learning Model

- Model type: `RandomForestClassifier`
- Data source: `loan_data.csv`
- Data preprocessing pipeline includes:
  - `SimpleImputer` for missing values  
  - `StandardScaler` for numeric features  
  - `OneHotEncoder` for categorical features  
- The model is trained and saved as `model.pkl` via `joblib`

Example model pipeline:

```python
pipe = Pipeline(steps=[
    ("preprocessor", preprocess),
    ("classifier", RandomForestClassifier(random_state=42))
])
⚙️ Installation & Setup
1. Clone the repository
bash
Копировать код
git clone https://github.com/Deadrizz/loan-user-prediction-django-project.git
cd loan-user-prediction-django-project
2. Create and activate a virtual environment
bash
Копировать код
python -m venv .venv
source .venv/bin/activate     # (Linux/macOS)
.venv\Scripts\activate        # (Windows)
3. Install dependencies
bash
Копировать код
pip install -r requirements.txt
4. Apply migrations and create a superuser
bash
Копировать код
python manage.py migrate
python manage.py createsuperuser
5. Run the development server
bash
Копировать код
python manage.py runserver
Now open the app at:
👉 http://127.0.0.1:8000/

🧑‍💻 Usage
Register or log in.

Go to “Apply for Loan” page (/loan/apply/).

Fill in the loan application form.

Click “Submit” — the backend will:

Validate the data

Run the ML model prediction

Display result with probability (approved / not approved)

You can check your previous loan applications at /loan/my_list/.

📊 Example Prediction (API Request)
Request:
bash
Копировать код
POST /api/loans/
Content-Type: application/json

{
  "gender": "Male",
  "married": "Yes",
  "dependents": "1",
  "education": "Graduate",
  "self_employed": "No",
  "applicant_income": 4000,
  "coapplicant_income": 1500,
  "loan_amount": 120,
  "loan_amount_term": 360,
  "credit_history": 1.0,
  "property_area": "Urban"
}
Response:
json
Копировать код
{
  "predicted_approved": true,
  "predicted_probability": 0.83
}
🧩 Project Structure
bash
Копировать код
config/
│
├── loan/
│   ├── models.py              # Django models (LoanApplication)
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API logic + ML integration
│   ├── templates/loan/        # HTML templates (apply.html, my_list.html)
│   ├── urls.py                # API endpoints
│   └── page_urls.py           # Front-end pages routing
│
├── config/settings.py         # Django settings
├── config/urls.py             # Root URLs (API + Docs + Admin)
└── model.pkl                  # Trained ML model
📈 Possible Improvements
🔹 Improve UI/UX (Bootstrap 5 + Charts)

🔹 Deploy on Render / Railway with Docker

🔹 Add JWT authentication for external API users

🔹 Admin dashboard for analytics (approval rates, income stats)

🔹 Export loan history to CSV / PDF

🧾 Author
👤 Stanislav Simutin (Deadrizz)
🎯 Python Backend Developer
📂 GitHub: @Deadrizz

📜 License
This project is open-source and available under the MIT License.

