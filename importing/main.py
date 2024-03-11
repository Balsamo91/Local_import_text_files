import things

print(things.THIS_IS_CONST)

user_name = input("What's your name?: ")
things.greetings(user_name)

person = things.Person("Adam", 34)

person.greet()