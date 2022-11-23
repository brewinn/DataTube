import pandas as pd
import psycopg2
import os


def main():

    print("Beginning video data import...", flush=True)
    connection = psycopg2.connect(
        dbname=os.environ.get("SQL_DATABASE"),
        user=os.environ.get("SQL_USER"),
        password=os.environ.get("SQL_PASSWORD"),
        host=os.environ.get("SQL_HOST"),
        port=os.environ.get("SQL_PORT"),
    )

    table = 'datatubeapp_video'

    df = pd.read_csv('../database/kaggle_data/USvideos.csv')

    df = df.drop_duplicates(subset=['video_id'])

    insert_records = f"INSERT INTO {table} (videoid, title, views, published, likes, dislikes, commentcount, description, channel, categoryid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    with connection.cursor() as cursor:
        select_all = f"SELECT * FROM {table}"
        cursor.execute(select_all)
        rows = cursor.fetchall()
        if len(rows) > 0:
            print(f"Table {table} not empty, aborting import...", flush=True)
            connection.close()
            return

        else:
            for _, row in df.iterrows():
                values = (
                    row['video_id'],
                    row['title'],
                    row['views'],
                    row['publish_time'],
                    row['likes'],
                    row['dislikes'],
                    row['comment_count'],
                    row['description'],
                    row['channel_title'],
                    row['category_id'],
                )
                cursor.execute(insert_records, values)

    connection.commit()
    connection.close()
    print("Finished importing video data.", flush=True)


if __name__ == '__main__':
    main()
