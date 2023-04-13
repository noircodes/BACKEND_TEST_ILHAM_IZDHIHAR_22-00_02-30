#1 String Slicing
text = "Dewangga"
slicing = text[:3]
print(slicing)

#2 String concat
kota1 = "Semarang"
kota2 = "Solo"
kota3 = "Jogjakarta"
negara = "Indonesia"
print(kota1 + " " + kota2 + " " + kota3 + " " + negara)

#3 Finding Array
Himpunan = [85,76,11,99,18]
x = 86
find = x in Himpunan
print(find)

#4 Dictionary/Object
person = {
    "name": "Ilham Izdhihar",
    "age": 24,
    "address": {
        "street": "Tegalrejo",
        "city": "Salatiga",
        "province": "Jawa Tengah"
    },
    "hobbies": ["playing game", "watch movie", "surfing internet"]
}
print(person)

#5 Logical Operator
a = 10
b = 15
c = 4
if a > b and a > c:
    print("nilai a paling besar dibanding yang lain")
elif b > a and b > c:
    print("nilai b paling besar dibanding yang lain")
else:
    print("nilai c paling besar dibanding yang lain")