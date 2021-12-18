from django import forms
from bootstrap_modal_forms.forms import BSModalForm, BSModalModelForm
from django_select2.forms import Select2Widget
from locations.models import Location

class LocationForm(BSModalModelForm):
    
          
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'setup': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-info btn-sm'}),
            'area': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-info btn-sm'}),
            'contact01': forms.TextInput(attrs={'class': 'form-control'}),
            'contact02': forms.TextInput(attrs={'class': 'form-control'}),
            'contact03': forms.TextInput(attrs={'class': 'form-control'}),
            'contact04': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-info btn-sm'}),
        }
        
       
    
    