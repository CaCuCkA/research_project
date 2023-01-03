import pandas as pd
import matplotlib.pyplot as plt


def plot_crimes_by_season(df: pd.DataFrame) -> None:
    df['MONTH'] = df['MONTH'].apply(lambda x: 0 if x < 4 else 1 if x < 7 else 2 if x < 10 else 3)
    df = df.groupby(['TYPE', 'MONTH']).size().unstack(fill_value=0)
    # plot df
    df.plot(kind='bar')
    plt.title('Crimes by Season')
    plt.xlabel('Season')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()