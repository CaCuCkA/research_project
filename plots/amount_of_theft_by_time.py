import pandas as pd
import matplotlib.pyplot as plt


def plot_amount_of_theft_by_time(df):
    df_theft = df[(df['TYPE'] == 'NARCOTICS')]
    df_t = df_theft['HOUR']
    df_t = df_t.apply(lambda x: (x + 1) % 24)
    df_t = df_t.apply(lambda x: 0 if x < 12 else 1)
    d = df_t.value_counts().to_dict()
    d_2 = {}
    for key, value in d.items():
        if key == 0:
            d_2.setdefault("(0-12]", value)
        else:
            d_2.setdefault("(12-24]", value)
    s = pd.Series(d_2)
    s.plot(kind='bar')
    plt.title('Theft by Period of Day')
    plt.xlabel('Time')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()