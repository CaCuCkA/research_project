import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_arrests_by_month(df: pd.DataFrame) -> None:
    df = df.groupby(['ARREST', 'MONTH']).size().unstack(fill_value=0) 
    arrested = []
    not_arrested = []
    labels = []
    d = df.to_dict()
    for key, value in d.items():
        total = value[True] + value[False]
        arrested.append(value[True] / total)
        not_arrested.append(value[False] / total)
        labels.append(key)
    df = pd.DataFrame({'Arrested': arrested, 'Not Arrested': not_arrested}, index=labels)
    df.plot(kind='bar', stacked=True)
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.title('Arrests by Month')
    plt.xlabel('Month')
    plt.ylabel('Probability')
    plt.tight_layout()
    plt.show()