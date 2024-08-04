num = int(input("Número: "))

a, b = 0, 1

for _ in range(num):
    print(a, end=" - ")
    temp = a + b
    a = b
    b = temp

print("Fim")
