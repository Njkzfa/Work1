arr = list()
n = int(input("Enter number of elements: "))
print("Enter elements:")
i = 0
while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1
print("Array:")
i = 0
for i in range(n):
    print(arr[i], end = " ")
print("")
