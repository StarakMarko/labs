n = int(input("input n "))
m = int(input("input m "))

A = []
B = []
result = []

print("enter n elements of A")
for _ in range(n):
    element = input()
    A.append(element)
print("enter m elements of B")

for _ in range(m):
    element = input()
    B.append(element)

for element_a in A:
    for element_b in B:
        if element_a == element_b and element_a not in result:
            result.append(element_a)


len_result = len(result)


print(len_result)
