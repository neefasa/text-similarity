import numpy as np
from itertools import combinations
import sys 
import json

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
    Words are counted in two samples of text. A list of unique words is returned along with a list of the word counts for each sample.
    '''
    word_list = []
    t1_word_count = []
    
    #Vectorize text1
    for word in simple_clean(text1).split():
        
        #This accounts for a multiple occurance of a word
        if word in word_list:
            t1_word_count[word_list.index(word)] += 1
        else:
            word_list.append(word)
            t1_word_count.append(1)
    
    #Create list of zeros for text2 to corespond to the word_list
    t2_word_count = [0 for _ in word_list]
    
    #Vectorize text2
    for word in simple_clean(text2).split():
        if word in word_list:
            t2_word_count[word_list.index(word)] += 1
        else:
            #This accounts for words that weren't in the first text sample
            word_list.append(word)
            t1_word_count.append(0)
            t2_word_count.append(1)
            
    return word_list, t1_word_count, t2_word_count

def measure_similarity(text1, text2):
    '''
    Given two strings of text, as similarity score is returned.
    '''
    word_list, text1_vector, text2_vector = vectorize_text(text1,text2)
    score = cos_sim(text1_vector, text2_vector)
    return f'{score:.2f}'

def measure_similarity_multiple(samples):
    '''
    Given a dictionary of samples. The text similarity is measured and printed for each combination.
    '''
    results = dict()
    
    for (name1,text1),(name2,text2) in combinations(samples.items(), 2):
        similarity_score = measure_similarity(text1, text2)
        # results.append(f'{name1} and {name2} have a similarity of {similarity_score}')
        results[f'{name1} and {name2}'] = similarity_score
    return results



if __name__ == '__main__':
    try:
        sample_file = sys.argv[1]
    except:
        exit('''
        Include a file with text samples.
        e.g. $python text_similarity.py <file>''')
    with open(sample_file,'r') as f:
        data = f.read()
        samples = json.loads(data)
        results = measure_similarity_multiple(samples)
        for samples, score in results.items():
            print(f'{samples} have a similarity of {score}')
    