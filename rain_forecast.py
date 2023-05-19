import requests
import datetime
import os

url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=" \
      "rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
longitude = 20.490189
latitude = 53.770226


class WeatherForecast:

    def __init__(self, searched_date):
        self.opady = {}
        self.searched_date = searched_date

        with open("opady.txt", 'r') as f:
            odczyt = f.readlines()
            for record in odczyt:
                self.opady[record.split()[0]] = record.split()[1].replace("\n", "")

        for line in odczyt:
            if line.split()[0] == str(self.searched_date):
                suma_opadow = float(line.split()[1])
                break
        else:
            resp = requests.get(url.format(latitude=latitude, longitude=longitude, searched_date=searched_date)). \
                json()
            suma_opadow = resp['daily']['rain_sum'][0]
            with open("opady.txt", 'a') as f:
                f.write( "\n" + str(self.searched_date) + " " + str(suma_opadow))

        self.opady[self.searched_date] = suma_opadow


    def __repr__(self):
        return f'<All the Rain Forecast data: {self.opady}>'

    def __setitem__(self, searched_date, opad):
        self.opady[searched_date] = opad

    def __getitem__(self, searched_date):
        return self.opady[searched_date]

    def __dict__(self):
        return self.opady
    def items(self):
        for d, o in self.opady.items():
            yield d, o

    def __iter__(self):
        return iter(self.opady)


if not os.path.exists('opady.txt'):
    with open('opady.txt', 'w'):
        pass

data = input("To check rainfall in Olsztyn, Poland :\n"
             "Enter a date or press enter to check for tomorrow (YYYY-MM-DD): ")

if data:
    try:
        searched_date = datetime.datetime.strptime(data, "%Y-%m-%d").date()
    except:
        print("Wrong date.")
        searched_date = datetime.date.today() + datetime.timedelta(days=1)
else:
    searched_date = datetime.date.today() + datetime.timedelta(days=1)


weather_forecast = WeatherForecast(searched_date)
print(f"Entered date: {searched_date}")

# print(weather_forecast.__dict__())
print(f'The total precipitation for {searched_date}: ', weather_forecast[searched_date], '[mm]')
# print()
# print(weather_forecast.items())
# print()

# print("\nDate printing:")
#
# for record in weather_forecast:
#     print(record)
#
# print("\nDrukowanie kluczy i wartości:")
# for a, b in weather_forecast.items():
#     print(a, b)
#
#
