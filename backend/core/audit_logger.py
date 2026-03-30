from datetime import datetime

audit_logs = []

def log_query(epsilon, remaining_budget):
    audit_logs.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "epsilon": epsilon,
        "remaining_budget": remaining_budget
    })

def get_logs():
    return audit_logs

def reset_logs():
    audit_logs.clear()