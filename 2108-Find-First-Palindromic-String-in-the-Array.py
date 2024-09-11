class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        for word in words:
            mid_index = int(len(word)/2)
            sub_str1 = word[0:mid_index]
            sub_str2 = ""

            if(len(word)) % 2 == 1: #length of string is odd
                sub_str2 = word[mid_index+1:len(word)]
            else: #length is even
                sub_str2 = word[mid_index:len(word)]

            sub_str2 = sub_str2[::-1] #reverse second substring
            #compare 2 substrings
            if(sub_str1 == sub_str2):
                return word
        
        return ""    


        