from django.forms import ModelForm
from .models import exp

class Expense(ModelForm):
    class Meta:
        model=exp
        fields =('name','price','catagory')
