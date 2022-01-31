# 必要なモジュールをインポートする
from ast import If
import csv
from multiprocessing import context
import xml.etree.ElementTree as ET

# contextに'conversion-test.xml'の値を代入する
context = ET.iterparse(r'conversion-test.xml')

i = 0
# 'conversion-test.csv'を書き込み専用で開き、writerに渡す
with open(r'conversion-test.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # XMLから取り出したcontextの要素をeventにわたし、for文を回す
    for event, elem in context:
        # tagが'country'の場合、csv(writer)に値を書き込む
        if elem.tag == 'country':
            # 更にi=0(先頭のタグ)だった場合はヘッダーを作成する
            if i == 0:
                writer.writerow([data.tag for data in elem])
            writer.writerow([data.text for data in elem])
            i += 1
            elem.clear()
            