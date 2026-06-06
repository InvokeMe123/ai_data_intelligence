import pandas as pd


def convert_datetime(series):
    return pd.to_datetime(series, errors="coerce")


def convert_numeric(series):
    return pd.to_numeric(series, errors="coerce")


def strip_whitespace(series):
    return series.astype(str).str.strip()


def lowercase_text(series):
    return series.astype(str).str.lower()


def standardize_duration(series):
    return series.astype(str).str.strip().str.lower()


COLUMN_RULES = {
    "show_id": [strip_whitespace],
    "category": [strip_whitespace, lowercase_text],
    "title": [strip_whitespace],
    "director": [strip_whitespace],
    "cast": [strip_whitespace],
    "country": [strip_whitespace, lowercase_text],
    "release_date": [convert_datetime],
    "rating": [strip_whitespace, lowercase_text],
    "duration": [standardize_duration],
    "type": [strip_whitespace, lowercase_text],
    "description": [strip_whitespace]
}