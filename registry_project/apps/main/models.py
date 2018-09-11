from django.db import models


from apps.util import models as utilmodels


class Module(models.Model):

    name = models.CharField(max_length=300)
    description = models.TextField(blank=None, null=None)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.name
    

class Mentor(utilmodels.People):
    username_discord = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Mentor"
        verbose_name_plural = "Mentores"


class Student(utilmodels.People):
    username_discord = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ('last_name', 'first_name')


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    date_pay = models.DateField(null=True, blank=True)
    period = models.DateField(null=True, blank=True)
    concept = models.TextField(null=True, blank=True)
    receipt = models.CharField(max_length=50)
    value = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return "{} {}".format(self.student, self.value)
    

class Teen(models.Model):

    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name='teen')

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        return self.name
    


class Course(models.Model):

    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    students = models.ManyToManyField(Student, blank=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.name
    