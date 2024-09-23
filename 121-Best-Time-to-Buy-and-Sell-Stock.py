class Solution(object):
    def maxProfit(self, prices):
        \\\
        :type prices: List[int]
        :rtype: int
        \\\
        
        left_ptr = 0
        right_ptr = 1
        max_profit = 0
        while(right_ptr < len(prices)):
            if(prices[left_ptr] < prices[right_ptr]):
                curr_profit = prices[right_ptr] - prices[left_ptr]
                max_profit = max(max_profit, curr_profit)
            else:
                left_ptr = right_ptr
            right_ptr += 1
        
        return max_profit