import requests
import datetime
import os


class WeatherForecast:

    def __init__(self):
        self.opady = {}
        with open("opady.txt", 'r') as f:
            odczyt = f.readlines()
            for record in odczyt:
                self.opady[record.split()[1].replace("\n", "")] = record.split()[0]

    def __repr__(self):
        return f'<Oto zapisane opady: {self.opady}>'

    def __getitem__(self, searched_date):

        suma_opadow = None

        url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=" \
              "rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
        longitude = 20.490189
        latitude = 53.770226

        with open("opady.txt", 'r') as f:
            odczyt = f.readlines()
            for line in odczyt:
                if line.split()[0] == str(searched_date):
                    if float(line.split()[1]) == 0:
                        print("Nie będzie padać.")
                    elif float(line.split()[1]) > 0:
                        print("Będzie padać.")
                else:
                    resp = requests.get(url.format(latitude=latitude, longitude=longitude, searched_date=searched_date)).json()
                    suma_opadow = resp['daily']['rain_sum']
                    if suma_opadow[0] == 0:
                        print("Nie będzie padać.")
                    elif suma_opadow[0] > 0:
                        print("Będzie padać.")
                    else:
                        print("Nie wiem.")
                    break

        if suma_opadow:
            with open("opady.txt", 'a') as f:
                f.write(str(searched_date) + " " + str(suma_opadow[0]) + "\n")

    def items(self):
        return self.opady

    def __iter__(self):
        return iter(self.opady)

if not os.path.exists('opady.txt'):
    with open('opady.txt', 'w'):
        pass

data = input("Aby sprawdzić opady deszczu w Olsztynie:\n"
             "Podaj datę lub naciśnij enter (Wymagany format YYYY-MM-DD): ")

if data:
    try:
        searched_date = datetime.datetime.strptime(data, "%Y-%m-%d").date()
    except:
        print("Podano złą datę.")
        searched_date = datetime.date.today() + datetime.timedelta(days=1)
else:
    searched_date = datetime.date.today() + datetime.timedelta(days=1)

print(f"Wybrana data: {searched_date}")

prognoza = WeatherForecast()

print(prognoza.items())

# prognoza_dzis = prognoza[searched_date]

# for record in prognoza():
#     print(record)




###########################################

#
# import requests
# import datetime
# import os
#
#
# class WeatherForecast:
#
#     def __init__(self):
#         self.opady = {}
#
#     def __getitem__(self, searched_date):
#
#         suma_opadow = None
#
#         url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=" \
#               "rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
#         longitude = 20.490189
#         latitude = 53.770226
#
#         with open("opady.txt", 'r') as f:
#             odczyt = f.readlines()
#             for line in odczyt:
#                 if line.split()[0] == str(searched_date):
#                     if float(line.split()[1]) == 0:
#                         print("Nie będzie padać.")
#                     elif float(line.split()[1]) > 0:
#                         print("Będzie padać.")
#                 else:
#                     resp = requests.get(url.format(latitude=latitude, longitude=longitude, searched_date=searched_date)).json()
#                     suma_opadow = resp['daily']['rain_sum']
#                     if suma_opadow[0] == 0:
#                         print("Nie będzie padać.")
#                     elif suma_opadow[0] > 0:
#                         print("Będzie padać.")
#                     else:
#                         print("Nie wiem.")
#                     break
#
#         if suma_opadow:
#             with open("opady.txt", 'a') as f:
#                 f.write(str(searched_date) + " " + str(suma_opadow[0]) + "\n")
#
#     def items(self):
#         return self.opady
#
#     def __iter__(self):
#         return iter(self.data)
#
# if not os.path.exists('opady.txt'):
#     with open('opady.txt', 'w'):
#         pass
#
# data = input("Aby sprawdzić opady deszczu w Olsztynie:\n"
#              "Podaj datę lub naciśnij enter (Wymagany format YYYY-MM-DD): ")
#
# if data:
#     try:
#         searched_date = datetime.datetime.strptime(data, "%Y-%m-%d").date()
#     except:
#         print("Podano złą datę.")
#         searched_date = datetime.date.today() + datetime.timedelta(days=1)
# else:
#     searched_date = datetime.date.today() + datetime.timedelta(days=1)
#
# print(f"Wybrana data: {searched_date}")
#
# prognoza = WeatherForecast()
#
# prognoza_dzis = prognoza[searched_date]