from django import forms


class PortfolioForm(forms.Form):
    title = forms.CharField(max_length=30)
    image = forms.ImageField()
    description = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
