import pandas as pd
import psycopg2
import os

def main():

    print("Beginning data import...", flush=True)    
    connection = psycopg2.connect(
            dbname=os.environ.get("SQL_DATABASE"), 
            user=os.environ.get("SQL_USER"), 
            password=os.environ.get("SQL_PASSWORD"),
            host=os.environ.get("SQL_HOST"), 
            port=os.environ.get("SQL_PORT"), 
            )

    table = 'datatubeapp_video'

    df = pd.read_csv('../database/kaggle_data/USvideos.csv')
    df = df[['video_id', 'title', 'description']]

    df = df.drop_duplicates(subset=['video_id'])

    insert_records = f"INSERT INTO {table} (videoid, title, description) VALUES(%s,%s,%s)"

    with connection.cursor() as cursor:
        select_all = f"SELECT * FROM {table}"
        cursor.execute(select_all)
        rows = cursor.fetchall()
        if len(rows) > 0:
            print(f"Table {table} not empty, aborting import...", flush=True)
            
        else:
            for _, row in df.iterrows():
               values = (row['video_id'], row['title'],row['description'])
               cursor.execute(insert_records, values)
    

    connection.commit()
    connection.close()
    print("Finished importing data.", flush=True)    

if __name__ == '__main__':
    main()
