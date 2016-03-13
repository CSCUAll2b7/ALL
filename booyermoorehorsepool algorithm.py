###The Class of the searching algorithm###
def BoyerMooreHorspool(pattern, text):
    m = len(pattern)
    n = len(text) ###The pattern and text that will be compared with eachother###
    if m > n:
        return -1 ###Move on to the next chatacter###
    next1 = []
    ###This goes over the text, and matches the pattern, if they do not match, they move over to the next character###
    for k in range(256):
        next1.append(m)
        
    for k in range(m - 1):
        next1[ord(pattern[k])] = m - k - 1###Taking away in order to find the valies###

    next1 = tuple(next1)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
        if j == -1: return i + 1
        k += next1[ord(text[k])]
    return -1

if __name__ == '__main__':
    text = "this is the string to search in"
    pattern = "this"
    s = BoyerMooreHorspool(pattern, text)
    print('Text:',text)
    print('Pattern:',pattern)
    if s > -1:
        print('Pattern \"' + pattern + '\" found at position',s)



