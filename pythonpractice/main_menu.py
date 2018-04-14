def main_menu():
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
        elif ans == '3':
            print ("\n Student Records")
        elif ans == '11':
            print ("\n Bye!")
            break
        else:
            ans = input("Select an option please :")