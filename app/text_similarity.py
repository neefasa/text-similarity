import numpy as np
from itertools import combinations

def simple_clean(text:str):
    '''Simple function to remove [,.] and to make all letters lowercase.'''
    return text.lower().replace(',','').replace('.','')

def cos_sim(vector1, vector2):
    '''
    Recreate the cosine similarity function. 
    Takes two vectors and outputs a float between 0 and 1.
    Closer to 1 means they are more similar.
    Closer to 0 means they are less similar.
    '''
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

def vectorize_text(text1:str, text2:str):
    '''
    Takes two strings and returns two vectors of their word counts.
    '''
    word_list = []
    t1_word_count = []
    
    #Vectorize text1
    for word in simple_clean(text1).split():
        if word in word_list:
            t1_word_count[word_list.index(word)] += 1
        else:
            word_list.append(word)
            t1_word_count.append(1)
    
    #Create list of zeros for text2
    t2_word_count = [0 for _ in t1_word_count]
    
    #Vectorize text2
    for word in simple_clean(text2).split():
        if word in word_list:
            t2_word_count[word_list.index(word)] += 1
        else:
            word_list.append(word)
            t1_word_count.append(0)
            t2_word_count.append(1)
            
    return word_list, t1_word_count, t2_word_count

# def measure_similarity(samples):
#     for (name1,text1),(name2,text2) in combinations(samples.items(), 2):
#         vector1, vector2 = vectorize_text(text1, text2)[1:]
#         similarity_score = cos_sim(vector1, vector2)
#         # print(f'{name1} and {name2} have a similarity of {similarity_score:.2f}')
#         

def measure_similarity(text1, text2):
    return f'{cos_sim(*vectorize_text(text1,text2)[1:]):.2f}'


    