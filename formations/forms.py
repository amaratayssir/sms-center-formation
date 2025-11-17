from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Inscription, Formation

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['formation', 'statut']  # Champs du modèle
        widgets = {
            'formation': forms.Select(attrs={'class': 'form-select'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }

class InscriptionUserForm(UserCreationForm):  # Form pour créer user + inscription
    email = forms.EmailField(required=True)
    formation = forms.ModelChoiceField(queryset=Formation.objects.all(), empty_label="Choisir une formation")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'formation')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        inscription = Inscription.objects.create(user=user, formation=self.cleaned_data['formation'])
        return user