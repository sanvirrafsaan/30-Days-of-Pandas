import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.drop_duplicates(subset = ['sell_date', 'product'])
    grouped_df = df.groupby('sell_date', as_index = False).agg(
        num_sold = ('product', 'nunique'), 
        products = ('product', lambda x: ','.join(sorted(x))) 
    )
    return grouped_df
