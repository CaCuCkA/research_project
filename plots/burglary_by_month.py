import pandas as pd
import matplotlib.pyplot as plt


def plot_burglary_by_month(df: pd.DataFrame) -> None:
    df_bulglary = df[(df['TYPE'] == 'BURGLARY')]
    df_bulglary = df_bulglary.groupby(['MONTH']).size()
    df_bulglary.plot(kind='bar')
    plt.title('Burglary by Month')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()