def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return 1
    if len(data) == 1 and search != data[0]:
        return 0
    if len(data) == 0:
        return 0
        
    medium = len(data) // 2
    if search == data[medium]:
        return 1
    else:
        if search > data[medium]:
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)
import sys
num_num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_cake = int(sys.stdin.readline())
num_stand = list(map(int, sys.stdin.readline().split()))
num_list.sort()
for item in num_stand:
    print(binary_search(num_list, item))
    # print(num_list,"in",item )