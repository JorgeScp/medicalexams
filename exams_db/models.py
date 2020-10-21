from django.db import models
from django.utils import timezone
from django.urls import reverse

from employees.models import Student
from exams.models import Exams
from finance.models import Receipt

class Employee_Record(models.Model):
  date = models.DateField(default=timezone.now,verbose_name="Fecha Registro")
  enterprise = models.CharField(max_length=300,blank=True,verbose_name="Empresa")
  employee = models.ForeignKey(Student,null=True,on_delete=models.CASCADE,verbose_name="Colaborador")
  
  #payment_link = models.FileField(blank=True, upload_to='finance/payments/',verbose_name="Link Pago") 
  # balance_from_previous_term = models.IntegerField(default=0)


  class Meta:
    ordering = ['employee']

  def __str__(self):
    return f'{self.employee}'

class Exams_Record(models.Model):
  type_exam_choices = [
    ('Ingreso','Ingreso'),
    ('Periódico','Periódico'),
    ('Egreso','Egreso'),
    ('Post-Incapacidad','Post-Incapacidad'),
  ]
  concept_choices = [
    ('Apto','Apto'),
    ('Apto con Recomendaciones','Apto con Recomendaciones'),
    ('Apto con Restricciones','Apto con Restricciones'),
    ('Aplazado','Aplazado'),
    ('No Apto','No Apto'),
    ('Satisfactorio','Satisfactorio'),
    ('Satisfactorio con Recomendaciones','Satisfactorio con Recomendaciones'),
    ('No Satisfactorio','No Satisfactorio'),
    ('Sin Hallazgos Clínicos','Sin Hallazgos Clínicos'),
    ('Con Hallazgos Clínicos','Con Hallazgos Clínicos'),
  ]
  sve_choices = [
    ('Ruido','Ruido'),
    ('Vibración','Vibración'),
    ('Presiones barométricas (altas o bajas)','Presiones barométricas (altas o bajas)'),
    ('Temperaturas extremas (altas o bajas)','Temperaturas extremas (altas o bajas)'),
    ('Radiaciones Ionizantes','Radiaciones Ionizantes'),
    ('Radiaciones no Ionizantes','Radiaciones no Ionizantes'),
    ('Iluminación','Iluminación'),
    ('Quimicos','Quimicos'),
    ('Biológicos','Biológicos'),
    ('Psicolaborales','Psicolaborales'),
    ('Ergonómicos','Ergonómicos'),
    ('Cardiovascular - Metabólico','Cardiovascular - Metabólico'),
    ('Ninguno','Ninguno'),
  ]
  receipt = models.ForeignKey(Receipt,null=True,on_delete=models.CASCADE,verbose_name="FV Examenes")
  employee_record = models.ForeignKey(Employee_Record, on_delete=models.CASCADE,verbose_name="Colaborador")
  date = models.DateField(default=timezone.now,verbose_name="Fecha Examen")
  type_exam = models.CharField(max_length=300,choices=type_exam_choices,verbose_name="Tipo Examen")
  concept = models.CharField(max_length=300,choices=concept_choices,verbose_name="Concepto")
  epp = models.CharField(max_length=400,verbose_name="EPP")
  sve = models.CharField(max_length=300,choices=sve_choices,verbose_name="SVE")
  recomendations = models.CharField(max_length=1000,verbose_name="Recomendaciones")
  recomendations_plan = models.CharField(max_length=800,verbose_name="Recomendaciones - Plan de Manejo")
  restrictions = models.CharField(max_length=1000,verbose_name="Restriciones")
  relocate = models.BooleanField(verbose_name="Reubicar")
  comments = models.CharField(max_length=200, blank=True,verbose_name="Comentarios")

  def __str__(self):
    return f'Registro {self.type_exam}-{self.date}'