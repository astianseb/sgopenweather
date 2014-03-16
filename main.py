import openweatherapi as owapi

is_running = True
print "Wpisanie \"stop\" konczy poszukiwania"
while True:
    location = str(raw_input("Podaj lokalizacje: "))
    if location ==  "stop":
        break
    else:
        weather = owapi.Weather(location)
        response = weather.get_response()
        
        if weather.is_response_valid(response):
            print weather.get_location()
            print ("Pogoda dla lokalizacji: %s" ) % location
            print ("Temperatura: %s C") % weather.get_temperature()
            print "Wilgotnosc: ", weather.get_humidity()
            print "Cisnienie: ", weather.get_pressure()
        else:
            print "Zla lokalizacja"
    
