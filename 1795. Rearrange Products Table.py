import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    new_product = products.melt(
        id_vars = 'product_id',
        var_name = 'store',
        value_name= 'price'
    )
    new_product = new_product.dropna()
    return new_product
