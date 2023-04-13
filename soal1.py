"""
1. Sample Framework Python : Django, Flask, FastAPI, Pyramid, CherryPy, Bottle, Tornado.
2. Install library di Python : Pastikan python sudah terinstall dengan baik, lalu jalankan "pip install [nama_library]"
"""

#3. Segitiga Bintang
def bintang_segitiga(n):
    for i in range(n):
        print("*"*(i+1))

bintang_segitiga(5)

#4. Mengecek Bilangan Prima
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(97))
print(is_prime(9))

#5. Menghitung huruf kapital dalam sebuah file
def count_capital_letters(file_path):

    with open(file_path, "r") as file:
        contents = file.read()
        capital_letters = [char for char in contents if char.isupper()]
        return len(capital_letters)

file_path = "test.txt"
capital_count = count_capital_letters(file_path)
print("Jumlah huruf kapital dalam file tersebut adalah " + str(capital_count))

#6 Algorithm Sorting
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr = ["1","4","0","6","9"]
print(arr)
sorted_array = bubble_sort(arr)
print(sorted_array)

#7 Usia Emas
def golden_age():
    name = input("Siapa nama anda? ")
    age = int(input("Berapa usia anda? "))
    golden = 50 - age
    print("Hai, "+ name +" anda akan berusia 50 tahun dalam "+ str(golden)+" tahun kedepan")
golden_age()
    
