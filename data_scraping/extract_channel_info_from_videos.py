# Adapted from https://www.thepythoncode.com/article/get-youtube-data-python
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import re
import ast
import pandas as pd
from tqdm import tqdm
import time
import pyppeteer


def get_channel_ids(url, channel, session, MAX_WAIT=3):
    # initialize the result
    result = {}

    # Set start time
    start_time = time.time()
    while True:
        try:
            # download HTML code
            response = session.get(url)
            # execute Javascript
            response.html.render(timeout=60)
            # create beautiful soup object to parse HTML
            soup = bs(response.html.html, "html.parser")

            # Extract channel name and url data
            channel_data = re.search(
                r''' <span itemprop="author" itemscope="" itemtype="http://schema.org/Person">\s*?<link href="(.*?)" itemprop="url"/>\s*?<link content="(.*?)" itemprop="name"/>\s*?</span>''', soup.prettify())

            result['channel_url'] = channel_data.group(1)
            result['channel_name'] = channel_data.group(2)

            return result
        except (TypeError, AttributeError, pyppeteer.errors.TimeoutError):
            if time.time() - start_time > MAX_WAIT:
                result['channel_url'] = None
                result['channel_name'] = channel
                return result
            time.sleep(0.5)


def get_channel_info(channel_url, session, MAX_WAIT=3):
    if channel_url is None:
        return {'subscribers': None, 'views': None, 'joined': None, 'description': None}

    # Set start time
    start_time = time.time()
    while True:
        try:
            # Use about page link
            about_url = channel_url + '/about'
            # download HTML code
            response = session.get(about_url)
            # execute Javascript
            response.html.render(timeout=60)
            # create beautiful soup object to parse HTML
            soup = bs(response.html.html, "html.parser")

            # initialize the result
            result = {}

            # Get channel information
            subscriber_data = re.search(
                r',"simpleText":"(.*?)"},', soup.prettify()).group(1)
            view_data = re.search(
                r'"viewCountText":{"simpleText":"(.*?)"},', soup.prettify()).group(1)
            joined_data = re.search(
                r'{"text":"Joined "},{"text":"(.*?)"}', soup.prettify()).group(1)
            description_data = re.search(
                r'{"description":{"simpleText":"(.*?)"},', soup.prettify()).group(1)

            result['subscribers'] = subscriber_data
            result['views'] = view_data
            result['joined'] = joined_data
            result['description'] = ast.literal_eval(f'"{description_data}"')

            return result

        except (TypeError, AttributeError, pyppeteer.errors.TimeoutError):
            if time.time() - start_time > MAX_WAIT:
                result['subscribers'] = None
                result['views'] = None
                result['joined'] = None
                result['description'] = None
                return result
            time.sleep(0.5)


def extract_channel_info_from_videos(videos, channels=None, prior_channels=None):
    # init session
    session = HTMLSession()

    # Track processed_channels
    processed_channels = prior_channels if prior_channels else set()

    # Store newly processed data in dataframe
    df = pd.DataFrame(columns=['channel', 'channel_url',
                      'subscribers', 'views', 'joined', 'description'])
    for index, video in tqdm(enumerate(videos), total=len(videos)):
        channel_ids = get_channel_ids(
            video, channels[index] if channels else None, session)
        if channel_ids['channel_name'] in processed_channels:
            continue

        channel_info = get_channel_info(channel_ids['channel_url'], session)
        temp_df = pd.DataFrame({
            "channel": channel_ids['channel_name'],
            "channel_url": channel_ids['channel_url'],
            "subscribers": channel_info['subscribers'],
            "views": channel_info['views'],
            "joined": channel_info['joined'],
            "description": channel_info['description'],
        }, index=[len(df)])
        df = pd.concat([df, temp_df], axis=0)
        processed_channels.add(channel_ids['channel_name'])

    return (df, processed_channels)


def extract_video_ids_from_kaggle_data(csv):
    df = pd.read_csv(csv, encoding='latin1')
    videos = df[['video_id', 'channel_title']
                ].drop_duplicates(subset="video_id")
    return videos


def get_video_urls_from_kaggle_data(csv):
    video_ids = extract_video_ids_from_kaggle_data(csv)
    urls = [
        f'https://www.youtube.com/watch?v={video_id["video_id"]}' for _, video_id in video_ids.iterrows()
    ]
    channels = [video_id['channel_title']
                for _, video_id in video_ids.iterrows()]
    return (urls, channels)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="YouTube Channel Data Extractor")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-u", "--url", help="URLs of the YouTube videos", nargs='+')
    group.add_argument(
        "-c", "--csv", help="CSV file of kaggle data to extract videos from")

    args = parser.parse_args()

    # parse the video URL from command line
    if args.csv:
        urls, channels = get_video_urls_from_kaggle_data(args.csv)
        df, processed_channels = extract_channel_info_from_videos(
            urls, channels)
    else:
        urls = args.url
        df, processed_channels = extract_channel_info_from_videos(urls)

    print(f'{processed_channels=}\n')
    print(df)
    df.to_csv('output.csv', index=False)
