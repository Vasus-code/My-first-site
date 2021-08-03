from django.forms import ModelForm

from .models import Db

class DbForm(ModelForm):
	class Meta:
		model = Db
		fields = ('name', 'pas')