
print("Name: Navdeep    Student_id: 21582009")

def reverse(name):
    if len(name) == 0:
        return name
    else:
        return reverse(name[1:]) + name[0]

string = str(input("Enter your name: "))
print(reverse(string))

