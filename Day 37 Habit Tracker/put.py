import requests
import datetime

today = datetime.date.today()
url = f"https://pixe.la/v1/users/thenewguyhere108/graphs/newgraph/{today.strftime("%Y%m%d")}"

kilo = input("How many kilos did you lift today ? :")
parameters = {
    "quantity": kilo
}
header = {"X-USER-TOKEN": "REDACTED"}

my_req = requests.put(url=url, headers=header, json=parameters)
print(my_req.text)
