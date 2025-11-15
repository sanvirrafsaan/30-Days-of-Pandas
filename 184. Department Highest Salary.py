import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salary_per_dept = (employee.groupby('departmentId', as_index = False)['salary'].max())

# max_salary has columns departmentId, salary
    top_salaries = (max_salary_per_dept.merge(employee, on=['departmentId', 'salary'], how='inner'))
# top_salary has columns id, name, salary, departmnetId
    final_df = top_salaries.merge(department, left_on='departmentId', right_on='id', how='left')

# final_df has columns id_x, name_x, salary, departmentId, id_y, name_y
#rename columns 
    result = final_df[['name_y', 'name_x', 'salary']].rename(
        columns = {
            'name_y': 'Department', 
            'name_x': 'Employee',
            'salary': 'Salary'
        }
    )
    return result
