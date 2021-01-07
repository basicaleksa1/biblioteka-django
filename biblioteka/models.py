from django.db import models


class Autor(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=20)

    def __str__(self):
        return self.ime + self.prezime


class Knjiga(models.Model):
    STATUS = (
        ('biografija', 'biografija'),
        ('komedija', 'komedija'),
        ('drama', 'drama'),
        ('roman', 'roman'),
    )
    isbn = models.CharField(max_length=50)
    naziv = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, null=True, on_delete=models.SET_NULL)
    zanr = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.naziv

