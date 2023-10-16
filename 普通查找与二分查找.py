def sequential_search(target, nums):

    for i, v in enumerate(nums):
        if v == target:
            return i

    return None



def binary_search_rec(target, left, right, nums):

    if left <= right:
        
        mid = (left + right) // 2
        
        if target < mid:
            return binary_search_rec(target, left, mid - 1, nums)
        elif target > mid:
            return binary_search_rec(target, mid + 1, right, nums)
        else:
            return mid

    return None



def binary_search_loop(target, left, right, nums):

    while left <= right:

        mid = (left + right) // 2
        if target < mid:
            right = mid - 1
        elif target > mid:
            left = mid + 1
        else:
            return mid

    return None



if __name__ == '__main__':

    nums = list(range(50))

    for i in range(60):
        print(sequential_search(i, nums), end=' ')
        print(binary_search_rec(i, 0, len(nums)-1, nums), end=' ')
        print(binary_search_loop(i, 0, len(nums)-1, nums))

"""
0 0 0
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
8 8 8
9 9 9
10 10 10
11 11 11
12 12 12
13 13 13
14 14 14
15 15 15
16 16 16
17 17 17
18 18 18
19 19 19
20 20 20
21 21 21
22 22 22
23 23 23
24 24 24
25 25 25
26 26 26
27 27 27
28 28 28
29 29 29
30 30 30
31 31 31
32 32 32
33 33 33
34 34 34
35 35 35
36 36 36
37 37 37
38 38 38
39 39 39
40 40 40
41 41 41
42 42 42
43 43 43
44 44 44
45 45 45
46 46 46
47 47 47
48 48 48
49 49 49
None None None
None None None
None None None
None None None
None None None
None None None
None None None
None None None
None None None
None None None
"""




















        
