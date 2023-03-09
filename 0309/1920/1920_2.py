import sys
def binary_search(list, target):
    mid = len(list)//2
    if len(list) == 1 and target == list[0]:
        return 1
    elif len(list) == 1 and target != list[0]:
        return 0
    if len(list) == 0:
        return 0
    
    medium = len(list) //2 
    if target == list[medium]:
        return 1
    else:
        if target > list[medium]:
            return binary_search(list[medium:], target)
        else:
            return binary_search(list[:medium], target)
num_num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_cake = int(sys.stdin.readline())
num_stand = list(map(int, sys.stdin.readline().split()))    

num_list.sort()
for item in num_stand:
    print(binary_search(num_list, item))