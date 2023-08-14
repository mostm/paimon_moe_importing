import json

import requests
from bs4 import BeautifulSoup, Tag
from datetime import date, time, datetime, timezone, timedelta

YOUR_GENSHIN_REGION = "Europe"  # Possible values: "Europe", "America", "Asia"


def proper_timezone():
    if YOUR_GENSHIN_REGION.lower().startswith("am"):
        tz = timezone(timedelta(hours=-5))
    elif YOUR_GENSHIN_REGION.lower().startswith("as"):
        tz = timezone(timedelta(hours=8))
    else:  # YOUR_GENSHIN_REGION.lower().startswith("eu")
        tz = timezone(timedelta(hours=1))
    return tz


def load_page():
    url = 'https://genshin-impact.fandom.com/wiki/Wish/History'
    r = requests.get(url)
    return r.text


def load_page_static():
    with open('banner_history_wiki\Wish History _ Genshin Impact Wiki _ Fandom.html', 'r') as f:
        return f.read()


def parse_table(table: Tag):
    header = table.find('thead')
    header_row = header.find('tr')
    header_cells = header_row.find_all('th')
    header_titles = [x.text.strip() for x in header_cells]
    # print(header_titles)
    if header_titles[0] != 'Wish':
        print('Skipping table {}, possible table was reformatted since parser was written'.format(header_titles))
        return None

    body = table.find('tbody')
    body_rows = body.find_all('tr')

    reset_time = time(hour=5, minute=0, second=0)  # UTC+1 == Europe

    banners = []
    last_banner_time = None

    for body_row in body_rows:
        body_cells = body_row.find_all('td')
        body_values = [x.text.strip() for x in body_cells]

        banner_name = body_values[0]
        if banner_name in ["Beginners' Wish", "Wanderlust Invocation"] or "TBA" in body_values[2]:
            continue
        banner_date = [x for x in banner_name.split(' ') if x.startswith('20')][0]

        banner_name = " ".join(banner_name.split(" ")[:-1]).strip()

        banner_type = "301" if banner_name != "Epitome Invocation" else "302"

        banner_date += " 04:00:00"
        banner_dt = datetime.strptime(banner_date, '%Y-%m-%d %H:%M:%S')
        tz = proper_timezone()
        banner_dt = banner_dt.astimezone(tz)

        banner_when = int(banner_dt.timestamp())

        second_character_wish = all([
            last_banner_time is not None,
            last_banner_time == banner_when,  # First character wish was present
            banner_type == "301"  # Character wish
        ])
        if second_character_wish:
            print(second_character_wish)
            banner_type = "400"
        last_banner_time = banner_when

        banners.append({
            'name': banner_name,
            'type': banner_type,
            'when': banner_when,
        })

    return banners


def parse_page(page_text):
    results = []

    soup = BeautifulSoup(page_text, 'lxml')
    tables = soup.find_all('table', class_='article-table alternating-colors-table sortable jquery-tablesorter')
    for table in tables:
        results += parse_table(table)

    return results


def main():
    page = load_page_static()
    banners = parse_page(page)
    with open('banner_history.json', 'w') as f:
        json.dump(banners, f, indent=4)


if __name__ == '__main__':
    main()
