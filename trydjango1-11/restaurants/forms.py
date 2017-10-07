from django import forms

from .models import RestaurantLocation
from .validators import validate_category

class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

    # Validating form data; called when is_valid func is called
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid name')
        return name


class RestaurantLocationCreateForm(forms.ModelForm):
    email = forms.CharField()
    # category = forms.CharField(required=False, validators=[validate_category])
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
        ]
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid name')
        return name
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in email:
            raise forms.ValidationError('no email1')

    # def clean(self):
    #     if self.cleaned_data.get('name') != self.cleaned_data.get('email'):
    #         raise forms.ValidationError('non-field error!!')
