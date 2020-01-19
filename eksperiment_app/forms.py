#Vi trenger form.py filen når vi har en eller annen form/skjema
#som skal legge til noe i databasen vår. 

from django import forms
from .models import Eksperiment
#from .views import rand_penger

#Dette er alt som skal til for å lage form.py filen vår.
class EksperimentForm(forms.ModelForm):
         
    class Meta:
        model = Eksperiment
        fields = ['deklarert_inntekt', ]

    
    def clean_deklarert_inntekt(self):
        #Denne vil gi oss den "default" deklarerte inntekten post-django(etter) clearning
        deklarert_inntekt = self.cleaned_data.get('deklarert_inntekt')
        if (deklarert_inntekt >= 0) and (deklarert_inntekt <= Eksperiment.utbetalt):
            return deklarert_inntekt
        else:
            raise forms.ValidationError("Må være mellom 0 og " + str(Eksperiment.utbetalt))
            