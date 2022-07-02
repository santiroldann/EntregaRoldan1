from django import forms


class NuevoJuego(forms.Form):
    
    juego = forms.CharField(max_length=30)
    grupo = forms.IntegerField(min_value=0)