import requests
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple"
newapi = "REDACTED"
# Get Change in Stock Price
alpha_url = "https://www.alphavantage.co/query"
stock_api = "REDACTED"
stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api
}

stock_data = requests.get(url=alpha_url, params=stock_param)
stock_data = stock_data.json()
today = list(stock_data["Time Series (Daily)"])[0]
yesterday = list(stock_data["Time Series (Daily)"])[1]
stock_data = stock_data["Time Series (Daily)"]
stock_price_change = round(float(stock_data[today]["4. close"]) - float(stock_data[yesterday]["4. close"]), 2)
change_percentage = round(((stock_price_change * 100) / round(float(stock_data[yesterday]["4. close"]), 2)), 2)
if change_percentage > 0:
    change_percentage = "🔺 " + str(change_percentage)
else:
    change_percentage = "🔻 " + str(change_percentage)

# Get the latest article from news api
news_param = {
    "q": COMPANY_NAME,
    "from": today,
    "apiKey": newapi
}
news_url = "https://newsapi.org/v2/everything?"
news_data = requests.get(news_url, params=news_param)
news_data = news_data.json()
try:
    news_title1 = news_data["articles"][0]["title"]
    news_title2 = news_data["articles"][1]["title"]
    news_title3 = news_data["articles"][2]["title"]
except KeyError:
    pass

account_sid = "REDACTED"
account_auth = "REDACTED"
acc_no = "REDACTED"

client = Client(account_sid, account_auth)
try:
    message = client.messages.create(
        to="+919080396132",
        from_=acc_no,
        body=f"{change_percentage}({stock_price_change}) \n {news_title1} , {news_title2} , {news_title3}"
    )
except NameError:
    message = client.messages.create(
        to="+919080396132",
        from_=acc_no,
        body=f"{change_percentage}({stock_price_change} , No new news articles "
    )
print(message.sid)
