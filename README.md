# 🏠 House Price Prediction System

An AI-powered House Price Prediction Web Application built using **Python, Django, Machine Learning, Bootstrap, and Scikit-Learn**.

The system predicts house prices based on various housing features such as income, house age, rooms, bedrooms, population, occupancy, latitude, and longitude.

---

## 🚀 Features

✅ Machine Learning-based House Price Prediction

✅ Modern Responsive UI with Bootstrap 5

✅ Prediction History Management

✅ Professional About Page

✅ User-Friendly Interface

✅ Real-Time Prediction Results

✅ Prediction Records Stored in Database

✅ Fully Responsive Design

---

## 📸 Screenshots

### Home Page

- Modern Hero Section
- AI Powered Prediction System
- Professional Bootstrap UI

### Prediction Page

- User Input Form
- Instant Price Prediction
- Attractive Result Display

### History Page

- Stores all previous predictions
- Displays input parameters and predicted price
- Professional table design

### About Page

- Project Overview
- Technology Information
- Features Description

---

## 🛠 Technologies Used

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons

### Backend

- Python
- Django

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Database

- SQLite3

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── mainapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── parent.html
│   │   ├── index.html
│   │   ├── prediction.html
│   │   ├── history.html
│   │   └── about.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── house_price_model.pkl
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

## 📊 Input Features

The model uses the following features for prediction:

| Feature | Description |
|----------|------------|
| MedInc | Median Income |
| HouseAge | Average House Age |
| AveRooms | Average Rooms |
| AveBedrms | Average Bedrooms |
| Population | Population |
| AveOccup | Average Occupancy |
| Latitude | Latitude |
| Longitude | Longitude |

---

## 🤖 Machine Learning Model

The prediction model is trained using housing data and exported using Joblib.

```python
joblib.dump(model, "house_price_model.pkl")
```

The trained model is loaded inside Django and used for real-time predictions.

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/House-Price-Prediction.git
```

### Navigate to Project

```bash
cd House-Price-Prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

## 🌐 Open In Browser

```text
http://127.0.0.1:8000/
```

---

## 📈 Future Improvements

- User Authentication
- Prediction Analytics Dashboard
- Data Visualization Charts
- Model Comparison
- CSV Export
- Cloud Deployment
- Advanced AI Models

---

## 👨‍💻 Developer

**Saif Ahmad**

Data Science & Machine Learning Enthusiast

GitHub: https://github.com/Saif-Ahmad11

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

It helps others discover the project and motivates future development.

---

## 📜 License

This project is licensed under the MIT License.
