#Imports time and date
import datetime
#axrhsimopoihto akomh
import random
#Oi dyo grammes apo katw einai gia na pernw weather report mesw API
from urllib.request import Request, urlopen
import json
from time import gmtime, strftime
#Oi dyo grammes apo katw einai gia na ginei to update/upgrade
import os
from subprocess import STDOUT, check_call
# internet connection module
import socket


quotes = {"You can't blame gravity for falling in love. Albert Einstein":1,
"Look deep into nature, and then you will understand everything better. Albert Einstein":2,
"Insanity: doing the same thing over and over again and expecting different results. Albert Einstein":3,
"Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop questioning. Albert Einstein":4,
"Peace cannot be kept by force; it can only be achieved by understanding. Albert Einstein":5,
"We cannot solve our problems with the same thinking we used when we created them. Albert Einstein":6,
"Try not to become a man of success, but rather try to become a man of value. Albert Einstein":7,
"The true sign of intelligence is not knowledge but imagination. Albert Einstein":8,
"Once we accept our limits, we go beyond them. Albert Einstein":9,
"The true sign of intelligence is not knowledge but imagination. Albert Einstein":10
}
def series():
    print ("""
        SERIES :

        1. The Walking Dead
        2. Fear The Walking Dead
        3. Once Upon A Time
        4. Strain
        5. Stranger Things
        6. Mr. Robot
        7. Game Of Thrones
        8. Grimm
        9. Back
        """)
#Internet check function
def internet(host="8.8.8.8", port = 53, timeout = 3):
    """
    Host : 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort : 53/tcp
    Service : domain (DNS/TCP)
    """
    print ("Checking Internet Connection")
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return "Internet is connected"
    except:
        return ("Internet Connection Failed")


#getting weather report with API (use your API from wunderground.com at API_KEY)
def weather():
    API_KEY = '953347195d82c160'
    url = 'http://api.wunderground.com/api/953347195d82c160/geolookup/conditions/astronomy/forecast/q/autoip.json'.format(API_KEY)

    request = Request(url)
    response = urlopen(request)
    json_string = response.read().decode('utf8')
    parsed_json = json.loads(json_string)
    #variables...h seira tou pws grafetai vrisketai sto site wunderground.com
    #location = place you live
    location = parsed_json['location']['city']
    #temperature and feel like in celcious
    temp_f = parsed_json['current_observation']['temp_c']
    feel = parsed_json['current_observation']['feelslike_c']
    #moon feedback
    moon_percent = parsed_json['moon_phase']['percentIlluminated']
    age_of_moon = parsed_json['moon_phase']['ageOfMoon']
    #general weather info
    weather_cur = parsed_json['current_observation']['weather']
    #forecast for 6 days
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
   
prompt = ">"   
now = datetime.datetime.now()
current_time = strftime("%Y-%m-%d %H:%M:%S")
print (current_time)
print("")
if now.hour <= 12:
    print ("Good Morning")
    print ("Is coffee ready yet?")
else:
    print ("Hello there")
    print ("If you had coffee then maybe you have to think about what you'll cook today!")
print ("")
print (random.choice(list(quotes.keys())))
print ("")
print ("")
#Gives weather info
print("Want to know about the weather? (y/n)")
answer = input(prompt)
print ("")
print (internet())
print ("")
while answer == 'y' or 'n':
    if answer == 'y':
        print (weather())
        break
    elif answer == 'n':
        print ("OK!!")
        break
    else:
        answer = input("'y' or 'n' please :D :")
#Update/dist-upgrade and autoremove with user input
print ("Do you want to update?")
update_ans = input(prompt)
print ("")
print (internet())
print ("")
while update_ans == 'y' or 'n':
    if update_ans == 'y':
        check_call(['apt-get', 'update'], stderr = STDOUT)
        check_call(['apt-get', 'dist-upgrade', '-y'], stderr = STDOUT)
        check_call(['apt', 'autoremove', '-y'], stderr = STDOUT)
        break
    elif update_ans == 'n':
        print ("OK!!")
        break
    else:
        update_ans = input("'y' or 'n' please :D :")
