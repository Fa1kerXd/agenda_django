from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError
from django import forms

class ContactForm(ModelForm):
    pictures = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
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
        fields = 'first_name',"last_name", "phone", 'email', 'description', 'category','pictures',
      

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

class RegisterUser(UserCreationForm):
    class Meta:
        first_name = forms.CharField(
            required=True
        )
        last_name = forms.CharField(
            required=True
        )
        email = forms.EmailField(
            required=True
        )
        
        model = User
        fields = 'first_name','last_name','email','username','password1','password2'
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Esse email já existe',
                    code='invalid'
                )
            )
        return email 
     