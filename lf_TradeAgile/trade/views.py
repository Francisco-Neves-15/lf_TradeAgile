from django.shortcuts import render, redirect  # Importa funções para renderizar templates e redirecionar
from .models import Produto, Venda, ItensVenda, Cliente, Fornecedor, Vendedor  # Importa os modelos utilizados
from .forms import ClienteForm, UserRegistrationForm  # Importa os formulários personalizados
from django.contrib.auth import authenticate, login, logout  # Importa funções de autenticação
from django.contrib.auth.forms import AuthenticationForm  # Importa o formulário de autenticação padrão
from django.contrib.auth.decorators import login_required  # Importa o decorador para proteger views


# Função de visão para a página inicial
def index(request):
    return render(request, 'trade/index.html')  # Redireciona para a página inicial

# Função de visão para cadastro de clientes
def cadastro_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # Cria uma instância do formulário com os dados POST
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva o novo cliente no banco de dados
            return redirect('demonstrativo_tabelas')  # Redireciona para a página inicial após o cadastro
    else:
        form = ClienteForm()  # Cria um formulário vazio se não for uma requisição POST
    return render(request, 'trade/cadastro_clientes.html', {'form': form})  # Renderiza a página de cadastro de clientes

# Função de visão para demonstrar tabelas de clientes, fornecedores, produtos e vendas
def demonstrativo_tabelas(request):
    clientes = Cliente.objects.all()  # Obtém todos os clientes
    fornecedores = Fornecedor.objects.all()  # Obtém todos os fornecedores
    produtos = Produto.objects.all()  # Obtém todos os produtos
    vendas = Venda.objects.all()  # Obtém todas as vendas
    return render(request, 'trade/demonstrativo_tabelas.html', {
        'clientes': clientes,  # Passa a lista de clientes para o template
        'fornecedores': fornecedores,  # Passa a lista de fornecedores para o template
        'produtos': produtos,  # Passa a lista de produtos para o template
        'vendas': vendas,  # Passa a lista de vendas para o template
    })

# Função de visão para exibir a galeria de produtos
def galeria_produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos
    return render(request, 'trade/galeria_produtos.html', {'produtos': produtos})  # Renderiza a galeria de produtos

# Função de visão para realizar uma venda
def realizar_venda(request):
    if request.method == 'POST':
        # Lógica simplificada para processar a venda
        cliente_id = request.POST.get('cliente')  # Obtém o ID do cliente do formulário
        produto_id = request.POST.get('produto')  # Obtém o ID do produto do formulário
        quantidade = request.POST.get('quantidade')  # Obtém a quantidade do produto
        cliente = Cliente.objects.get(idcli=cliente_id)  # Obtém o cliente pelo ID
        produto = Produto.objects.get(idprod=produto_id)  # Obtém o produto pelo ID
        vendedor = Vendedor.objects.first()  # Supondo que há um vendedor padrão
        fornecedor = produto.idforn  # Obtém o fornecedor do produto

        valor_venda = produto.valorprod * int(quantidade)  # Calcula o valor total da venda
        venda = Venda.objects.create(
            codivend='12345',  # Código de venda gerado automaticamente
            idcli=cliente,
            idforn=fornecedor,
            idvende=vendedor,
            valorvend=valor_venda,
            descvend=0,
            totalvend=valor_venda,
            datavend='2024-07-30',  # Data atual
            valorcomissao=valor_venda * vendedor.porcvende / 100  # Calcula a comissão do vendedor
        )

        ItensVenda.objects.create(
            idvend=venda,
            idprod=produto,
            valoritvend=produto.valorprod,
            qtditvend=quantidade,
            descitvend=0
        )

        return redirect('demonstrativo_tabelas')  # Redireciona para a página inicial após a venda

    clientes = Cliente.objects.all()  # Obtém todos os clientes para o formulário
    produtos = Produto.objects.all()  # Obtém todos os produtos para o formulário
    return render(request, 'trade/realizar_venda.html', {
        'clientes': clientes,  # Passa a lista de clientes para o template
        'produtos': produtos,  # Passa a lista de produtos para o template
    })

# Função de visão para gerenciar o login dos usuários
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Passa os dados do formulário
        if form.is_valid():  # Verifica se o formulário é válido
            username = form.cleaned_data.get('username')  # Obtém o nome de usuário
            password = form.cleaned_data.get('password')  # Obtém a senha
            user = authenticate(username=username, password=password)  # Tenta autenticar o usuário
            if user is not None:  # Se o usuário for autenticado com sucesso
                login(request, user)  # Faz o login do usuário
                return redirect('index')  # Redireciona para a página inicial
            else:
                form.add_error(None, "Nome de usuário ou senha inválidos.")  # Adiciona erro se a autenticação falhar
    else:
        form = AuthenticationForm()  # Se não for POST, cria um novo formulário
    return render(request, 'trade/login.html', {'form': form})  # Renderiza o formulário de login

# Função de visão para gerenciar o registro de novos usuários
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Cria uma instância do formulário com os dados POST
        if form.is_valid():  # Verifica se o formulário é válido
            user = form.save()  # Salva o novo usuário no banco de dados
            login(request, user)  # Faz o login automático do novo usuário
            return redirect('index')  # Redireciona para a página inicial
        else:
            form.add_error(None, "Erro ao registrar o usuário.")  # Adiciona um erro se a validação falhar
    else:
        form = UserRegistrationForm()  # Se não for POST, cria um novo formulário
    return render(request, 'trade/register.html', {'form': form})  # Renderiza o formulário de registro

# Função de visão protegida que só pode ser acessada por usuários autenticados
@login_required
def welcome_view(request):
    return render(request, 'trade/welcome.html')  # Renderiza a página de boas-vindas

# Função de visão para gerenciar o logout dos usuários
def logout_view(request):
    logout(request)  # Realiza o logout do usuário
    return redirect('login')  # Redireciona para a página de login