import pandas as pd
from lxml import etree

# csv を読み込んでデータフレームに変換する
df_read_csv = pd.read_csv('conversion-test.csv')
print(df_read_csv)

# データうレームをxml に変換する
df_converted_xml = df_read_csv.to_xml('reconversion-test.xml', encoding='utf-8', xml_declaration=True)
print(df_converted_xml)
