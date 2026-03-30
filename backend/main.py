from fastapi import FastAPI, UploadFile, HTTPException
import pandas as pd
import logging
from backend.core.federated import simulate_federated_learning
from backend.core.audit_logger import log_query, get_logs, reset_logs
# IMPORTANT: correct package imports
from backend.core.differential_privacy import (
    private_count,
    private_mean,
    private_sum,
)
from backend.core.privacy_budget import PrivacyBudget


# -------------------------
# Logging Configuration
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------------
# App Initialization
# -------------------------
app = FastAPI(title="Privacy Analytics Engine")

# Global Privacy Budget
budget = PrivacyBudget(total_budget=5.0)


# -------------------------
# Routes
# -------------------------
@app.post("/federated/")
async def federated(file: UploadFile):
    df = pd.read_csv(file.file)
    
    col = df.select_dtypes(include=["int64", "float64"]).columns[0]
    data = df[col].dropna().values

    result = simulate_federated_learning(data)

    return result


@app.get("/")
def root():
    return {"message": "Privacy Analytics Engine is running"}

@app.get("/logs/")
def get_audit_logs():
    return get_logs()


@app.post("/reset-budget/")
def reset_budget():
    global budget
    budget = PrivacyBudget(total_budget=5.0)
    reset_logs()
    return {"message": "Budget reset"}


@app.post("/upload/")
async def upload(file: UploadFile, epsilon: float = 1.0):

    # Consume privacy budget
    try:
        budget.consume(epsilon)
	log_query(epsilon, budget.remaining())
        logging.info(f"Epsilon used: {epsilon}")
        logging.info(f"Remaining budget: {budget.remaining()}")
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))

    # Read dataset
    df = pd.read_csv(file.file)
    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

    # Private Count
    private_count_value = private_count(df, epsilon)
    logging.info("Private count computed")

    results = {
        "private_count": private_count_value,
        "remaining_budget": budget.remaining()
    }

    # Compute private stats per numeric column
    for col in numeric_columns:
        series = df[col].dropna()
        results[col] = {
            "mean": private_mean(series, epsilon),
            "sum": private_sum(series, epsilon),
        }

    return results