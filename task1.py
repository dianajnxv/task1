def reverse_words(text):
    words = text.split(' ')
    reversed_words = []
    
    for word in words:
        letters = list(word)
        start = 0
        end = len(letters) - 1
        
        while start < end:
            if letters[start].isalpha() and letters[end].isalpha():
                letters[start], letters[end] = letters[end], letters[start]
                start += 1
                end -= 1
            elif not letters[start].isalpha():
                start += 1
            elif not letters[end].isalpha():
                end -= 1

        reversed_words.append(''.join(letters))
    
    return ' '.join(reversed_words)

if __name__ == '__main__':
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
    ]
        
    for text, reversed_text in cases:
        result = reverse_words(text)
        print(f"Original: {text} -> Reversed: {result}")
        assert result == reversed_text

