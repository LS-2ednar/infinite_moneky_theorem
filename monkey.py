import random as r

def random_string(number):
    abc = 'abcdefghijklmnopqrstuvwxyz '
    word = list()
    for i in range(number):
        letter = r.randint(0,len(abc)-1)
        word.append(abc[letter])
    word = ''.join(word)
    return(word)
        
def score_match(word1,word2):
    match = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            match += 1
        else:
            continue
    return((match/len(word1))*100)

def matching_time(goal):
    goal = goal.lower()
    word = ""
    score = 0
    record = 0
    counter = 0
    tries  = 0
    print('Match || The monekeys "Sentence"      || Tries')
    while score != 100:
        counter += 1
        tries += 1
        word = random_string(len(goal))
        score = score_match(goal, word)
        if score > record:
            record = score
            rword = word
        if counter == 100:
            print('%.2f || %s || %i' % (record, rword, tries))
            counter = 0    
    print('It is done after %d tries!!!' % tries)
    return(tries)
    
"""
Section to run the functions with a given sentence
"""
goal = 'methinks it is like a weasel'
matching_time(goal)
