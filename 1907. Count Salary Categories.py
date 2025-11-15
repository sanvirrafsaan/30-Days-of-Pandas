import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts[accounts["income"] < 20000].shape[0]
    avg_salary = accounts[(accounts["income"] >= 20000) & (accounts["income"] <= 50000)].shape[0]
    high_salary = accounts[accounts["income"] > 50000].shape[0]
    
    result_df = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'], 
        'accounts_count': [low_salary, avg_salary, high_salary]
    })
    return result_df
