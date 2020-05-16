import os
import json
import pandas as pd

from currencies import currencies
from utils import safe_request, date_format, generate_file_path


def get_rates(currency, start_date, end_date):
    csv_file_path = generate_file_path(currency, start_date, end_date)
    if os.path.isfile(csv_file_path):
        return

    url = "http://www.nbrb.by/API/ExRates/Rates/Dynamics/{}?startDate={}&endDate={}"
    request = url.format(
        currency,
        "-".join(start_date.split("-")[::-1]),
        "-".join(end_date.split("-")[::-1]),
    )

    data = json.loads(safe_request(request).text)
    df = pd.DataFrame(
        {
            "day": [date_format(i["Date"]) for i in data],
            "rate": [i["Cur_OfficialRate"] for i in data],
        }
    )

    with open(generate_file_path(currency, start_date, end_date), "w") as csv_file:
        csv_file.write(df.to_csv(index=False))
