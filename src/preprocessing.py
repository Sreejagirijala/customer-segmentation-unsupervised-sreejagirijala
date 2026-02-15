import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.dropna(subset=['Customer ID'])
    df = df[df['Quantity'] > 0]
    df = df[df['Price'] > 0]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

def create_rfm(df):
    df['TotalAmount'] = df['Quantity'] * df['Price']

    rfm = df.groupby('Customer ID').agg({
        'InvoiceDate': 'max',
        'Invoice': 'count',
        'TotalAmount': 'sum'
    }).reset_index()

    rfm.columns = ['CustomerID', 'LastPurchase', 'Frequency', 'Monetary']
    rfm['Recency'] = (rfm['LastPurchase'].max() - rfm['LastPurchase']).dt.days

    return rfm[['Recency', 'Frequency', 'Monetary']]

def scale_features(data):
    scaler = StandardScaler()
    return scaler.fit_transform(data)

