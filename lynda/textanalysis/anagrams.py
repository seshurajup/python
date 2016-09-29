wordsFile = open('data/words','r')
words = wordsFile.readlines();
print(" Total no of words :",len(words))
print("First 10 words from starting ",words[:10])
convertedWords = [key.strip().lower() for key in words];
print("First 10 words from starting ",convertedWords[:10])
uniqWords = list(set(convertedWords))
uniqWords.sort()
print("First 10 unique words from starting ",uniqWords[:10])


#single line same example 
uniqWords = sorted(list(set([key.strip().lower() for key in open("data/words")])))
print("First 10 unique words from starting ",uniqWords[:10])


#single line same example 
uniqWords = sorted(list(set([key.strip().lower() for key in open("data/words")])))
anagramWords = {''.join(sorted(key)):key for key in uniqWords}
print("First 10 unique words from starting ",anagramWords.keys()[:10])

print(" All anagrams of dictionary",anagramWords[''.join(sorted("dictionary"))])

import collections
anagramWords = collections.defaultdict(list)
for word in uniqWords :
    anagramWords[''.join(sorted(word))].append(word)
print(" All anagrams of dictionary",anagramWords[''.join(sorted("dictionary"))])


