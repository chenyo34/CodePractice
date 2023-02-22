def getPrefixScores(arr):
    
    ans = []
    for i in range(1,len(arr)+1):
        cur_arr = []
        temp = arr[:i]
        cur = max(temp)
        for n in temp:
            n += cur
            cur_arr.append(n)
            cur = n
        ans.append(sum(cur_arr) % (10**9+7))
    return ans


###############
#### Test Cases
###############


arr = [5, 1, 4, 2]

print(getPrefixScores(arr))

