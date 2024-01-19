import requests

url = "http://localhost:3000"

payload = {}
files=[
  ('file',('NIFTY 50-19-12-2023-to-19-01-2024.csv',open('C:/Users/jayesh/Downloads/NIFTY 50-19-12-2023-to-19-01-2024.csv','rb'),'csv'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
