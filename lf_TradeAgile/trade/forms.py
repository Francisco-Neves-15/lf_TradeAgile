from django import forms  # Importa a biblioteca de formulários do Django
from .models import Cliente  # Importa o modelo Cliente
from django.contrib.auth.models import User  # Importa o modelo User do Django
from django.contrib.auth.forms import UserCreationForm  # Importa o formulário de criação de usuário padrão

# Classe de formulário para o modelo Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Especifica que o modelo a ser usado é Cliente
        fields = '__all__'  # Inclui todos os campos do modelo Cliente no formulário

# Classe de formulário personalizado para registro de usuários
class UserRegistrationForm(UserCreationForm):
    # Campo de email adicionado ao formulário
    email = forms.EmailField()  # Adiciona um campo de email ao formulário

    class Meta:
        # Classe interna para configurar o formulário
        model = User  # Especifica que o modelo a ser usado é User
        # Campos do formulário
        fields = ['username', 'email', 'password1', 'password2']  # Define os campos a serem incluídos no formulário