import pandas as pd
import psycopg2
import os

connection = psycopg2.connect(
        dbname=os.environ.get("SQL_DATABASE"), 
        user=os.environ.get("SQL_USER"), 
        password=os.environ.get("SQL_PASSWORD"),
        host=os.environ.get("SQL_HOST"), 
        port=os.environ.get("SQL_PORT"), 
        )

table = 'datatubeapp_video'

cursor = connection.cursor()

df = pd.read_csv('../database/kaggle_data/USvideos.csv')
df = df[['video_id', 'title', 'description']]

print(df.head())

insert_records = f"INSERT INTO {table} (videoid, title, description) VALUES(%s,%s,%s)"

for _, row in df.iterrows():
    values = (row['video_id'], row['title'],row['description'])
    cursor.execute(insert_records, values)

select_all = f"SELECT * FROM {table}"
cursor.execute(select_all)
rows = cursor.fetchall()
print('Inside the database:')
for index, row in enumerate(rows):
    print(row)
    if index > 3:
        break

connection.commit()
connection.close()
