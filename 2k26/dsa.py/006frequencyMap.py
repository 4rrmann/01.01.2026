nums = [5,6,7,7,1,9,111,1,1,5,1,1]

freq_map = dict()

for i in range(0, len(nums)): #O(n)
    if nums[i] in freq_map: #O(1)
        freq_map[nums[i]] +=1 #O(1)
    else:
        freq_map[nums[i]] =1 #O(1)

print(freq_map)

# time Complexity: O(n)
# space Complexity: O(n) {considering worst case}