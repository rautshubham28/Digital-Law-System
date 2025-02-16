from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .template import Template
import json

_template = Template()

# Create your views here.
def index(request):
	if request.method == 'POST':
		search = json.loads(request.body)['search']								# Accept user query and search if any relevant
		category, title = _template.get_category(search)						# template is present in database. Return the result
		return JsonResponse({ 'category': category, 'title': title })
	else:
		return render(request, 'Templates/index.html')

@login_required
def template(request, template):
	if template == 'tenant_notice':
		return render(request, 'Templates/tenant_notice.html')
	if template == 'breach_of_contract':
		return render(request, 'Templates/breach_of_contract.html')
	if template == 'resignation':
		return render(request, 'Templates/resignation.html')
	if template == 'defamation':
		return render(request, 'Templates/defamation.html')
	if template == 'rti':
		return render(request, 'Templates/rti.html')