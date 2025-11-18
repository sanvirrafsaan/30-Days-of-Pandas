import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login_df = activity.groupby('player_id', as_index = False)['event_date'].min()
    final_df = first_login_df.rename(
        columns = {
            'event_date': 'first_login'
        }
    )

    return final_df
