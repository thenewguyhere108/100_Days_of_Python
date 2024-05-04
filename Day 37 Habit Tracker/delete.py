import requests
import datetime

today = datetime.date.today()
url = f"https://pixe.la/v1/users/thenewguyhere108/graphs/newgraph/{today.strftime("%Y%m%d")}"

header = {"X-USER-TOKEN": "REDACTED"}

my_req = requests.delete(url=url, headers=header)
