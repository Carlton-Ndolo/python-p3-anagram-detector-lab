# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = [w for w in words if self.is_anagram(w)]
        return anagrams if anagrams else []

    def is_anagram(self, other):
        return sorted(self.word.lower()) == sorted(other.lower())


