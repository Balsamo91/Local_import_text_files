# Can be done like this on multiple line
from things import Person
from things import greetings

# Can be done in a single line
from things import Person, THIS_IS_CONST

# To import a file/module that is in a folder
### from <folder>.<file> import <name os what you need to import>


person = Person("Julia", 27)

person.greet()

print(THIS_IS_CONST)



