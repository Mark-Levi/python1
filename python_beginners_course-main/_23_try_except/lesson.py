# def find_average(*, numbers: list) -> float:
#     return sum(numbers) / len(numbers)


# try:
#     find_average(numbers=[])
# except ZeroDivisionError:
#     print("Empty list")
import requests
import json


try:
    url = "https://api.binance.com/api/v3/ticker/price1"
    response = requests.get(url, params={"symbol": "BTCUSDT"})
    print(response)
    print(response.content)
    print(type(response))
    price_object = response.json()
    print(price_object["price"])
except json.decoder.JSONDecodeError as error:
    print(f"Error request: {error}")
