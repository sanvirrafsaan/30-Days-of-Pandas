import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    grouped_df = courses.groupby('class', as_index = False)['student'].count().rename(columns = {'student': 'student_count'})
    final_df = grouped_df[(grouped_df['student_count'] >= 5)]
    return final_df[['class']]
