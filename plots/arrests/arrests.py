import pandas as pd
import matplotlib.pyplot as plt


def plot_arrests(df: pd.DataFrame) -> None:
    df['ARREST'].value_counts().plot(kind='bar')
    plt.title('Arrests')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
