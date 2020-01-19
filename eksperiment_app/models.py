from django.db import models
from django.core.exceptions import ValidationError
import random



#Revideringsratene
sansynlighet_revidert = random.randint(1, 100)
revideringsrate2 = 2;
revideringsrate3 = 10;


    # Create your models here.


class Eksperiment(models.Model):
    utbetalt = models.DecimalField(decimal_places=2, max_digits=4, blank=True)
    deklarert_inntekt = models.DecimalField(decimal_places=2, max_digits=4,)
    revidert = models.BooleanField(default=False)
    faktisk_utbetaling = models.DecimalField(decimal_places=2, max_digits=4, blank=True)
    
        
    def __str__(self):
        return "Deklarert inntekt:" + str(self.deklarert_inntekt) + ", utbetalt: " + str(self.utbetalt) + "Revidert: " + str(self.revidert) + "Faktisk utbetaling: " + str(self.faktisk_utbetaling)
    
    @property
    def utbetaling_etter_skatt(self):
        self.faktisk_utbetaling = self.deklarert_inntekt * 0.6
        self.save()
    
    @property
    def utbetaling_metode(self):
        #random pengesum fra listen
        penger = [0.25, 0.50, 0.75, 1, 1.25, 1.50, 1.75, 2]
        randint = random.randint(0, 7)
        rand_penger = penger[randint]
        return rand_penger
    
    @property
    def prob_revidert():
    randint = random.randint(1, 101)
    if randint < 10:
        return True
    else:
        return False

    def save(self, *args, **kwargs):
        self.utbetalt = self.utbetaling_metode
        self.faktisk_utbetaling = self.utbetaling_etter_skatt
        super(Eksperiment, self).save(*args, **kwargs)

        
