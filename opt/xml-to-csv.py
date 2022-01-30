# まず、必要なモジュールをインポートする
from ast import If
import csv
from multiprocessing import context
import xml.etree.ElementTree as ET

context = ET.iterparse(r'conversion-test.xml')

i = 0
with open(r'conversion-test.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    for event, elem in context:
        if elem.tag == 'country':
            if i == 0:
                writer.writerow([data.tag for data in elem])
            writer.writerow([data.text for data in elem])
            i += 1
            elem.clear()
