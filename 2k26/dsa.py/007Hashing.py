n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0] * 11 #0...10 indices

for num in n:
    hash_list[num] +=1

for num in m:
    if num<1 or num>len(hash_list): #defines the range
        print(f"{num}:",0)
    else:
        print(f"{num}:",hash_list[num])

# time Complexity: O(n+m)
# space Complexity: O(11) <-> O(1) {contsant}