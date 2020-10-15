def vigenere(word, key, encode=True):
    key_length = len(key)
    result = ""
    for index in range(0, len(word)):
        letter = ord(word[index]) - ord("a")
        key_letter = ord(key[index % key_length]) - ord("a")
        difference = letter + key_letter if encode else letter - key_letter
        decoded_letter = difference % 26 + ord("a")
        result += chr(decoded_letter)
    
    return result

def encode(word, key):
    return vigenere(word, key, encode=True)

def decode(word, key):
    return vigenere(word, key, encode=False)

mode = input()
key = input()
word = input()
print(encode(word, key) if mode == "encode" else decode(word, key))
