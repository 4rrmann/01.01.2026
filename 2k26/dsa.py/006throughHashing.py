nums = [5,6,7,7,1,9,111,1,1,5,1,1]

hash_map = {}
n = len(nums)

for i in range(0,n): #O(n)
    hash_map[nums[i]] = hash_map.get(nums[i],0) +1 #O(1)

print(hash_map)

# time Complexity: O(n)
# space Complexity: O(n) {considering worst case}