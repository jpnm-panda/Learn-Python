from base64 import encode
from operator import index
from os import EX_DATAERR
import pandas as pd
from lxml import etree

tree = etree.parse('conversion-test.xml')
for i in tree.iter():
    tags = i.tag
    texts = i.text
    print(tags)
    print(texts)
