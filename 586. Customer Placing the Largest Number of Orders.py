import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    grouped_df = orders.groupby('customer_number', as_index = False).count().rename(columns = {'order_number': 'order_count'})
    
    sorted_df = grouped_df.sort_values('order_count', ascending=False)

    sorted_df = grouped_df.sort_values('order_count', ascending=False)
    final_val = sorted_df.iloc[0]                      # full row as Series
    customer = final_val['customer_number']            # extract scalar
    
    return pd.DataFrame({'customer_number': [customer]})
    
