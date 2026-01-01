n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

freq_map = {}
for i in n:
    if i in freq_map:
        freq_map[i] +=1
    else:
        freq_map[i] = 1
# print(freq_map)

result = {}
# m_freq = dict()
for i in m:
    if i in freq_map:
        result[i] = freq_map[i]
    else:
        result[i] = 0

print(result)

# time Complexity: O(n+m)
# space Complexity: O(1) {contsant}