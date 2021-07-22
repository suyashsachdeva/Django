from django import forms

from .models import fuckoff as product

class ProductForm(forms.ModelForm):
    class Meta :
        model = product
        fields =  [
            'title',
            'description',
            'price'
        ]


class RawProform(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()