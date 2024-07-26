name = str(input("Введите название файла: "))
n = int(input("Введите число N: "))

with open(name, 'w+') as func:
    a = 1
    for i in range(n):
        func.write(str(a) + "\n")
        a = a + 1
func.close()

with open(name, 'r') as func:
    data = func.read()
print(data)
func.close()
