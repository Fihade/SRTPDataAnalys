from django.db import models

# Create your models here.


class rawMaterials(models.Model):
    name = models.CharField(max_length=10, unique=True)
    CaO = models.FloatField(max_length=10)
    SiO2 = models.FloatField(max_length=10)
    Al2O3 = models.FloatField(max_length=10)
    MgO = models.FloatField(max_length=10)
    Fe2O3 = models.FloatField(max_length=10)
    MnO = models.FloatField(max_length=10)
    TiO2 = models.FloatField(max_length=10)
    K2O = models.FloatField(max_length=10)
    Na2O = models.FloatField(max_length=10)
    SO3 = models.FloatField(max_length=10)
    P2O5 = models.FloatField(max_length=10)
    Cr2O3 = models.FloatField(max_length=10)
    Total = models.FloatField(max_length=10, blank=False)

    def __str__(self):
        return self.name


class HeavySetalSlag(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    temp = models.IntegerField()
    strength = models.FloatField(max_length=10)
    rate = models.FloatField(max_length=10)

    def _str_(self):
        return self.temp, self.rate


class RedMud(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    temp = models.IntegerField()
    strength = models.FloatField(max_length=10)
    rate = models.FloatField(max_length=10)

    def __str__(self):
        return self.temp, self.rate


class SteelSlag(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    temp = models.IntegerField()
    strength = models.FloatField(max_length=10)
    rate = models.FloatField(max_length=10)

    def __str__(self):
        return self.temp, self.rate


class VantaiSlag(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    temp = models.IntegerField()
    strength = models.FloatField(max_length=10)
    rate = models.FloatField(max_length=10)

    def __str__(self):
        return self.temp, self.rate


class NiIronSlag(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    temp = models.IntegerField()
    strength = models.FloatField(max_length=10)
    rate = models.FloatField(max_length=10)

    def __str__(self):
        return self.temp, self.rate

