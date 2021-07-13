from django.db import models


class User(models.Model):
	user_name = models.CharField(max_length=15, unique=True, verbose_name='Nome Completo')
	email = models.EmailField(unique=True, verbose_name='E-mail')
	tel = models.IntegerField(verbose_name='Celular', unique=True)
	

	def __str__(self):
		return self.user_name

