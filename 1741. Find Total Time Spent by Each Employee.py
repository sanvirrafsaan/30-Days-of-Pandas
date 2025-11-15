import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    final_df = employees.groupby(['event_day', 'emp_id'], as_index = False)['time_spent'].sum()
    final_df = final_df.rename(
        columns = {
        'event_day': 'day', 
        'emp_id': 'emp_id',
        'time_spent': 'total_time'
    })
    final_df.sort_values(by= ['emp_id', 'day'], inplace=True)
    return final_df
