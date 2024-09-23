class Solution(object):
    def twoSum(self, numbers, target):
        \\\
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        \\\

        left_ptr = 0
        right_ptr = len(numbers)-1
        while(left_ptr < right_ptr):
            current_sum = numbers[left_ptr] + numbers[right_ptr]
            #if sum is greater than target, decrement right pointer
            if(current_sum > target):
                right_ptr -= 1
            #if sum less than target, increment left pointer
            elif(current_sum < target):
                left_ptr += 1
            #if sum = target, we have a solution so return the two numbers
            else:
                return [left_ptr+1, right_ptr+1]
        


