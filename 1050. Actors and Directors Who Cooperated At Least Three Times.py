import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    #find coop_count
    result = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name = 'count') # dataframe output 
    final_result = result[result['count'] >=3 ] # series output 
    

    return final_result[['actor_id', 'director_id']]
