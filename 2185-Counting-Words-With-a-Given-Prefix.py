class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int

        for each word in words:
            if pref in word AND if the index of the substring == 0
                count += 1

        """
        pref_length = len(pref)
        pref_count = 0
        

        for word in words:
            #if(word[0:pref_length] == pref):
            if((pref in word) and (word.find(pref) == 0)):
                pref_count += 1
            

        return pref_count





        
        