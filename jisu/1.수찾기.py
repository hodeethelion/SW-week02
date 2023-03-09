# 기준 list 'A', 찾아볼 list 'arr'
N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

# low, high 두 변수를 이용해 lower/upper bounds range
def bineary_search(arr, x):         # arr에서 x 찾기
    low = 0
    high = N - 1
    isExist = False

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            isExist = True
            print(1)
            break
        elif arr[mid] < x:
            low = mid + 1       # 검색 대상 절반으로. 
        else: 
            high = mid - 1
            
    if not isExist:
        print(0)

for _ in arr:
    bineary_search(A, _)

# mid == x인 지점에서 print(1)을, while을 전부 돌았는데 break되지 않았다면 print(0)을 리턴하면 됨.
# bineary_search에서 찾아볼 원소 x는 arr에서 for문으로 가져와야 함. 

"""
기본 함수
# low, high 두 변수를 이용해 lower/upper bounds range

def bineary_search(arr, x):
    low = 0
    high = N - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1       # 검색 대상 half로.
        else: 
            high = mid - 1
            
    return -1                   # 검색 실패

"""




"""
재귀 이용한 Binary Search

def Binary_Search(self, x):
    if (tNode == None):
        return None
    elif (x == tNode.item):
        return tNode
    elif (x < tNode.item):
        return self.Binary_Search(tNode.left, x)
    else:
        return self.Binary_Search(tNode.right, x)

"""
