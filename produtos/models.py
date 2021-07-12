from django.db import models



class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100, unique=True)
    comentario = models.TextField('Comentário', max_length=255) 
    criacao = models.DateTimeField(auto_now_add=True)
    publicacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
