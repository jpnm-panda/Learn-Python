# 必要なモジュールをインポートする
import xmltodict

# XMLの値を辞書に変換する
with open('conversion-test.xml', encoding='utf-8') as fd:

    dict_data = xmltodict.parse(fd.read())
 
    print(dict_data)
