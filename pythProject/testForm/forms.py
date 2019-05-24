from django import forms

class DataForm(forms.Form):
    text = forms.CharField( widget= forms.TextInput(attrs=
                                                    {'class': 'form-control',
                                                    'placeholder': 'Enter text', }
                                                   )
                          )