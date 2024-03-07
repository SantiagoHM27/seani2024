from django.db import models

from django.contrib.auth.models import User
from career.models import Career
from library.models import Module, Question

# Create your models here.
class Stage(models.Model):

    stage = models.IntegerField(
        verbose_name = "Etapa",
    )
    application_date = models.DateField(
        verbose_name = "Fecha de Aplicacion"
    )

    def month(self):
        months = [
            'enero', 'febrero', 'marzo', 
            'abril', 'mayo', 'junio', 'julio', 
            'agosto', 'septiembre', 'octubre',  
            'noviembre', 'diciembre'
            ]
        return months[self.application_date.month - 1]
    month.short_description = 'Mes'
    
    def year(self):
        return self.application_date.year
    year.short_description = 'Año'
    
    def __str__(self):
        return f"{ self.stage } - { self.month() } { self.year() }"
    
    class Meta:
        verbose_name = "etapa"
        verbose_name_plural = "etapas"

class Exam(models.Model):
    user = models.OneToOneField(
                User,
            on_delete=models.CASCADE,
            verbose_name="usuario"
            )
    career = models.ForeignKey(
                Career,
            on_delete=models.CASCADE,
            verbose_name="carrera"
                )
    stage = models.ForeignKey(
                Stage,
            on_delete=models.CASCADE,
            verbose_name="etapa"
                )
    module = models.ManyToManyField(
                Module,
                through='ExamModule',
                verbose_name="modulo"
                )
    questions = models.ManyToManyField(
                Question,    
                through='Breakdown',
                verbose_name="Preguntas"
                )
    score = models.FloatField(
                default=0.0,
                verbose_name="Calificacion"
                )
    created = models.DateTimeField(
                auto_now_add=True,
                verbose_name="Fecha de creacion"
                )
    updated = models.DateTimeField(
                auto_now=True,
                verbose_name="Fecha de actualizacion"
                )


    def __str__(self):
        return f"{self.user} - { self.career } - { self.score }"
    
    class Meta:
        verbose_name="examen"
        verbose_name_plural = "examenes"

class ExamModule(models.Model):
    exam = models.ForeignKey(
                Exam,
                on_delete=models.CASCADE,
                verbose_name="Examen"
                )
    module = models.ForeignKey(
                Module,
                on_delete=models.CASCADE,
                verbose_name="Modulo"
                )
    active = models.BooleanField(
                default=True,
                verbose_name="Activo"
                )
    score = models.FloatField(
                default=0.0,
                verbose_name="Calificacion"
                )

    def __str__(self):
        return f"{ self.module } - { self.score }"



    class Breakdown(models.Model):
        exam = models.ForeignKey(
                Exam,
                on_delete=models.CASCADE,
                verbose_name="Examen"
                )
        question = models.ForeignKey(
                Question,
                on_delete=models.CASCADE,
                verbose_name="Pregunta"
                )
        answer = models.CharField(
                max_length=5,
                default = '-',
                verbose_name="Respuesta"
                )
        correct = models.CharField(
                max_length=5,
                default = '-',
                verbose_name="Respuesta correcta"
                )

        def __str__(self):
            return f"{self.question} - {self.answer}"
        
        

