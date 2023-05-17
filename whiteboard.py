#Given two strings containing only capital and lowercase letters, write a function that returns true if they are anagrams of each other and false otherwise.
#An anagram is a word, phrase, or name formed by rearranging the letters of another word.

s1 = "anagram"
t1 = "nagaram"
# Output:
# True

#s2 = "rat"
#t2 = "car"
#Output:
# False

#s3 = "stops"
#t3 = "pots"
#Output:
# False

def solution(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())
