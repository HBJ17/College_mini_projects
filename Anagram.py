word1 = input("Enter word 1 = ")
word2 = input("Enter word 2 = ")

word1 = word1.lower()
word2 = word2.lower()

word1 = list(word1)
word2 = list(word2)

word1 = sorted(word1)
word2 = sorted(word2)

if word1 == word2:
    print("The input words are Anagrams.")
else:
    print("The input words are not Anagrams.")



