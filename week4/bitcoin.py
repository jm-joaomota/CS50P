import requests
import sys

def main():
    if len(sys.argv) == 2:
        try:
            value = float(sys.argv[1])
            print(bitcoin_price(value))
        except ValueError:
            sys.exit('Command-line argument is not a number')
    else:
        sys.exit('Missing Command-line argument')


def bitcoin_price(num):
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        result = response.json()
        price = result['bpi']['USD']['rate_float']
        amount = price * num
        return f"${amount:,.4f}"
    except requests.RequestException:
        return NONE
main()
