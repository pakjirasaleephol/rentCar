from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Person
from .models import Car,Rent
from .forms import PersonForm
from django.views.generic.list import ListView

def home(request):
	return render(request,'home.html')

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='create.html'
	form_class = PersonForm
	success_url = '/admin'

class ListCarView(ListView):
    model = Car
    template_name='car_list.html'

class ListRentView(ListView):
    model = Rent
    template_name='rent_list.html'