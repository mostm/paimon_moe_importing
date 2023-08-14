import json
from contextlib import suppress


def main():
    banner_history = []  # Used for suppression
    with suppress(FileNotFoundError, json.decoder.JSONDecodeError):
        with open('banner_history.json', 'r') as f:
            banner_history = json.load(f)

    when = input('When did you see banner update (UNIX timestamp)? ')
    banner_count = int(input('How many banners did you see? '))
    for i in range(banner_count):
        banner = input('Enter a banner name: ')
        banner_type = input('What type of banner was it ([W]eapon/[C]haracter/[2]-nd Character)? ')
        banner_type = banner_type.lower()
        if banner_type == 'w':
            banner_type = '301'
        elif banner_type == 'c':
            banner_type = '302'
        elif banner_type == '2':
            banner_type = '400'

        banner_history.append({'banner': banner, 'when': when, 'type': banner_type})

    with open('banner_history.json', 'w') as f:
        json.dump(banner_history, f, indent=4)


if __name__ == '__main__':
    print("Deprecated! Use banner_parser.py instead.")
    # main()
