class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for each in s:
            if each in ["(","{","["]:
                res.append(each)
            else:
                if not res:
                    return False
                last_char = res.pop()    
                if last_char == "(":
                    if each != ")":
                        return False
                if last_char == "{":
                    if each !="}":
                        return False
                if last_char == "[":
                    if each !="]":
                        return False
        if res:
            return False
        return True                                        
