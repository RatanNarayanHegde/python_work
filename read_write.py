import json
filename = 'username.json'
try:
    with open(filename) as file:
        username = json.load(file)
except:
    username = input("Enter your username ")
    with open(filename,'w') as file:
        json.dump(username,file)
    print("We'll Remember you next time!")
else:
    print("Welcome "+username+" to the game")   