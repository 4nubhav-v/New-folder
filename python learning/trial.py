dictionary = {}
cond = "true"
while cond == "true":
    name = input("Enter your name :- ")
    grade = input("Enter your grade :- ")
    dictionary[name] = grade
    cond = (input("Enter 'True' to continue or 'False' to stop :- ")).lower()
print(dictionary)
