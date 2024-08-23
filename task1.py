def reverse_word(word):
    letters = list(word)
    start = 0
    end = len(letters) - 1
            
        while start < end:
            if not letters[start] .isalpha():
                start += 1
            elif not letters[end].isalpha():
                end -= 1
            else:
                letters[start], letters[end] = letters[end], letters[start]
                start += 1
                end -= 1
    
    return ' '.join(letters)

def reversed_words(text):
    return ''.join(reverse_word(word) for word in text.split(''))

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

