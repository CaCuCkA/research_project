import pandas as pd
import matplotlib.pyplot as plt


def plot_crimes_by_time_2(df: pd.DataFrame) -> None:
    df['HOUR'] = df['HOUR'].apply(lambda x: (x + 1) % 24)
    df['HOUR'] = df['HOUR'].apply(lambda x: "0-12" if x < 12 else "12-24")	
    d = df['HOUR'].value_counts().to_dict()
    print(d)
    df = df.groupby(['TYPE', 'HOUR']).size().unstack(fill_value=0)
    d_2 = df.to_dict()
    for key, value in d_2.items():
        scale = d[key]
        print(scale, value)
        for k, v in value.items():
            value[k] = v / scale
    df = pd.DataFrame(d_2)
    df.plot(kind='bar')
    plt.title('Crimes by Time')
    plt.xlabel('Time')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()