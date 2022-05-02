from django.shortcuts import render
from .forms import LeadAddForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
from dadata import Dadata

from lead_app.settings import URL_PARAM 

token = "0c37a434a17b1ab220bada81b2b67e4eb323d9a7"
secret = "b07d5816bc21f5768392dd52c3e29ac0f6d5ce5d"
dadata = Dadata(token, secret) 

# Create your views here.
def index(request):
	
	if request.method == 'POST':
		form_lead_add = LeadAddForm(request.POST)
		
		if form_lead_add.is_valid():
			fio_client = str(form_lead_add.cleaned_data['fio_client'])
			phone_client = str(form_lead_add.cleaned_data['phone_client'])
			address_client = str(form_lead_add.cleaned_data['address_client'])
			result_name = dadata.clean("name", fio_client)
			result_address = dadata.clean("address", address_client)

			params = {'fields': {'NAME': result_name['name'],'SECOND_NAME': result_name['patronymic'],
            'LAST_NAME': result_name['surname'],'PHONE': [{'VALUE': phone_client,'VALUE_TYPE':'WORK'},
            {'VALUE': phone_client, 'VALUE_TYPE': 'HOME'}], 'ADDRESS': address_client},
             'params': { 'REGISTER_SONET_EVENT': 'Y' }}
			a = requests.post(URL_PARAM, json=params)
			return HttpResponseRedirect(reverse('post_ok') )
	else:
		form_lead_add = LeadAddForm(initial={'fio_client': 'Иванов Иван Иванович'})

	return render(request, 'index.html', {'form': form_lead_add})


def post_ok(request):
	return render(request, 'post_ok.html')