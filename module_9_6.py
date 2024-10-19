def all_variants(text):
    i = 0
    for i in range(1, len(text) + 1):
        for j in range(len(text) + 1 - i):
            yield text[j:j + i]


a = all_variants("abc")
for i in a:
    print(i)
b = all_variants("abcd") #даже с чётными работает :)
for i in b:
    print(i)

