class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([S.count(c) for c in J])
		
		
S = Solution()
J = "aA"
Stone = 'aAAcabbedfaDbbb'
#print Stone.count('A')
print S.numJewelsInStones(J,Stone)
 