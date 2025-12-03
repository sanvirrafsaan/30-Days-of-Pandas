import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # number of times each student attended each exam 
    #there could be subjects for which they took 0 exams. For which we 
    #need to start with a cross join 
    crossed_df = students.merge(subjects, how='cross')
    #student_id, student_name, subject (all) 

    #find count of student to exam attended 
    exam_df = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name = 'attended_exams')
    #student_id, subject_name (for exam attended)
    final_df = crossed_df.merge(exam_df, on=['student_id', 'subject_name'], how='left')
    final_df['attended_exams'] = final_df['attended_exams'].fillna(0)

    final_df = final_df.sort_values(['student_id', 'subject_name'], ascending = True)
    return final_df
