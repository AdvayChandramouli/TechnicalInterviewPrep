class Solution(object):
    def reverseWords(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\

        rev_words = \\
        words = s.split()

        for i in range(0, len(words), 1):
            words[i] = words[i][::-1]
            rev_words += words[i]

            if(i == len(words)-1):
                break
            else:
                rev_words += \ \

        return rev_words    

        