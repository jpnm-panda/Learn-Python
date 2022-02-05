from array import array
from operator import index
from textwrap import indent
from turtle import update
import pandas as pd
import numpy as np

# 辞書型のデータをつくる
data = {
    'Name': 'John',
    'Sex': 'male',
    'Age': 22
}

# data の値からpandas を使ってSeries をつくる
df = pd.Series(data)
print(df.head())

# numpy でつくったarray をSeries に変換してみる
array = np.array([22, 31, 42, 23])
df = pd.Series(array)
print(df)

# 作ったSeries にindex をつけてみる
array = np.array(['John', 'male', 22])
df = pd.Series(array, index=['name', 'Sex', 'Age'])
print(df)

# numpy で配列を作って、DataFrame に変換する
ndarray = np.arange(10).reshape(2, 5)
print(ndarray)
df = pd.DataFrame(ndarray, index=['index1', 'index2'], columns=['a', 'b', 'c', 'd', 'e'])
print(df)

# 値に配列を入れた辞書型を用意し、DataFrame に変換する
data = {
    'name': ['john', 'Zack', 'Emily'],
    'sex': ['name', 'male', 'female'],
    'age': [22, 30, 32]
}
df = pd.DataFrame(data)
print(df)

#csv をDataFrame に変換する
df = pd.read_csv('dataset/tmdb_5000_movies.csv')

# 統計情報を表示する
print(df.describe())

# headerの値を表示する
print(df.columns)

# 指定したcolumn を表示する
print(df[['revenue', 'budget', 'keywords']].head(3))

# 指定した範囲のrow を表示する
print(df.iloc[10:13])

# 特定のSeries を削除し表示する
print(df.head(3))
print(df.drop(0).head(3)) # 指定したrow を削除して表示する
print(df.drop('id', axis=1).head(3)) # 指定したcolumn を削除して表示する

# budget やrevenue が0のものをfilter out する
df = df[~((df['budget'] == 0) | (df['revenue'] == 0))] 

# profit というカラムを作成する
df['profit'] = df.apply(lambda row: row['revenue'] - row['budget'], axis = 1)

# profit でソートする
print(df.sort_values('profit', ascending=False).head(3))

# csv で保存する
df.to_csv('dataset/tmdb_5000_movies_profit_sorted.csv', index=False)

# 保存したcsv を読み込んで確認する
updated_df = pd.read_csv('dataset/tmdb_5000_movies_profit_sorted.csv')
print(updated_df.head(3))
