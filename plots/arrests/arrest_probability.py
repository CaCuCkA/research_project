import pandas as pd
import matplotlib.pyplot as plt


def plot_probability_of_arrest_by_crime_type(df: pd.DataFrame) -> None:
    df['ARREST'] = df['ARREST'] == True
    df_t = df.groupby('TYPE')['ARREST'].mean()
    df_t.plot(kind='bar')
    plt.title('Probability of Arrest by Crime Type')
    plt.xlabel('Type')
    plt.ylabel('Probability')
    plt.tight_layout()
    plt.show()