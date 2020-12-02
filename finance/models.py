from django.db import models
from django.utils import timezone
from django.urls import reverse

from corecode.models import StudentClass, AcademicSession, AcademicTerm
from employees.models import Employee
from exams.models import Exams

class Invoice(models.Model):
  enterprise = models.CharField(max_length=300,blank=True,verbose_name="Empresa")
  payment_day = models.DateField(default=timezone.now,verbose_name="Fecha Pago")
  #payment_amount = models.IntegerField(blank=True,default=0)
  provider = models.CharField(max_length=300,blank=True,verbose_name="Proveedor")
  payment_link = models.FileField(blank=True, upload_to='finance/payments/',verbose_name="Link Pago") 
  # session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
  # term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
  # class_for = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
  # balance_from_previous_term = models.IntegerField(default=0)
  # status = models.CharField(max_length=20, choices=[(
  #     'active', 'Active'), ('closed', 'Closed')], default='active')

  class Meta:
    ordering = ['payment_day']

  def __str__(self):
    return f'{self.payment_day}-{self.provider}'


  def balance(self):
    payable = self.total_amount_payable()
    paid = self.total_amount_paid()
    return payable - paid

  def amount_payable(self):
    items = InvoiceItem.objects.filter(invoice=self)
    total = 0
    for item in items:
      total += item.amount
    return total

  def total_amount_payable(self):
    return self.amount_payable()

  def total_amount_paid(self):
    receipts = Receipt.objects.filter(invoice=self)
    amount = 0
    for receipt in receipts:
      amount += receipt.amount_paid
    return amount

  def get_absolute_url(self):
    return reverse('invoice-detail', kwargs={'pk': self.pk})


class InvoiceItem(models.Model):
  invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,verbose_name="Pago")
  description = models.CharField(max_length=200,verbose_name="Descripción")
  amount = models.IntegerField()


class Receipt(models.Model):
  invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,verbose_name="Pago")
  employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,verbose_name="Colaborador")
  exams = models.ForeignKey(Exams,on_delete=models.CASCADE,null=True,verbose_name="Exámenes")
  amount_paid = models.IntegerField(verbose_name="Costo Examen")
  date_paid = models.DateField(default=timezone.now,verbose_name="Fecha FV")
  receipt_link = models.FileField(blank=True, upload_to='finance/receipts/',verbose_name="Link") 
  comment = models.CharField(max_length=200, blank=True,verbose_name="Comentarios")

  def __str__(self):
    return f'Receipt on {self.date_paid}'
