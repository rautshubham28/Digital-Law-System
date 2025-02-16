################## Methods ###################
# query 1 -> minimal number of stopwords ratio
# query 2 -> ACT or abberviations match 
# query 3 -> v, vs, versus comes in middle
##############################################

def is_query2(query) :
    query = query.lower()
    if (query.find("act") or query.find("bill")) != -1 :
        return 1
    else:
        return 0
        
def is_query3(query) :
    query = query.lower()
    if (query.find(" v ") or query.find(" vs ") or query.find(" v.s. ") or query.find(" v.s ") or query.find("versus")) != -1 :
        return 1
    else :
        return 0



def identify_query_type(query) :

    if is_query2(query) :
        return 2

    if is_query3(query) :
        return 3
    return 1
   


