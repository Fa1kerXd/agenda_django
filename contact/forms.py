from . import models
from django.forms import ModelForm, ValidationError
from django import forms

class ContactForm(ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o primeiro nome',
            
        }),
        label='Primeiro Nome',
        help_text='Digite o Primeiro Nome'
    )
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

       
    class Meta:
        model = models.Contact
        fields = 'first_name',"last_name", "phone", 'email', 'description', 'category',
      

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        msg = ValidationError('Primeiro nome não pode ser igual ao segundo nome', code='invalid')
        if first_name == last_name:
            self.add_error('first_name',msg)
            self.add_error('last_name',msg)
       

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not str(first_name).isalpha():
            self.add_error(
                'first_name',
                ValidationError(
                    'Digite apenas Letras',
                    code='invalid'
                )
            )
        if len(str(first_name)) < 2:
            self.add_error(
                'first_name',
                ValidationError(
                    'Não existe nome com apenas uma letra!',
                    code='invalid'
                )
            )

        
        return first_name



