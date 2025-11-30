text = input("Enter a paragraph: ")

words = text.lower().split()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

k = int(input("Enter value of k: "))

sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print(f"\nTop {k} most frequent words:\n")
for word, count in sorted_words[:k]:
    print(word, ":", count)
