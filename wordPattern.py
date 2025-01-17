#T(n) = O(n)
#S(n) = O(n)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pDict,sDict={},{}
        sArr=s.split(" ")
        if len(pattern)!=len(sArr):
            return False
        for i in range(0,len(pattern)):
            if pDict.get(pattern[i],-1)==-1:
                pDict[pattern[i]]=sArr[i]
            else:
                if pDict[pattern[i]]!=sArr[i]:
                    return False
            
            if sDict.get(sArr[i],-1)==-1:   
                sDict[sArr[i]]=pattern[i]
            else:
                if sDict[sArr[i]]!=pattern[i]:
                    return False
        return True