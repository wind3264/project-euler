def permute(l,s,ans):
    if l == []:
        ans.append(s)
    for e in l:
        l1 = [x for x in l if x != e]
        ans.append(permute(l1, s + str(e), ans))
ans = []
permute([0,1,2,3,4,5,6,7,8,9], "", ans)
ans1 = [x for x in ans if x is not None]
ans1.sort()
print(ans1[999999])
# solved, answer: 2783915460
