from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .query import query1 as query_1
from .query2 import query2 as query_2
from .case_names import query_3
from .query_classifier import identify_query_type

# Create your views here.
def index(request):
    if request.method == 'POST':
        categories = []
        search = json.loads(request.body)['search']
        query_type = identify_query_type(search)
        if query_type == 1:
            allResults, categories = query_1(search)
        elif query_type == 2:
            allResults = query_2(search)
        else:
            allResults = query_3(search)
        return JsonResponse({ 'AllResult': allResults[:10], 'matched': categories })
    else:
        return render(request, 'VirtualAdvisor/index.html')