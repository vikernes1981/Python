prompt = ">"   
now = datetime.datetime.now()
current_time = strftime("%Y-%m-%d %H:%M:%S")
print (current_time)
print("")
print("Want to know about the weather? (y/n)")
answer = input(prompt)
if answer == 'y':
    return weather()
elif answer == 'n':
    print ("OK!!")
else:
    print ("'y' or 'n' please :D")
print ("")
if now.hour <= 12:
    print ("Good Morning")
    print ("Is coffee ready yet?")
else:
    print ("Hello there")
    print ("If you had coffee then maybe you have to think about what you'll cook today!")