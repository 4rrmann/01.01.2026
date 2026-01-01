s = "azyxyyzaaaa"
q = ["d","a","y","x"]

freq_map = {}
for i in s:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1
print(freq_map)

result = {}
for i in q:
    if i in freq_map:
        result[i] = freq_map[i]
    else:
        result[i] = 0
print(result)

# time Complexity: O(n+m)
# space Complexity: O(11) <-> O(1) {contsant}