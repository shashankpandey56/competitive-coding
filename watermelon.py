weight = int(input())
def partition(weight):
    if weight % 2 == 0 and weight !=2:
        return "YES"
    else:
        return "NO"
print(partition(weight))