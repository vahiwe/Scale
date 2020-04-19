from django import forms
from .models import Resource, ResourceCategory

class ResourceCategoryForm(forms.Form):
    category = forms.ModelChoiceField(
                queryset=ResourceCategory.objects.all(), 
                empty_label='Not Specified', 
                widget=forms.Select(attrs={ 
                                   "onChange":'getresources()'})
                )