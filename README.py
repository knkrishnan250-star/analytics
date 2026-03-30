# 🔐 Privacy-Preserving Analytics Engine

A web-based analytics system that enables secure data analysis using **Differential Privacy** techniques. This project ensures that statistical insights can be extracted from datasets **without exposing sensitive individual information**.

---

## 🚀 Features

* 🔢 **Private Statistics**

  * Private Count
  * Private Mean
  * Private Sum
  * Histogram (with noise)

* 🛡 **Differential Privacy**

  * Laplace Mechanism
  * Gaussian Mechanism
  * Adjustable epsilon (privacy level)

* 📉 **Privacy Budget Tracking**

  * Dynamic epsilon consumption
  * Prevents excessive data querying

* 📜 **Audit Logging**

  * Tracks query history
  * Logs epsilon usage and timestamps

* 🔄 **Budget Reset System**

  * Reset privacy budget safely

* 🤖 **Federated Learning Simulation**

  * Demonstrates distributed learning without sharing raw data

* 🎨 **Interactive Dashboard**

  * Built with Streamlit
  * Sidebar controls for privacy settings

---

## 🏗 Architecture

```
privacy_analytics_engine/
│
├── backend/
│   ├── main.py
│   ├── core/
│   │   ├── differential_privacy.py
│   │   ├── privacy_budget.py
│   │   ├── audit_logger.py
│   │   └── federated.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib

---

## 🔬 How It Works

1. User uploads a dataset (CSV)
2. Backend processes numeric columns
3. Applies **Differential Privacy noise**
4. Returns safe statistical results
5. Tracks privacy budget and logs queries

---

## 🧠 Differential Privacy

This system uses:

* **Laplace Mechanism** → for basic privacy protection
* **Gaussian Mechanism** → for advanced privacy scenarios

Privacy is controlled using:

```
epsilon ↓  → more privacy, less accuracy  
epsilon ↑  → less privacy, more accuracy  
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/privacy-analytics-engine.git
cd privacy-analytics-engine
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run Backend

```
python -m uvicorn backend.main:app
```

---

### 4️⃣ Run Frontend

```
python -m streamlit run frontend/app.py
```

---

### 5️⃣ Open in Browser

```
http://localhost:8501
```

---

## 📊 Example Output

* Private Count: 768.25
* Private Mean (Glucose): 122.15
* Remaining Budget: 1.13

---

## 🎯 Use Cases

* 🏥 Healthcare data analysis
* 📊 Government statistics
* 🔐 Privacy-focused analytics systems
* 📚 Research and academic projects

---

## 🏆 Key Highlights

* Implements **Differential Privacy from scratch**
* Includes **privacy budget enforcement**
* Demonstrates **secure analytics pipeline**
* Combines **data science + privacy engineering**

---

## 📌 Future Improvements

* Authentication system (multi-user)
* Synthetic data generation
* Advanced ML with privacy guarantees
* Cloud deployment (SaaS)

---

## 👨‍💻 Author

Your Name

---

## ⭐ If you like this project, give it a star!
