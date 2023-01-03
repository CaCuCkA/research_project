import pandas as pd
import matplotlib.pyplot as plt

def plot_crimes_by_time(df: pd.DataFrame) -> None:
    df_t = df['HOUR']
    df_t.value_counts(sort=False).plot(kind='bar')  
    plt.title('Crimes by Time')
    plt.xlabel('Time')
    plt.ylabel('Count')
    plt.show()
