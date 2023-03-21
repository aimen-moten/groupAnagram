# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Solution to Leetcode 49
# --------------------------------

# Algorithm:
    # 1. Create a default dictionary of type list to store the result. Using a default dictionary helps us avoid key error.
    # 2. Loop through all strings in the array.
    # 3. For each string, initialise a count array. This count array is created to keep a track of the count of all alphabets that occur in that string.
    # 4. Loop through each character in the string.
    # 5. For each character, increment the count of it at the relevant position. Remember, the aim is to have a mapped to index 0, b mapped to index 1 and so on.
    # 6. After the increments, append that string to the result dictionary. The key will be the pattern of the number of characters in the form a tuple, since the key cannot be a list.append
    # 7. Finally, return the values portion of the result (since we don't need the keys).

# Code:

from collections import defaultdict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)                                     #creating a default dictionary of type list
    for s in strs:                                              #looping through every string to identify alphabet patterns
        count = [0] * 26                                        #initialising count array to be 0 for all 26 alphabets (assuming english lowercase alphabet)
        for c in s:                                             #looping through each character in the current string
            count[ord(c)-ord("a")] += 1                         #incrementing count at the relevant position of alphabet, designed in a way that a maps to 0 and so on
        res[tuple(count)].append(s)                             #casting the count array to a tuple to generate a pattern and using that pattern as key to append the string to
    return res.values()                                         #returning the values of all keys in the res array

# Time Complexity:
# O(m*n) where m is the length of the array and n is the average length of every string

# Space Complexity:
# O(26m) => O(m)

# To test:
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))