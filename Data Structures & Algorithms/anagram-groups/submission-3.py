class Solution:
    def groupAnagrams(self, strs):
        import string
        letters = string.ascii_lowercase
        values = {}
        for i in range(len(letters)):
            values[letters[i]] = i

        anagrams = {}
        for word in strs:
            hashing = [0] * 26
            for char in word:
                index = values[char]
                hashing[index] = hashing[index] + 1
            if tuple(hashing) not in anagrams:
                anagrams[tuple(hashing)] = []
            anagrams[tuple(hashing)].append(word)

        return [anagrams[parts] for parts in anagrams]