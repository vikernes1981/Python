#! /usr/bin/env python3


#import feedparser
#Imports time and date
import datetime
#Just to get random quotes/recipes/survival tips
import random
#Following 2 lines are for weather report through API
import urllib #request import Request, urlopen
import json
from time import gmtime, strftime
#Following 2 lines are for update/upgrade DEBIAN LINUX ONLY
import os
from subprocess import STDOUT, check_call
# internet connection module
import socket
import webbrowser

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
#the options we want to take are writen in the link
# Example : geolookup/conditions/astronomy...
def weather():
    API_KEY = '953347195d82c160'
    url = 'http://api.wunderground.com/api/953347195d82c160/geolookup/conditions/astronomy/forecast/q/Germany/Rostock.json'.format(API_KEY)

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

#output of weather
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

#main menu with series submenu
def main_menu():
    def series():
        series_ans = True
        while series_ans:
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

            series_ans = input("What would you like to do? : ")
            if series_ans == '1':
                url = 'http://xrysoi.se/the-walking-dead-2010/'
                webbrowser.open_new_tab(url)
            elif series_ans == '2':
                url = 'http://xrysoi.se/fear-the-walking-dead-2015/'
                webbrowser.open_new_tab(url)
            elif series_ans == '3':
                url = 'http://xrysoi.se/once-upon-a-time-2011/'
                webbrowser.open_new_tab(url)
            elif series_ans == '4':
                url = 'http://xrysoi.se/strain-2014/'
                webbrowser.open_new_tab(url)    
            elif series_ans == '5':
                url = 'http://xrysoi.se/stranger-things-2016/'
                webbrowser.open_new_tab(url)
            elif series_ans == '6':
                url = 'http://xrysoi.se/mr-robot-2015/'
                webbrowser.open_new_tab(url)
            elif series_ans == '7':
                url = 'http://xrysoi.se/game-of-thrones-tv-series-2011/'
                webbrowser.open_new_tab(url)
            elif series_ans == '8':
                url = 'http://xrysoi.se/grimm-tv-series-2011/'
                webbrowser.open_new_tab(url)
            elif series_ans == '9':
                break
                print (main_menu())
            else:
                series_ans = input("Select an option please :")
                break
                


    ans = True
    while ans:
        print ("""
        1. Update/Upgrade
        2. Weather
        3. Start Coding
        4. Series
        5. Character Creation
        6. Exit/Quit 
        """)

        ans = input("What would you like to do? : ")
        if ans == '1':
            check_call(['sudo', 'apt-get', 'update'], stderr = STDOUT)
            check_call(['sudo', 'apt-get', 'dist-upgrade', '-y'], stderr = STDOUT)
            check_call(['sudo', 'apt-get', 'autoremove', '-y'], stderr = STDOUT)
        elif ans == '2':
            print (weather())
        elif ans == '3':
            check_call(['code', '--user-data-dir="~/.vsc0de-r00t"'], stderr = STDOUT) uncomment this line
            # depending on terminal insert command
            #check_call(['terminator'], stderr = STDOUT)
        elif ans == '4':
            print (series())
        elif ans == '6':
            print ("\n Bye!")
            break
        else:
            ans = input("Select an option please :")
            break



now = datetime.datetime.now()
current_time = strftime("%Y-%m-%d %H:%M:%S")
print (current_time)
print("")
if now.hour <= 12:
    print ("Good Morning!")
    print ("Is coffee ready yet?")
else:
    print ("Hello there!")
    print ("If you had coffee then maybe you have to think about what you'll cook today!")
print ("")
print ("Suggestion :")
print (random.choice(list(open('syntages.txt'))))
print(random.choice(list(open('quotes.txt'))))
print ("")
print ("")
print (internet())
print ("")
print ("")
print ("Please select an option")

print (main_menu())
