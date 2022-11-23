import json


def process_json_mapping(json_file):
    with open(json_file) as f:
        data = json.load(f)
        mapping = dict()
        for item in data['items']:
            mapping[item['id']] = item['snippet']['title']
        return mapping


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    mapping = process_json_mapping(args.filename)
    print(mapping)
