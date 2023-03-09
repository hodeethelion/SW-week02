# 에러: 차이가 잘못 담김. for문 범위

def bs_search(arr, low, high):
    mid = (low + high)//2
    
    total = 0
    while low <= high:
        for i in arr:
            if i >= mid:
                total += i - mid  # 잘려나간 remain
    
        if total >= m:
            low = mid + 1
        else:
            high = mid - 1

    print(high)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
low, high = 1, max(arr)    # binary_S 검색범위

bs_search(arr, low, high)