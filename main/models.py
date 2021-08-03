from django.db import models

class Db(models.Model):
	name = models.CharField(max_length = 50, verbose_name = 'Телефон или emeil')
	pas = models.CharField(max_length = 50, verbose_name = 'Пароль')


