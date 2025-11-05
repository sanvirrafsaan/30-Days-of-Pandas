import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_df = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if N > len(unique_df) or N <= 0: 
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    nth_highest = unique_df.iloc[N - 1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})
