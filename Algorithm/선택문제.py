# 입력: n개의 값
# 출력: 최솟값 찾기

def find_min(lst):
    compare_cnt = 0
    if len(lst) == 1:
        compare_cnt += 1
        return lst[0], compare_cnt
    else:
        min = lst[0]
        for i in range(1, len(lst)):
            compare_cnt += 1
            if min > lst[i]:
                min = lst[i]
        return min, compare_cnt

def find_min_tonerment(lst):
    compare_cnt = 0
    if len(lst) == 1:
        compare_cnt += 1
        return lst[0], compare_cnt
    else:
        while len(lst) > 1:
            for i in range(0, len(lst)):
                if i + 1 < len(lst):
                    compare_cnt += 1
                    if lst[i] > lst[i + 1]:
                        lst.remove(lst[i])
                    else:
                        lst.remove(lst[i + 1]) 
        return lst[0], compare_cnt

# 테스트
print(find_min([3, 1, 4, 7, 8, 9, 2, 6, 5]))  # Output: (1, 8)
print(find_min_tonerment([3, 1, 4, 7, 8, 9, 2, 6, 5]))  # Output: (1, 12)
# 두 함수 모두 n - 1번의 비교를 수행

# 입력: n개의 값
# 출력: 최솟값과 최솟값 찾기

def find_min_max(lst):
    compare_cnt = 0
    if len(lst) < 2:
        return None, None, compare_cnt
    elif len(lst) == 2:
        compare_cnt += 1
        if lst[0] < lst[1]:
            return lst[0], lst[1], compare_cnt
        else:
            return lst[1], lst[0], compare_cnt
    else:
        min = lst[0]
        for i in range(1, len(lst)):
            compare_cnt += 1
            if min > lst[i]:
                min = lst[i]
        lst.remove(min)
        max = lst[0]
        for i in range(1, len(lst)):
            if lst[i] != min:
                compare_cnt += 1
            if max < lst[i]:
                max = lst[i]
        return min, max, compare_cnt    
    
def find_min_max_tonerment(lst):
    compare_cnt = 0
    if len(lst) < 2:
        return None, None, compare_cnt
    elif len(lst) == 2:
        compare_cnt += 1
        if lst[0] < lst[1]:
            return lst[0], lst[1], compare_cnt
        else:
            return lst[1], lst[0], compare_cnt
    else:
        round1_losers = []
        num = len(lst)
        if num % 2 == 1:
            round1_losers.append(lst[-1])
        while len(lst) > 1:
            for i in range(0, len(lst)):
                if i + 1 < len(lst):
                    compare_cnt += 1
                    if lst[i] > lst[i + 1]:
                        if len(round1_losers) < num // 2:
                            round1_losers.append(lst[i])
                        lst.remove(lst[i])
                    else:
                        if len(round1_losers) < num // 2:
                            round1_losers.append(lst[i + 1])
                        lst.remove(lst[i + 1])
        while len(round1_losers) > 1:
            for i in range(0, len(round1_losers)):
                if i + 1 < len(round1_losers):
                    compare_cnt += 1
                    if round1_losers[i] < round1_losers[i + 1]:
                        round1_losers.remove(round1_losers[i])
                    else:
                        round1_losers.remove(round1_losers[i + 1])
    return lst[0], round1_losers[0], compare_cnt
       
# 테스트
print(find_min_max([3, 1, 4, 7, 8, 9, 2, 6, 5]))  # Output: (1, 9, 15)
print(find_min_max_tonerment([3, 1, 4, 7, 8, 9, 2, 6, 5]))  # Output: (1, 9, 11)
# 첫 번째 함수는 2n - 3 번의 비교를 수행
# 두 번째 함수는 약 3n/2 - 2 번의 비교를 수행

# 입력: n개의 값
# 출력: 최솟값과 2번째 최솟값 찾기

def find_min_second_min(lst):
    compare_cnt = 0
    if len(lst) < 2:
        return None, None, compare_cnt
    elif len(lst) == 2:
        compare_cnt += 1
        if lst[0] < lst[1]:
            return lst[0], lst[1], compare_cnt
        else:
            return lst[1], lst[0], compare_cnt
    else:
        min = lst[0]
        for i in range(1, len(lst)):
            compare_cnt += 1
            if min > lst[i]:
                min = lst[i]
        lst.remove(min)
        second_min = lst[0]
        for i in range(1, len(lst)):
            if lst[i] != min:
                compare_cnt += 1
                if second_min > lst[i]:
                    second_min = lst[i]
        return min, second_min, compare_cnt
    
def find_min_second_min_tonerment(lst):
    compare_cnt = 0
    if len(lst) < 2:
        return None, None, compare_cnt
    elif len(lst) == 2:
        compare_cnt += 1
        if lst[0] < lst[1]:
            return lst[0], lst[1], compare_cnt
        else:
            return lst[1], lst[0], compare_cnt
    else:
        temp = lst.copy()
        while len(lst) > 1:
            for i in range(0, len(lst)):
                if i + 1 < len(lst):
                    compare_cnt += 1
                    if lst[i] > lst[i + 1]:
                        lst.remove(lst[i])
                    else:
                        lst.remove(lst[i + 1])
        min = lst[0]
        losers_of_min = []
        while len(temp) > 1:
            for i in range(0, len(temp)):
                if i + 1 < len(temp):
                    if temp[i] > temp[i + 1]:
                        if temp[i + 1] == min:
                            losers_of_min.append(temp[i])
                        temp.remove(temp[i])
                    else:
                        if temp[i] == min:
                            losers_of_min.append(temp[i + 1])
                        temp.remove(temp[i + 1])
        while len(losers_of_min) > 1:
            for i in range(0, len(losers_of_min)):
                if i + 1 < len(losers_of_min):
                    compare_cnt += 1
                    if losers_of_min[i] > losers_of_min[i + 1]:
                        losers_of_min.remove(losers_of_min[i])
                    else:
                        losers_of_min.remove(losers_of_min[i + 1])
        return min, losers_of_min[0], compare_cnt
    
# 테스트
print(find_min_second_min([3, 1, 4, 7, 8, 9, 2, 6, 5]))  # Output: (1, 2, 17)
print(find_min_second_min_tonerment([3, 1, 4, 7, 8, 9, 2, 6, 5]))  # Output: (1, 2, 11)
# 첫 번째 함수는 2n - 3 번의 비교를 수행
# 두 번째 함수는 n + log2(n)(정수 올림) - 2 번의 비교를 수행

# 입력: n개의 값과 k(1<=k<=n) 값
# 출력: k번째로 작은 입력 값
# 목표: 비교 횟수 최소화

