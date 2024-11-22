import pandas as pd
from sqlalchemy import create_engine

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('/home/ts/Downloads/task_update_202410040951.csv')

# Connect to the PostgreSQL database
engine = create_engine('postgresql://postgres:postgres@localhost:5432/spark_db')

# Write the DataFrame to a PostgreSQL table
df.to_sql('task_update', engine, if_exists='append', index=False)