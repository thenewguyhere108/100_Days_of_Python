import requests
import datetime


url = "https://pixe.la/v1/users/thenewguyhere108/graphs/newgraph/"
today = datetime.date.today()

kilo = input("How many kilos did you lift today ? :")
parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": kilo
}
header = {"X-USER-TOKEN": "REDACTED"}

my_req = requests.post(url=url, headers=header, json=parameters)
print(my_req.text)
