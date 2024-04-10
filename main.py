# import pandas as pd
#
# data = pd.read_xml('data/29-28-104155-13_5c7ca0bc-4fad-20e3-55af-42e6ae387be8.xml', encoding='UTF-8')
#
# """
# Index(['ext_object_id', 'code', 'value', 'last_container_fixed_at', 'date_c',
#        'object_code', 'object_name', 'object_type', 'cadastralnumber',
#        'regdate', 'hash_id', 'address_type', 'note', 'okato', 'kladr',
#        'region', 'city', 'street', 'level1', 'item', 'cad_cost_value',
#        'cad_cost_unit', 'groundcategory_code', 'groundcategory_name',
#        'utilization_bydoc_name', 'utilization_bydoc_code'],
#
#       dtype='ext_object_id')
# """
#
# print(data['code'])
#
# data.to_csv('r_data/1.csv', sep=';', encoding='UTF-8')
#
# # print(data.head())
#
# # def read_file(file_path):
# #     pass


import xml.etree.ElementTree as ET
from pprint import pprint
import psycopg2
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# def conn_db():
#     db_params = {
#         'host': '127.0.0.1',
#         'port': 5432,
#         'database': 'northwind',
#         'user': 'postgres',
#         'password': '1234',
#     }
#
#     conn = psycopg2.connect(**db_params)
#
#     return conn


query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
          AND table_type = 'BASE TABLE';
"""

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="northwind",
    user="postgres",
    password=os.environ.get('postgres_password')
)

cur = conn.cursor()

cur.execute(query)

result = cur.fetchall()

print(result)

cur.close()
conn.close()


tree = ET.parse('data/29-22-0-505-01-292_5c7ca0bc-4fad-20e3-55af-42e6ae387be8.xml')
root = tree.getroot()

data = {}

for child in root:
    if child.tag not in data:
        data[child.tag] = []
    if len(child) > 0:
        child_data = {}
        for sub_child in child:
            child_data[sub_child.tag] = sub_child.text
        data[child.tag].append(child_data)
    else:
        data[child.tag].append(child.text)

pprint(data)

# import pandas
#
# df = pandas.DataFrame(data)
#
# # df.to_csv('r_data/1.csv', sep=';', encoding='utf-8-sig', index=False)
#
# a = df.to_dict(orient='records')
# print(df['object_name'])
#
#
# pprint(a)
