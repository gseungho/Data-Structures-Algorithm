# 리스트 L에서 k번째로 작은 원소를 찾는 퀵 셀렉트 알고리즘

'''
1. 기준 원소(pivot)를 선택(random, 첫 번째, 마지막 등)
2. 리스트를 pivot보다 작은(A), 큰(B), 같은(M) 원소들로 분할 (n-1번 비교)
3. if |A| >= k: k번째 원소는 A에 있음 -> A에서 재귀 호출
   elif |A| + |M| < k: k번째 원소는 B에 있음 -> B에서 재귀 호출 (k - |A| - |M|)
   else: pivot이 k번째 원소임 -> pivot 반환
'''

def quick_select(lst, k):
    if len(lst) == 0 or k < 1 or k > len(lst):
        return None  # 잘못된 입력 처리
    pivot = lst[0]  # 첫 번째 원소를 기준 원소로 선택
    A = []
    B = []
    M = []
    for x in lst:
        if x < pivot:
            A.append(x)
        elif x > pivot:
            B.append(x)
        else:
            M.append(x)
    if len(A) >= k:
        return quick_select(A, k)
    elif len(A) + len(M) < k:
        return quick_select(B, k - len(A) - len(M))
    else:
        return pivot

# 테스트
print(quick_select([3, 6, 2, 7, 5, 1, 4], 3))  # Output: 3
print(quick_select([10, 20, 15, 25, 5], 4))  # Output: 20
print(quick_select([1, 2, 3, 4, 5], 1))  # Output: 1
print(quick_select([1, 2, 3, 4, 5], 5))  # Output: 5

# best case: O(n) (절반씩 분할 시)
# worst case: O(n^2) (편향 분할 시)
# average case: O(n)