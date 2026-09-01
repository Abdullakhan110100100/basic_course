# Problem 5: Product of Array Except Self (LC 238)

# Return an array where each element is the product of all other elements. O(n) time, no division.

# product_except_self([1,2,3,4])      # [24,12,8,6]
# product_except_self([-1,1,0,-3,3])  # [0,0,9,0,0]


def product_except_self(nums):
    n = len(nums)
    suffix_arr = [1] * n
    prefix_arr = [1] * n
    answer = [1] * n

    for i in range(1, n ):
        prefix_arr[i] = prefix_arr[i-1] * nums[i-1]
    print(prefix_arr)

    for i in range (n-2, -1, -1 ):
        suffix_arr[i] = nums[i+1] * suffix_arr[i+1]
    print(suffix_arr)

    for i in range(n):
        answer[i] = prefix_arr[i] * suffix_arr[i]
    return answer

# print(product_except_self([1,2,3,4])  )
print(product_except_self([-1,1,0,-3,3]))
    