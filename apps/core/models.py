from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    empresa = models.CharField(max_length=200, blank=True)
    projeto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome