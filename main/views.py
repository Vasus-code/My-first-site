from django.template import loader
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Db
from .forms import DbForm

class DbCreateView(CreateView):
	template_name = 'main/register.html'
	form_class = DbForm
	success_url = '/main/'


def index(request):
	dbs = Db.objects.all()
	context = {'dbs': dbs}
	template = 'main/index.html'
	return render(request, template, context)

