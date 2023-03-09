import sys
import math
num_tree, desti = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))
if num_tree == 1:
    k = tree_list[0] - desti
    print(k)

elif sum(tree_list) - (min(tree_list)*len(tree_list)) < desti:
    need_all = desti -  (sum(tree_list) - (min(tree_list)*len(tree_list)) )
    # print("need_all ", need_all)
    need_one = math.ceil(need_all/len(tree_list))
    # print("yala")
    print(min(tree_list)- need_one)

else:
    tree_list.sort()
    tree_list = tree_list[::-1]
    for i in range(1,len(tree_list)):
        total = 0 
        for k in range(i):
            total += tree_list[k] - tree_list[i]    
            print(total)
        if total > tree_list[i]:
            standard_index = i
            print(standard_index)
            break
    meaningful_tree = tree_list[:standard_index+1]
    need = total - desti 
    for_need = math.ceil(need // standard_index)
    print(meaningful_tree[-1] + for_need)