from django.db import models


class People(models.Model):

    MEN = 'Masculino'
    WOMAN = 'Femenino'

    SEX = (
        ('men', MEN), 
        ('woman', WOMAN), 
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, blank=True, null=True)
    sex = models.CharField(max_length=20, choices=SEX, blank=True, null=True)
    email = models.EmailField()
    cellphone = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        abstract = True
        
    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)

    