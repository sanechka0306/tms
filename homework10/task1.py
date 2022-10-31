def longest_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read().split()
        longest_word_list = []
        long_word = max(text, key=len)
        longest_word_list.append(long_word)
        for word in text:
            if len(word) == len(long_word) and word != long_word:
                longest_word_list.append(word)
        print(*longest_word_list)


longest_words('article.txt')
