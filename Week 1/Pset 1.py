s = 'abcdefghijklmnopqrstuvwxyz'
words = ''
words_2 = ''

for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        words = words + s[i]
    else:
        words = words + s[i]
        if len(words_2) < len(words):
            words_2 = words
        words = '' 
        
if i == len(s) - 2 and words != '' and words_2 == '':        
    if s[i+1] >= s[i]:
        words_2 = words + s[i+1]
print('Longest substring in alphabetical order is: ' + str(words_2))
    
    