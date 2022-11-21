from django.db import models

# Create your models here.
class DiseaseType(models.Model):
    did = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.did

class Country(models.Model):
    cname = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.cname
    

class Disease(models.Model):
    disease_code = models.CharField(max_length=50,primary_key=True)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    did = models.ForeignKey(DiseaseType,on_delete=models.CASCADE)

    def __str__(self):
        return self.disease_code

class Discover(models.Model):
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code =models.ForeignKey(Disease, on_delete=models.CASCADE)
    first_enc_date = models.DateField

   

class Users(models.Model):
    email = models.CharField(max_length=60,unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname=models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class PublicServant(models.Model):
    email = models.ForeignKey(Users,on_delete=models.CASCADE)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Doctor(models.Model):
    email = models.ForeignKey(Users,on_delete=models.CASCADE)
    degree = models.CharField(max_length=20)

    def __str__(self):
        return self.degree

class Specialize(models.Model):
    did = models.ForeignKey(DiseaseType,on_delete=models.CASCADE)
    email = models.ForeignKey(Users,on_delete=models.CASCADE)

    

class Record(models.Model):
    email = models.ForeignKey(Users,on_delete=models.CASCADE)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code =models.ForeignKey(Disease, on_delete=models.CASCADE)
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()

    
