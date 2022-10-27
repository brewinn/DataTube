import pandas as pd
import sqlite3

connection = sqlite3.connect("../datatube/db.sqlite3")
table = 'datatubeapp_video'

cursor = connection.cursor()

df = pd.read_csv('kaggle_data/USvideos.csv')
df = df[['video_id', 'title']]

print(df.head())

insert_records = f"INSERT INTO {table} (videoid, title) VALUES(?,?)"

for _, row in df.iterrows():
    values = (row['video_id'], row['title'])
    cursor.execute(insert_records, values)

select_all = f"SELECT * FROM {table}"
rows = cursor.execute(select_all).fetchall()
print('Inside the database:')
for index, row in enumerate(rows):
    print(row)
    if index > 3:
        break

connection.commit()
connection.close()
