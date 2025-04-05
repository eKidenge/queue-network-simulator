from django import forms

class SimulationForm(forms.Form):
    customers = forms.IntegerField(min_value=1, max_value=100, initial=10)
    time_steps = forms.IntegerField(min_value=10, max_value=10000, initial=1000)
