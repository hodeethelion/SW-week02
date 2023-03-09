import sys
import math
num_tree, desti = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))
tree_list.sort()
tree_list = tree_list[::-1]
for i in range(1,len(tree_list)):
    total = 0 
    for k in range(i):
        total += tree_list[k] - tree_list[i]    
    if total > tree_list[i]:
        standard_index = i
        break
meaningful_tree = tree_list[:standard_index+1]
need = total - desti 
for_need = math.ceil(need // standard_index)
print(meaningful_tree[-1] + for_need)