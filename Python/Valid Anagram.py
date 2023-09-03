class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sa = list(s)
        ta = list(t)
        a = True
        if len(sa) != len(ta):
                return False
        else:
            for i in range(len(sa)):
                    if sa[i] in ta:
                        ta.remove(sa[i])
                        # print(ta)
                        a = True
                    else:
                        # print("wrong")               
                        a = False
                        break
            return a
                
c = Solution() 
c.isAnagram("vishant","antvish")