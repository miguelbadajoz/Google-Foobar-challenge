# Level 1
def encription_google(word):

    s='abcdefghijklmnopqrstuvwxyz'
    solution=''

    for letter in x:
        pos = s.find(letter)
        if pos>=0:
            solution = solution + s[-s.find(letter)-1]
        else:
            solution = solution + letter

    return solution

