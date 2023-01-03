import pandas as pd
import matplotlib.pyplot as plt


def theft_battery_arrest_comparison(df: pd.DataFrame) -> None:
    df_theft = df[(df['TYPE'] == 'THEFT')]
    df_battery = df[(df['TYPE'] == 'BATTERY')]
    df_theft['ARREST'] = df_theft['ARREST'] == True
    df_battery['ARREST'] = df_battery['ARREST'] == True
    df_theft['ARREST'].value_counts().plot(kind='bar')
    plt.title('Arrests for Theft')
    plt.xlabel('Arrest')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
    df_battery['ARREST'].value_counts().plot(kind='bar')
    plt.title('Arrests for Battery')
    plt.xlabel('Arrest')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
  