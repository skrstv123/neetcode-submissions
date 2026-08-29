class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f'#{len(s)}*{s}'
        # print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        ans = []
        while i < n:
            if s[i] == '#':
                cstr = ''
                i += 1
                cnt = ''
                while i < n and s[i] != r'*':
                    cnt += s[i]
                    i += 1
                i += 1
                endi = i + int(cnt)
                while i < n and i < endi:
                    cstr += s[i]
                    i += 1
                ans.append(cstr)
        return ans



                
