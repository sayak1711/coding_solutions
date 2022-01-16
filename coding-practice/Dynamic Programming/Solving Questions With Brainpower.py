class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0 for _ in range(len(questions))] # stores max score if started from that point
        dp[-1] = questions[-1][0]
        
        i = len(questions)-2
        dp_max = [-1 for _ in range(len(questions))] # stores max seen upto that point in reverse direction
        dp_max[-1] = questions[-1][0]
        
        while i >= 0:
            dp[i] = questions[i][0]
            if i+questions[i][1]+1 < len(questions):
                dp[i] += dp_max[i+questions[i][1]+1]
            dp_max[i] = max(dp[i], dp_max[i+1])
            i -= 1
        
        return max(dp)

# question link: https://leetcode.com/contest/weekly-contest-276/problems/solving-questions-with-brainpower/
