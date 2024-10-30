"""
This function should take three strings as input:
the main text, the target substring, and the replacement substring.

It should return a new string where all occurrences of the target substring within the main text
are replaced with the replacement substring.

EXAMPLE:
    "hello world", "world", "TypeScript") == "hello TypeScript"
    "hello world world", "world", "TypeScript") == "hello TypeScript TypeScript"
)
"""

def search_replace(main_text, target_word, replacement_word):
    words = main_text.split()
    for word in words:
        print(word)

    

search_replace('hello mr man', 'mr', 'replaced!')