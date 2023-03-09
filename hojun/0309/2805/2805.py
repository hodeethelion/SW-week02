import sys
import math
num_tree, desti = map(int, sys.stdin.readline().split())
#tree data만들기
tree_list = list(map(int, sys.stdin.readline().split()))
tree_list.sort()
tree_list = tree_list[::-1]
# print("tree list: " , tree_list)

# standard_index = 0

for i in range(1,len(tree_list)):
    total = 0 
    for k in range(i):
        total += tree_list[k] - tree_list[i]    
    print("standard tree : ", tree_list[i])
    print("total : ", total)
    if total > tree_list[i]:
        standard_index = i
        break
print("standard_index   :   ",standard_index)

# calculating the exact one
meaningful_tree = tree_list[:standard_index+1]
print("meaningful tree: ",meaningful_tree)
need = total - desti 
print("need   :   ", need)
#search for the one

for_need = math.ceil(need // standard_index)
print("for need : " , for_need)
print(meaningful_tree[-1] + for_need)