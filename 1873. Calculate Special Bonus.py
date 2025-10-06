import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees_modified = employees.assign(
        is_odd = lambda x: x["employee_id"] % 2 != 0, 
        not_m = lambda x: ~x["name"].str.startswith("M"), 
        bonus = lambda x: x["salary"].where(x["is_odd"] & x["not_m"], 0)
    )
    return employees_modified[["employee_id", "bonus"]].sort_values(by="employee_id")
