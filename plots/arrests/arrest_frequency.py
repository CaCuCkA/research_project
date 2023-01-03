import pandas as pd
import matplotlib.pyplot as plt


def plot_arrests_frequency(df: pd.DataFrame) -> None:
    df_2 = df[df['ARREST'] == True]
    df_2['HOUR'] = (df_2['HOUR'] + 1) % 24
    d = df_2.groupby(pd.cut(df_2['HOUR'], [0, 4, 8, 12, 16, 20, 24])).size().to_dict()
    df_t = df
    df_t['HOUR'] = (df_t['HOUR'] + 1) % 24
    d_t = df_t.groupby(pd.cut(df_t['HOUR'], [0, 4, 8, 12, 16, 20, 24])).size().to_dict()
    print(d)
    d_2 = {}
    for key, value in d.items():
        scale = d_t[key] / 100
        print(scale, value)
        k, v = [(int(x) + 23) % 24 for x in str(key)[1:-1].split(', ')]
        d_2.setdefault(f"({k}, {v}]", value/scale)
    s = pd.Series(d_2)
    s.plot(kind='bar')
    plt.title('Arrests by Time')
    plt.xlabel('Time')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()