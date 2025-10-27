#User function Template for python3

class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        def backtrack(i,target):
            if target==0:
                return True
            if i==len(arr) or target<0:
                return False
            return backtrack(i+1,target-arr[i]) or backtrack(i+1,target)
        return backtrack(0,K)
            
            
        # Code herehttps://media.geeksforgeeks.org/img-practice/chatIcon-1653561581.svg