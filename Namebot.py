m_name = input("Do you have a middle name? ").lower()
name = input("Enter your full name: ")
opt = int(input("Do you want your name on 2 lines (1) or your initials (2)? 1 or 2? "))
index = 0
char = "T"
if m_name == "no":
    while not char == " ":
        char = name[index]
        index = index + 1
    if opt == 1:
        print(name[0:index].capitalize())
        print(name[index:len(name)].capitalize())
    else:
        print("Hello", name[0].upper(), name[index:len(name)].capitalize())
else:
    while not char == " ":
        char = name[index]
        index = index + 1
    index2 = index+1
    char = "T"
    while not char == " ":
        char = name[index2]
        index2 = index2 + 1
    if opt == 1:
        print(name[0:index].capitalize())
        print(name[index:index2].capitalize())
        print(name[index2:len(name)].capitalize())
    else:
        print("Hello", name[0].upper(), name[index].capitalize(), name[index2:len(name)].capitalize())