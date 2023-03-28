import requests
import datetime
import os

data = input("Aby sprawdzić opady deszczu w Olsztynie:\n"
             "Podaj datę lub naciśnij enter (Wymagany format YYYY-MM-DD): ")

url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_" \
      "sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

longitude = 20.490189
latitude = 53.770226

if data:
    try:
        searched_date = datetime.datetime.strptime(data, "%Y-%m-%d").date()
    except:
        print("Podano złą datę.")
        searched_date = datetime.date.today() + datetime.timedelta(days=1)
else:
    searched_date = datetime.date.today() + datetime.timedelta(days=1)

print(f"Wybrana data: {searched_date}")

if not os.path.exists('opady.txt'):
    with open('opady.txt', 'w'):
        pass

with open("opady.txt", 'r') as f:
    odczyt = f.readlines()

for line in odczyt:
    if line.split()[0] == str(searched_date):
        suma_opadow = float(line.split()[1])

else:
    resp = requests.get(url.format(latitude=latitude, longitude=longitude, searched_date=searched_date)).\
        json()
    suma_opadow = resp['daily']['rain_sum']
    with open("opady.txt", 'a') as f:
        f.write(str(searched_date) + " " + str(suma_opadow[0]) + "\n")

if suma_opadow[0] == 0:
    print("Nie będzie padać.")
elif suma_opadow[0] > 0:
    print("Będzie padać.")
else:
    print("Nie wiem.")


