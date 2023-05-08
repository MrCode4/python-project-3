
def find_evens(list, index, evens):
    if(index >= len(list)):
        return 
    if(list[index] % 2 == 0):
        evens.append(list[index])

    find_evens(list, index+1, evens)

def find_odds(list, index, odds):
    if(index >= len(list)):
        return 
    if(list[index] % 2 != 0):
        odds.append(list[index])

    find_odds(list, index+1, odds)

list = [int(num) for num in input("Enter numbers: ").split(" ")]

evens = []
odds = []

find_evens(list, 0, evens)
find_odds(list, 0, odds)

print("Even list are: ", sep ="")
print(evens)

print("Odd list are: ", sep="")
print(odds)

