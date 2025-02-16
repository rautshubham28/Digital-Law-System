import json
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer

def get_similar_cases(search_query):
    words = open('VirtualAdvisor/Data/catchword_to_case.json', 'r')
    catchwords_dict = json.load(words)
    catchwords = []
    tokenizer = RegexpTokenizer(r'\w+')
    case_tokens = tokenizer.tokenize(search_query)
	# print(act_tokens)

    for key in catchwords_dict:
        catchwords.append(key)

    rel_catchwords = process.extract(search_query, catchwords, limit =100 ,scorer=fuzz.token_set_ratio)
    rel_cases = {}
    exist = {}
    categories = []
    for c in rel_catchwords:
        if c[1]==100:
            categories.append(c[0])
            for cases in catchwords_dict[c[0]]:
                if cases in exist:
                    exist[cases]+=1
                else:
                    exist[cases]=1

    rel_cases = dict( sorted(exist.items(),
                           key=lambda item: item[1],
                           reverse=True))
    return rel_cases, categories

def cases_info(rel_cases):
    f = open('VirtualAdvisor/Data/case_to_info.json','r')
    cases_info_dict = json.load(f)
    rel_cases_info = []
    i=0
    for case in rel_cases:
        cases_info_dict[case]["id"] = i
        rel_cases_info.append(cases_info_dict[case])
        i+=1
    
    return rel_cases_info

def query1(search_query):
    rel_cases, categories = get_similar_cases(search_query)

    rel_cases_info = cases_info(rel_cases)
    return rel_cases_info, categories

if __name__ == '__main__':
    search_query = input("Enter query = ")
    result, categories = query1(search_query)