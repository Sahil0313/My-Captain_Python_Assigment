a = list(map(int,input("\nEnter the numbers : ").strip().split()))
z = []
for i in a:
    if i>=0:
        z.append(i)
print(z)
