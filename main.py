# write your code here
person = {
    "name": "sarah",
    "age": "17",
    "hobbies":['drawing', 'singing', 'dancing', 'taking pics']
}
print(person["name"])
print(person["age"])

person["age"] = "20"
person["contry"]= "Kuwait"
print(person)
print(len(person))

person["hobbies"].append('shopping')
print(person)

def check_hobbies(person):
    if "hobbies" > "3":
        print("WOW YOU ARE AMAZING")
    else:
        print("get off your phone")
check_hobbies(person)

