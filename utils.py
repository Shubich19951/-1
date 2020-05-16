import time
import csv
import requests

from datetime import datetime
from requests.exceptions import ConnectionError
from currencies import currencies


def validate_args(args):
    if len(args) != 4:
        raise ValueError("Unknown arguments!")
    if int(args[1]) not in currencies.values():
        raise ValueError("Unknown currency!")
    datetime.strptime(args[2], "%d-%m-%Y")
    datetime.strptime(args[3], "%d-%m-%Y")


def safe_request(request):
    while True:
        try:
            response = requests.get(request)
            break
        except ConnectionError:
            print("ConnectionError, I try again.")
            time.sleep(1)
    return response


def date_format(date):
    return "-".join(date.split("T")[0].split("-")[::-1])


def shorten_dates(x):
    x_copy = x.copy()
    if len(x_copy) > 31:
        short_x = x_copy[::5]
        return short_x


def generate_file_path(currency, start_date, end_date):
    return r"{}_{}_{}.csv".format(currency, start_date, end_date)


def csv_parse(file_name):
    x = []
    y = []
    with open(file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        first_line = True
        for row in csv_reader:
            if first_line:
                first_line = False
                continue
            x.append(row[0])
            y.append(float(row[1]))
    return x, y
