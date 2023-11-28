import requests
import sys

link = "https://api.coindesk.com/v1/bpi/currentprice.json"


try:
    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)
    elif not float(sys.argv[1]):
        print("Command-line argument is not a number")
        sys.exit(1)
    else:
        c = float(sys.argv[1])

except (ValueError, TypeError):
    print("Command-line argument is not a number")
    sys.exit(1)




try:
    r = requests.get(link).json()
    p = r["bpi"]["USD"]["rate_float"]
    price = c * p

except requests.RequestException:
    print("CONNECTION ERROR")
    sys.exit(1)

print(f"${price:,.4f}")