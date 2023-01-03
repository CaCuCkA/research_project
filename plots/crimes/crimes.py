import pandas as pd
import matplotlib.pyplot as plt

def plot_crimes(df: pd.DataFrame) -> None:
    df['TYPE'].value_counts().plot(kind='bar')
    plt.title('Crimes by Type')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
