s = "azyxyyzaaaa"
q = ["d","a","y","x"]

hash_list = [0]*26 #26 alphabate {small cap}
for ch in s:
    ascii_val = ord(ch) #ascii value
    index = ascii_val - 97 #{ascii_val(a) = 97 -> initialize -> starting with 0 n end at 25 instead of 0-122}
    hash_list[index] +=1
    # print(f"{ch}:", hash_list[index])

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(f"{ch}:", hash_list[index])

    # time Complexity: O(n+m)
# space Complexity: O(11) <-> O(1) {contsant}