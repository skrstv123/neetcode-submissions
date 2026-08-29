from collections import defaultdict as df
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        idg = df(int)
        adj = df(list)
        n = len(words)
        allchars = set(''.join(words))
        for i in range(n-1):
            a, b = words[i], words[i+1]
            la, lb = len(a), len(b)
            if lb < la and a[:lb] == b[:lb]:
                return ""
            for j in range(min(la, lb)):
                if a[j] != b[j]:
                    adj[a[j]].append(b[j])
                    idg[b[j]] += 1
                    break
        queue = [c for c in allchars if idg[c] == 0]
        ans = ''
        while queue:
            cc = queue.pop()
            ans = ans + cc
            for x in adj[cc]:
                idg[x] -= 1
                if idg[x] == 0:
                    queue.append(x)
        return ans if len(ans) == len(allchars) else ''