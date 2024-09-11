class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0 #make that digit a zero
                if i == 0: #if we reach the first element
                    digits[i] = 1
                    digits.append(0) #append a zero to the end
                    return digits
            else:
                digits[i] +=1
                return digits

        

        


            
        