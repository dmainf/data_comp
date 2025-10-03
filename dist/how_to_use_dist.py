import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = 'Arial Unicode MS'
matplotlib.rcParams['axes.unicode_minus'] = False
import sys
sys.path.append('../lib')
from plot_dist import *
from prepro import *

print("loading data...")
df_raw = pd.read_csv('../data/data.txt', sep='\t')

space_columns = [
    '書名',
    '著者名'
]
df = df_raw.copy()
for column in space_columns:
    df = delete_space(df, column)
df = normalize_author(df, '著者名')
df = normalize_title(df, '書名')

df_clean = clean_df(df)

#正規化
plot_columns = [
    '書名',
    '著者名'
]
for column in plot_columns:
    plot_distribution(column, df)

#count_encodingしたあとのグラフ
plot_count_columns = [
    '書名',
    '著者名'
]
for column in plot_count_columns:
    plot_count_distribution(column, df_clean)