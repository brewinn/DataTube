import pandas as pd
import psycopg2
import os


def main():

    print("Beginning channel data import...", flush=True)
    connection = psycopg2.connect(
        dbname=os.environ.get("SQL_DATABASE"),
        user=os.environ.get("SQL_USER"),
        password=os.environ.get("SQL_PASSWORD"),
        host=os.environ.get("SQL_HOST"),
        port=os.environ.get("SQL_PORT"),
    )

    table = 'datatubeapp_channel'

    df = pd.read_csv('../database/channel_data/USchannels.csv')

    df = df.drop_duplicates(subset=['channel'])

    insert_records = f"INSERT INTO {table} (channel, channel_url, subscribers, views, joined, description) VALUES(%s,%s,%s,%s,%s,%s)"

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
                    row['channel'],
                    row['channel_url'],
                    row['subscribers'],
                    row['views'],
                    row['joined'],
                    row['description'],
                )
                cursor.execute(insert_records, values)

    connection.commit()
    connection.close()
    print("Finished importing channel data.", flush=True)


if __name__ == '__main__':
    main()
