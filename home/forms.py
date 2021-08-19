from home.models import Car
from users import forms


class UploadCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('title', 'brand', 'description', 'volume', 'price', 'release_date',
                  'color', 'transmission', 'rul','owner', 'image')


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('title', 'brand', 'description', 'volume', 'price',
                  'color', 'transmission', 'rul', 'image')
