def two_sum(nums, target):
    hash_map = {}

        
    for i, num in enumerate(nums):
        need_result = target - nums[i] 
        if need_result in hash_map :
            return [i, hash_map.get(need_result)]
        hash_map[num] = i
        
        
        # for y in range(len(nums)):
        #     if y == i:
        #         continue
        #     if nums[y] == need_result:
        #         return [i, y]

print(two_sum([3,3],  6))


