from django.urls import path

from .views import index,  DbCreateView

urlpatterns = [
	path('join/', DbCreateView.as_view(), name='join'),
	
	path('', index,)
]