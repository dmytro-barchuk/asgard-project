from django.db import models

class Payment(models.Model):
    name = models.CharField(verbose_name = "Вид платежа:", max_length=60)	
    describe = models.TextField(verbose_name ="Реквизиты:", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(verbose_name = "Вид контакта:", max_length=60)
    describe = models.TextField(verbose_name ="Сам контакт:", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name