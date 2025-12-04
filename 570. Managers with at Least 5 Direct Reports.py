import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_counts = (employee[employee['managerId'].notna()].groupby('managerId').size().reset_index(name= 'report_count'))

    #edge case: no managers? or null grouped?-> remove null 
    merged = employee.merge(report_counts, left_on='id', right_on='managerId', how='left')
    manager = merged[merged['report_count'] >= 5]
    return manager[['name']]
