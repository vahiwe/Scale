from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from job.models import Job, Resource, Level, Comments, LevelUpCategory, ResourceCategory

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True,
                            widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if any(x.isupper() for x in username):
            raise forms.ValidationError('Please enter only lowercase letters')
        return username


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class LevelCategoryForm(forms.Form):
    category = forms.ModelChoiceField(
                queryset=LevelUpCategory.objects.all(), 
                empty_label='Not Specified', 
                widget=forms.Select(attrs={ 
                                   "onChange":'getlevels()'})
                )


class ResourceCategoryForm(forms.Form):
    category = forms.ModelChoiceField(
                queryset=ResourceCategory.objects.all(), 
                empty_label='Not Specified', 
                widget=forms.Select(attrs={ 
                                   "onChange":'getresources()'})
                )