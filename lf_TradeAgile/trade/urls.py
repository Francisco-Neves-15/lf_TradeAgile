from django.urls import path  # Importa a função path para definir URLs
from . import views  # Importa todas as views do módulo atual

# Lista de padrões de URL para a aplicação
urlpatterns = [
    path('cadastro_clientes/', views.cadastro_clientes, name='cadastro_clientes'),  # URL para a página de cadastro de clientes
    path('demonstrativo_tabelas/', views.demonstrativo_tabelas, name='demonstrativo_tabelas'),  # URL para a página de demonstrativo de tabelas
    path('galeria_produtos/', views.galeria_produtos, name='galeria_produtos'),  # URL para a página de galeria de produtos
    path('realizar_venda/', views.realizar_venda, name='realizar_venda'),  # URL para a página de realizar vendas
    path('', views.login_view, name='login'),  # URL para a página de login, chamando a view login_view
    path('logout/', views.logout_view, name='logout'),  # Ativação da View para Logout
    path('welcome/', views.welcome_view, name='welcome'),  # URL para a página inicial da aplicação
    path('index/', views.index, name='index'),  # URL para a página inicial da aplicação
    path('register/', views.register_view, name='register'),  # URL para a página de registro, chamando a view register_view
]