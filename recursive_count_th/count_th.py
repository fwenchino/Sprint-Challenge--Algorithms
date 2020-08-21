'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    #word with 2 or more letters
    if len(word) < 2:
        return 0
    
    #verify 2 letters of word 'th'
    elif word[0:2] == 'th':
        #recursive call  into the 2 firts letters
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])
    
