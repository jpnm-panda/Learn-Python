from base64 import encode
from operator import index
import pandas as pd
from lxml import etree

# xml を読み込んでデータフレームに変換する
df_read_xml = pd.read_xml('conversion-test.xml', encoding='utf-8', parser='lxml')
print(df)

# データフレームをcsv に変換する
df_converted_csv = df_read_xml.to_csv('conversion-test.csv', encoding='utf-8', index=False)
print(df_converted_csv)
