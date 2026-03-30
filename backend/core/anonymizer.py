import re
import pandas as pd

def mask_email(text):
    return re.sub(r'\S+@\S+', '[EMAIL]', str(text))

def mask_phone(text):
    return re.sub(r'\b\d{10}\b', '[PHONE]', str(text))

def mask_ip(text):
    return re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[IP]', str(text))

def anonymize_dataframe(df):
    for col in df.columns:
        df[col] = df[col].apply(mask_email)
        df[col] = df[col].apply(mask_phone)
        df[col] = df[col].apply(mask_ip)
    return df