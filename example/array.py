arr = list()
n = int(input("Enter number of elements: "))
print("Enter elements:")
i = 0
if (n > 15):
    print("error")
while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1
print("Array:")
i = 0
for i in range(n):
    print(arr[i], end = " ")
print("")
