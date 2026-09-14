I=['a','e','i','o','u','A','E','I','O','U']
def main():
    word=input('Input: ')
    s_word=shorten(word)
    print(s_word)

def shorten(word):
    for i in I:
        word=word.replace(i,'')
    return word

if __name__ == "__main__":
    main()
