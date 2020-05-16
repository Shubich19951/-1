import sys
from utils import validate_args, generate_file_path
from scraper import get_rates
import pandas as pd
from plot_graphs import plot_graph,\
                        plot_std,\
                        plot_changes,\
                        plot_histogram,\
                        plot_decompose


def main():
    try:
        validate_args(sys.argv)
    except ValueError as e:
        print(e.args[0])
        return

    currency, start_date, end_date = sys.argv[1:]
    currency = int(currency)
    get_rates(currency, start_date, end_date)

    df = pd.read_csv(generate_file_path(currency, start_date, end_date), sep=',')
    label = f"BYN/{currency} {start_date} - {end_date}"
    df.index = pd.to_datetime(df['day'].values, format="%d-%m-%Y")
    df = df.drop(['day'], axis=1)
    df_month = df.resample('M').mean()
    df_quarter = df.resample('Q').mean()
    # plotting
    plot_graph(df, label, 'Day')
    plot_graph(df_month, label, 'Month')
    plot_graph(df_quarter, label, 'Quarter')
    plot_decompose(df)
    plot_changes(df, label, 'Day')
    plot_histogram(df, 'Day', 12)
    plot_std(df, label, 'Day')


if __name__ == "__main__":
    main()
