def naive(pattern, text):
    list_of_occurs = []
    i = 0
    j = 0
    k = 0
    last = len(text) - len(pattern)
    while i <= last:
        end = i + len(pattern) - 1
        while j <= end:
            if not pattern[k] == text[j]:
                break
            if j == end:
                list_of_occurs.append(i)
            k += 1
            j += 1
        k = 0
        i += 1
        j = i
    return list_of_occurs

def kmp(pattern, text):
    list_of_occurs = []
    def p(pattern):
        length = len(pattern)
        arr = [0] * length
        i = 0
        j = 1
        while j < length:
            if pattern[i] == pattern[j]:
                arr[j] = i + 1
                i += 1
                j += 1
            elif i != 0:
                i = arr[i - 1]
            else:
                j += 1
        return arr

    if pattern and text:
        prefix = p(pattern)
        n = 0
        m = 0
        while n < len(text):
            if text[n] == pattern[m]:
                n += 1
                m += 1
            elif m != 0:
                m = prefix[m - 1]
            else:
                n += 1
            if m == len(pattern):
                list_of_occurs.append(n - m)
                m = prefix[m - 1]
    return list_of_occurs


def kr(pattern, text):
    list_of_occurs = []
    pass


# pat = 'aiai'
# text = 'aiaisdi, what is aiaiaisdi? aisdaisdii'
# pat = 'b'
# text = 'absbab'
# print(naive(pat, text))
# print(kmp(pat, text))

# kmp("abraabra", "asdasdasdasd")
