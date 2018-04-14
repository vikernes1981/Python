

from urllib.request import Request, urlopen
import json

API_KEY = '953347195d82c160'
url = 'http://api.wunderground.com/api/953347195d82c160/geolookup/conditions/astronomy/forecast/q/autoip.json'.format(API_KEY)

request = Request(url)
response = urlopen(request)
json_string = response.read().decode('utf8')
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
# gia kapoio logo prepei na vazw mprosta to current_observation kai meta otidipote allo
temp_f = parsed_json['current_observation']['temp_c']
feel = parsed_json['current_observation']['feelslike_c']
moon_percent = parsed_json['moon_phase']['percentIlluminated']
age_of_moon = parsed_json['moon_phase']['ageOfMoon']
weather_cur = parsed_json['current_observation']['weather']
tomorrow_day = parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext_metric']
day_after_tomorrow = parsed_json['forecast']['txt_forecast']['forecastday'][1]['fcttext_metric']
third_day = parsed_json['forecast']['txt_forecast']['forecastday'][2]['fcttext_metric']
fourth_day = parsed_json['forecast']['txt_forecast']['forecastday'][3]['fcttext_metric']
fifth_day = parsed_json['forecast']['txt_forecast']['forecastday'][4]['fcttext_metric']
sixth_day = parsed_json['forecast']['txt_forecast']['forecastday'][5]['fcttext_metric']
print("Current temperature in %s is: %s but it feels like %s" % (location, temp_f, feel))
print ("Moon is :\n%s%% Illuminated and is :\n%s days old" % (moon_percent, age_of_moon))
print ("Weather today is going to be : %s " % weather_cur)
print ("Tomorrow :\n %s " % tomorrow_day)
print ("Day after tomorrow :\n %s " % day_after_tomorrow)
print ("Third day :\n %s " % third_day)
print ("Fourth day :\n %s " % fourth_day)
print ("Fifth day :\n %s " % fifth_day)
print ("Sixth day :\n %s " % sixth_day)
response.close()
