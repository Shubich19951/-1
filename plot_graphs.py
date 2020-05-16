from matplotlib import pyplot as plt
import statsmodels.tsa.api as sm
import numpy as np
import seaborn as sn
from utils import shorten_dates

sn.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (20, 10)


def plot_graph(df, label, season):
    plt.title(f'График зависимости курса валюты от времени ({season})')
    plt.plot(df, "-", linewidth=1, label=label)
    plt.xticks(shorten_dates(df.index.values), rotation=90)
    plt.legend()
    plt.ylabel('Курс валют')
    plt.xlabel('Время')
    plt.show()


def plot_changes(df, label, season):
    plt.title(f'График зависимости изменения курса валюты от времени ({season})')
    plt.plot((df['rate'] - df['rate'].shift(1))[1:], "-", linewidth=1, label=label)
    plt.xticks(shorten_dates(df.index.values), rotation=90)
    plt.legend()
    plt.ylabel('Курс валют')
    plt.xlabel('Время')
    plt.show()


def plot_histogram(df, season, bins):
    plt.title(f'Равноинтервальная гистограмма курса валют ({season})')
    hist_data = np.histogram(df['rate'].values, bins)
    plt.hist(df['rate'].values, bins, label='Гистограмма')
    plt.plot(hist_data[1][1:], hist_data[0], linestyle='--', color='red', linewidth=5, label='Аппроксимация гистограммы')
    plt.legend()
    plt.xlabel('Курс валют')
    plt.ylabel('Количество вхождений в интервал')
    plt.show()


def plot_std(df, label, season):
    plt.title(f'График зависимости cреднеквадратического отклонения'
              f'курса валюты с окном в 5 дней от времени ({season})')
    plt.plot(df.index[::5].values, [df['rate'][i:i + 5].std() for i in range(0, len(df), 5)], linewidth=1, label=label)
    plt.xticks(shorten_dates(df.index.values), rotation=90)
    plt.legend()
    plt.ylabel('Среднеквадратическое отклонение')
    plt.xlabel('Время')
    plt.show()


def plot_decompose(df):
    sm.seasonal_decompose(df['rate']).plot()
    plt.show()
