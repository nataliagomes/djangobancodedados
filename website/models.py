from django.db import models

# Create your models here.

class Pessoa(models.Model):
    GENERO= ( 
        ('M' , 'Masculino'),
        ('F','Feminino'),
        ('O','Outros'),

    )


    nome = models.CharField(
        max_length=255,
        verbose_name= 'Nome'
    )
    sobrenome = models.CharField (
        max_length=255,
        verbose_name='sobrenome'
    )       
    genero = models.CharField(
        max_length=255,
        verbose_name='Genero',
        choices=GENERO
        #para o que conseguir prever 
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='Email'

    )
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True) 
 
    def __str__(self):
        return self.nome + ' ' + self.sobrenome 
    
