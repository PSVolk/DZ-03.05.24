start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for i in range(start, end + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()
