from django import forms
from .models import Level, LevelUpCategory

class LevelCategoryForm(forms.Form):
    category = forms.ModelChoiceField(
                queryset=LevelUpCategory.objects.all(), 
                empty_label='Not Specified', 
                widget=forms.Select(attrs={ 
                                   "onChange":'getlevels()'})
                )
