# 1부터 n까지의 합
def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

# 테스트
print(sum_recursive(5))  # Output: 15
print(sum_recursive(10)) # Output: 55

# a 부터 b까지의 합
def sum_range_recursive(a, b):
    if a == b:
        return a
    elif a > b:
        return 0
    else:
        return a + sum_range_recursive(a + 1, b)
    
# 테스트
print(sum_range_recursive(3, 7))  # Output: 25
print(sum_range_recursive(5, 5))  # Output: 5

# 리스트 reverse 시키기
def reverse_list_recursive(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_list_recursive(lst[:-1])
    
# 테스트
print(reverse_list_recursive([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
print(reverse_list_recursive(['a', 'b', 'c']))   # Output: ['c', 'b', 'a']

# 리스트 start 부터 stop 까지 reverse 시키기
def reverse_sublist_recursive(lst, start, stop):
    if start >= stop:
        return lst
    lst[start], lst[stop] = lst[stop], lst[start]
    return reverse_sublist_recursive(lst, start + 1, stop - 1)

# 테스트
print(reverse_sublist_recursive([1, 2, 3, 4, 5], 1, 3))  # Output: [1, 4, 3, 2, 5]
print(reverse_sublist_recursive(['a', 'b', 'c', 'd'], 0, 2))   # Output: ['c', 'b', 'a', 'd']
