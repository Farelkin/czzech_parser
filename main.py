import re
import sqlite3

import requests
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup

from sql_commands import create_main_table


def get_data(data_link):
    """
    Function fint data in users link
    :param data_link: str: users link
    :return: pandas.DataFrame: data
    """
    r = requests.get(data_link)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table')
        links = [item['data-href'] for item in table.find_all('tr', attrs={'data-href': True})]

        df = pd.read_html(data_link, flavor='html5lib')[0]

        terrace_area = []
        for link in links:
            r2 = requests.get(link)
            if r2.status_code == 200:
                soup2 = BeautifulSoup(r2.text, 'html.parser')
                _terrace_area = \
                    soup2.find('div', class_='block block-inline', ).find_all(text=re.compile('Terasa:(.*)'))
                try:
                    terrace_area.append(float(re.findall(r'\d{2},\d{2}', _terrace_area[0])[0].replace(',', '.')))
                except IndexError:
                    terrace_area.append(0.0)
            else:
                print(f'For link {link} error code {r.status_code}')

        df['link'] = links
        df['terrace'] = terrace_area

        df['Jednotka'].astype('Int64')
        df['Podlaží'] = df['Podlaží'].apply(lambda row: int(re.findall(r'^\d', row)[0]))
        df['Plocha'] = df['Plocha'].apply(lambda row: re.findall(r'\d{2},\d{2}', row))
        df['Plocha'] = df['Plocha'].apply(lambda row: float(row[0].replace(',', '.')) if row else float(0))
        df['Stav'] = df['Stav'].replace(
            {
                'rezervováno': 'reserved',
                'volný': 'available',
                'připravujeme': 'sold'
            })
        df['Cena (v Kč)'] = df['Cena (v Kč)'].apply(lambda row: int(row.replace(" ", "")) if row is not np.nan else 0)

        df.rename(
            columns={
                'Jednotka': 'ID',
                'Dispozice': 'floor_plan',
                'Podlaží': 'floor',
                'Plocha': 'area',
                'Stav': 'status',
                'Cena (v Kč)': 'price',
                'Typ': 'type'
            },
            inplace=True
        )
        return df

    else:
        print(f'For link {data_link} error code {r.status_code}')


def write_to_db(data):
    """
    Function create and write data to the DB SQLite3
    :param data: pandas.DataFrame: data from parser
    :return: None
    """
    conn = sqlite3.connect('tech_specdb.sqlite3')
    cur = conn.cursor()
    cur.execute(create_main_table())
    conn.commit()
    data.to_sql('parser_data', con=conn, if_exists="append", index=False)


if __name__ == '__main__':
    user_link = r'https://www.italska8.cz/byty'
    write_to_db(get_data(user_link))
