import sys
num_num = int(sys.stdin.readline())
num_list = set(map(int, sys.stdin.readline().split()))
num_cake = int(sys.stdin.readline())
num_stand = list(map(int, sys.stdin.readline().split()))

for item in num_stand:

    if item in num_list:
        # print("item is", item)
        # print("num_list", num_list)
        print(1)
    else:
        print(0)