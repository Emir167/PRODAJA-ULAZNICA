from django.db import models
from utakmice.models import Utakmica
from loginovanje.models import Korisnik

class TipKarte(models.Model):
    naziv = models.CharField(max_length=100)
    def __str__(self):
        return self.naziv


class Karte(models.Model):
    tip_karte = models.ForeignKey(TipKarte, on_delete=models.CASCADE)
    kupac = models.ForeignKey(Korisnik, on_delete = models.RESTRICT, null=True, blank=True)
    cena = models.DecimalField(max_digits=6, decimal_places=2)


class PreostaloKarata(models.Model):
    utakmica = models.ForeignKey(Utakmica, on_delete = models.CASCADE)
    tip_karte = models.ForeignKey(TipKarte, on_delete=models.CASCADE)
    preostalo = models.PositiveIntegerField()