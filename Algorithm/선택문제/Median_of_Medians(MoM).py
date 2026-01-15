# 리스트 L에서 k번째로 작은 원소를 찾는 MoM 알고리즘

'''
1. 리스트를 5개씩 그룹으로 나눔 (n/5 그룹)
2. 각 그룹의 중앙값을 구함 (정렬 후 가운데 원소 선택)
3. 중앙값들의 리스트에서 다시 MoM 알고리즘으로 중앙값(median of medians)을 구함
4. 리스트를 pivot(median of medians)보다 작은(A), 큰(B), 같은(M) 원소들로 분할 (n-1번 비교)
5. if |A| >= k: k번째 원소는 A에 있음 -> A
    elif |A| + |M| < k: k번째 원소는 B에 있음 -> B에서 재귀 호출 (k - |A| - |M|)
    else: pivot이 k번째 원소임 -> pivot 반환
'''

def median_of_medians(lst, k):
    if len(lst) == 0 or k < 1 or k > len(lst):
        return None  # 잘못된 입력 처리
    # 1. 리스트를 5개씩 그룹으로 나누기
    groups = [lst[i:i + 5] for i in range(0, len(lst), 5)]
    # 2. 각 그룹의 중앙값 구하기
    medians = []
    for group in groups:
        group.sort()
        medians.append(group[len(group) // 2])
    # 3. 중앙값들의 리스트에서 MoM으로 중앙값 구하기
    if len(medians) <= 5:
        medians.sort()
        pivot = medians[len(medians) // 2]
    else:
        pivot = median_of_medians(medians, len(medians) // 2 + 1)
    # 4. 리스트를 pivot보다 작은(A), 큰(B), 같은(M) 원소들로 분할
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
    # 5. k번째 원소 찾기
    if len(A) >= k:
        return median_of_medians(A, k)
    elif len(A) + len(M) < k:
        return median_of_medians(B, k - len(A) - len(M))
    else:
        return pivot
    
# 테스트
print(median_of_medians([3, 6, 2, 7, 5, 1, 4], 3))  # Output: 3
print(median_of_medians([10, 20, 15, 25, 5], 4))  # Output: 20
print(median_of_medians([1, 2, 3, 4, 5], 1))  # Output: 1
print(median_of_medians([1, 2, 3, 4, 5], 5))  # Output: 5

# best case: O(n) (절반씩 분할 시)
# worst case: O(n) (균형 잡힌 분할 시)
# average case: O(n)

'''
점화식: T(n) = T(3n/4) + T(n/5) + 11n/5, T(1) = 1
귀납법을 통해 T(n) <= 44n임을 증명할 수 있음
'''