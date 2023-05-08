list = [int(num) for num in input("Enter numbers: ").split(" ")]
list = sorted(list)

tuples = []

l = list[0]
r = list[0]

for i in range(len(list)-1):
    if(list[i]+1 == list[i+1]):
        r+=1
    else:
        tuples.append((l,r))
        l = list[i+1]
        r = list[i+1]

tuples.append((l, r))

print(tuples)

