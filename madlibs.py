# string concatenation (akka how to put strings together)
# # suppose we want to create a string that says "subscribe to ____ "
# youtuber = "Manny Ventura" # some string variable

# # a few ways...
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
place = input("Make a name for a place: ")
number = input("Number : ")


madlib = f"My time on earth is absolutely {adj}! All i want to do is {verb1} \n\
    and {verb2} because I miss my home planet. Back home in the land of {place}, \n\
    we had {noun1}'s running around all the time. Not only that, but some {noun2}'s \n\
    even got along with the them! It was a crazy time, and I want to go back... \n\
    I just... I miss my kids man. \n\
    I wasn't there for them like I should have. Heck, LOOK WHERE I AM NOW. \n\
    Its a scary feeling not being sure if I ever will be a good dad man, or ever was. \n\
    Its not like wanting to be is enough. And its not fair to try and explain \n\
    The hardships I go through to be there for them. There kids you know? \n\
    Im supposed to not make it seem so scary, but what's scary is that \n\
    They probably learned that life is scary and sometimes those that \n\
    want to be there for them wont. Tough as nails, but it breaks my heart, \n\
    cause its not fair to them. They should not have to tough BECAUSE of me. \n\
    I hope at least they know I do love them, and that I am just a bad father \n\
    I owe them at least that. Love all {number} of ya, \n\
    \n\
    Pops"
print(madlib)