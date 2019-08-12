def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    num = 0
        
    for k in aDict:
        if len(aDict[k]) >= num:
            num = len(aDict[k])
            key = k
        
    return key
        