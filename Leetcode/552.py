class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 1
        # Possible states: n00, n01, n02, n10, n11, n12.
        # Current State        A        L       P       (m = n - 1)
        #       n00           m10      m01     m00
        #       n01           m10      m02     m00
        #       n02           m10      N/A     m00
        #       n10           N/A      m11     m10
        #       n11           N/A      m12     m10
        #       n12           N/A      N/A     m10
        m00 = m01 = m02 = m10 = m11 = m12 = 1
        for length in range(1, n):
            m00, m01, m02, m10, m11, m12 = m10 + m01 + m00, m10 + m02 + m00, m10 + m00, m11 + m10, m12 + m10, m10
        return (m10 + m01 + m00) % 1000000007

# O(N) for time. O(1) for space.

# class Solution:
#     def checkRecord(self, n: int) -> int:
#         maxValue = 10 ** 9 + 7
#         mapDict = {}
#         def recordCount(length, letterALeft, consecutiveLetterL):
#             if length == 0:
#                 return 1
#             key = length * 100 + letterALeft * 10 + consecutiveLetterL
#             if mapDict.get(key, 0) != 0:
#                 return mapDict[key]
#             else:
#                 sub = 0
#                 if letterALeft > 0:
#                     sub += recordCount(length - 1, letterALeft - 1, 0)
#                 if consecutiveLetterL != 2:
#                     sub += recordCount(length - 1, letterALeft, consecutiveLetterL + 1)
#                 sub += recordCount(length - 1, letterALeft, 0)
#                 mapDict[key] = sub
#                 return sub
#         total = recordCount(n, 1, 0)
#         return total % (10 ** 9 + 7)

# This solution will exceed call stack limit of python in leetcode
# O(N) for time and space.

# class Solution {
# public:
#     int checkRecord(int n) {
#         if (n == 0)
#             return 1;
#         // Possible states: n00, n01, n02, n10, n11, n12.
#         // Current State        A        L       P       (m = n - 1)
#        //       n00           m10      m01     m00
#        //       n01           m10      m02     m00
#        //       n02           m10      N/A     m00     # Done with m10 and m00 here.
#        //       n10           N/A      m11     m10
#        //       n11           N/A      m12     m10
#        //       n12           N/A      N/A     m10     # Done with m12 here.
#         unsigned long long int m00 = 1, m01 = 1, m02 = 1, m10 = 1, m11 = 1, m12 = 1, n00, n01, n02, n10, n11, MOD = 1000000007;
#         for (int i = 1; i < n; i++)
#         {
            
#             n00 = m10 + m01 + m00;
#             n01 = m10 + m02 + m00;
#             n02 = m10 + m00;
#             n10 = m11 + m10;
#             n11 = m12 + m10;
            
#             m12 = m10;
#             m00 = n00 % MOD;
#             m01 = n01 % MOD;
#             m02 = n02 % MOD;
#             m10 = n10 % MOD;
#             m11 = n11 % MOD;
#         }
#         return (m10 + m01 + m00) % 1000000007;
#     }
# };
        
