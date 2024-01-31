import requests
from datetime import datetime


API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
DEFAULT_OUTPUT_FILE = "exchange_rates.txt"


def get_exchange_rates(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to retrieve exchange rates. Error: {e}")
        return None
    except ValueError as e:
        print(f"Failed to parse JSON. Error: {e}")
        return None


def format_currency_line(currency):
    name = currency['txt']
    rate = currency['rate']
    return f"{name} to UAH: {rate}"


def write_to_file(data, file_path):
    date_format = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("exchange_rates.txt", "w", encoding="utf-8") as file:
        file.write(f"[{date_format}]\n\n")
        for currency in data:
            file.write(format_currency_line(currency) + "\n")


def check_currency_nbu(api_url=API_URL, output_file=DEFAULT_OUTPUT_FILE):
    exchange_rates_data = get_exchange_rates(api_url)

    if exchange_rates_data:
        write_to_file(exchange_rates_data, output_file)
        print(f"Exchange rates successfully written to '{output_file}'")
    else:
        print("Exchange rates not retrieved")


check_currency_nbu()

