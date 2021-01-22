# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         sub_str=''
#         for i in s:
#             if s.count(i)==1:
#                 sub_str+=i
#                 print(i)
#         return sub_str
#
# if __name__ == '__main__':
#
#     obj=Solution()
#     s="abcabcbb"
#     r=obj.lengthOfLongestSubstring(s)
#     print(r)

s='pwwkew'
sub_str=''
di={}
for i in s:
    di[i]=s.count(i)
l=list(di.keys())
for j in l:
    sub_str+=j
print(sub_str)
