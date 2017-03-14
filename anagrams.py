WORDLIST = open("dictionary.txt", 'r')

def enough_letters(word, letters):
    return all([word.count(letter) <= letters.count(letter) for letter in word])

def get_anagrams(letters):
    anagrams = []
    letters = letters.lower()
    for line in WORDLIST.readlines():
        if len(line.strip()) < 16 and len(line.strip()) > 2:
            if all([letter in letters for letter in line.strip().lower()]):
                anagrams.append(line.strip().lower())

    anagrams = filter(lambda word: enough_letters(word, letters), anagrams)

    return anagrams
