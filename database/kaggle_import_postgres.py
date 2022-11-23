import pandas as pd
import psycopg2
import os
from json_mapping import process_json_mapping


def parse_tags(tags):
    return tags.replace('"', '').split('|')


def main():

    print("Beginning video data import...", flush=True)
    connection = psycopg2.connect(
        dbname=os.environ.get("SQL_DATABASE"),
        user=os.environ.get("SQL_USER"),
        password=os.environ.get("SQL_PASSWORD"),
        host=os.environ.get("SQL_HOST"),
        port=os.environ.get("SQL_PORT"),
    )

    video_table = 'datatubeapp_video'
    tag_table = 'datatubeapp_tag'

    df = pd.read_csv('../database/kaggle_data/USvideos.csv')
    mapping = process_json_mapping('../database/kaggle_data/US_category_id.json')

    df = df.drop_duplicates(subset=['video_id'])

    insert_video_records = f"INSERT INTO {video_table} (videoid, title, views, published, likes, dislikes, commentcount, description, channel, categoryid, category) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    insert_tag_records = f"INSERT INTO {tag_table} (videoid, tag) VALUES (%s,%s)"

    with connection.cursor() as cursor:
        select_all = f"SELECT * FROM {video_table}"
        cursor.execute(select_all)
        rows = cursor.fetchall()
        if len(rows) > 0:
            print(f"Table {video_table} not empty, aborting import...", flush=True)
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
                    mapping[str(row['category_id'])],
                )
                tag_entries = parse_tags(row['tags'])
                for tag in tag_entries:
                    cursor.execute(insert_tag_records, (row['video_id'], tag))
                cursor.execute(insert_video_records, values)

    connection.commit()
    connection.close()
    print("Finished importing video data.", flush=True)


if __name__ == '__main__':
    main()
