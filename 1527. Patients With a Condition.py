import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = (
        patients["conditions"].str.match(r"^DIAB1") |
        patients["conditions"].str.contains(r" DIAB1")
    )
    patient_df = patients[mask]
    return patient_df[["patient_id", "patient_name", "conditions"]]
