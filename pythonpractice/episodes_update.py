import webbrowser
import datetime

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
        3. EVE
        4. Rootchk
        5. Horrorscope
        6. Recipes
        7. Install Software
        8. Start Coding
        9. Series
        10.Character Creation
        11.Exit/Quit 
        """)

        ans = input("What would you like to do? : ")
        if ans == '1':
            check_call(['apt-get', 'update'], stderr = STDOUT)
            check_call(['apt-get', 'dist-upgrade', '-y'], stderr = STDOUT)
            check_call(['apt', 'autoremove', '-y'], stderr = STDOUT)
        elif ans == '2':
            print (weather())
        elif ans == '9':
            print (series())
        elif ans == '11':
            print ("\n Bye!")
            break
        else:
            ans = input("Select an option please :")
            break


saved_data = 'TWD_last_ep.txt'
f = open(saved_data, "r")
print(f.read())
f.close()
series_ep = input("What was the last episode you watched? : ")
if series_ep == "":
    print ("Bye")
else:
    file = open("TWD_last_ep.txt", "w")
    file.write("Last episode you watched was " + series_ep + "\n")
    file.close()
print (main_menu())