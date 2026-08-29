class Solution:
    def isValid(self, s: str) -> bool:
        ocm = {
            '(':')',
            '[':']',
            '{':'}'
        }

        st = []
        for i in s:
            if i in ocm:
                st.append(i)
            else:
                if not st:
                    return False
                top = st.pop()
                if ocm[top] != i:
                    return False
        return not st
                