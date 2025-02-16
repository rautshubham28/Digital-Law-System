import json
from collections import OrderedDict
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer



copy_rankings = {}

def cal(x):
	if x in copy_rankings:
		return -copy_rankings[x]
	else:
		return 0


def get_related_acts(search_query):

	file = open('VirtualAdvisor/Data/actlist.txt' , 'r')

	abb_file = open('VirtualAdvisor/Data/abbreviation_mapping.json', 'r')
	abb_dict = json.load(abb_file)
	acts = []

	for act in file:
		act = act.rstrip('\n')
		acts.append(act)

	for key in abb_dict:
		acts.append(key)

	file.close()

	# print(acts[:10])


	rel_acts = process.extract(search_query, acts, limit =50 ,scorer=fuzz.token_set_ratio)
	copy_rel_acts = []
	i = 0
	for act in rel_acts:
		if act[0] in abb_dict:
			for x in abb_dict[act[0]]:
				copy_rel_acts.append(x)
		else :
			copy_rel_acts.append(act[0])
	
	return copy_rel_acts

def get_related_cases(rel_acts):
	

	f = open('VirtualAdvisor/Data/act_to_cases.json','r')

	act_to_case_dict = json.load(f)
	rel_cases = []
	for act in rel_acts:
		# print(act)
		try:
			for x in act_to_case_dict[act]:
				rel_cases.append(x)
		except :
			pass
	print(rel_cases)
	f = open('VirtualAdvisor/Data/case_to_info.json','r')
	cases_info_dict = json.load(f)
	rel_cases_info = []
	i=0
	for case in rel_cases:
		cases_info_dict[case]["id"] = i
		rel_cases_info.append(cases_info_dict[case])
		i+=1
    
	return rel_cases_info



def query2(search_query):
	search_query = search_query.replace('.', '')

	rel_acts = get_related_acts(search_query)	

	final_dict = get_related_cases(rel_acts)

	return final_dict

if __name__ == '__main__':
	search_query = input("search query = ")
	final = query2(search_query)
