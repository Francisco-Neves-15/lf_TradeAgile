from django.db import models  # Importa a biblioteca de modelos do Django

# Modelo para Vendedor
class Vendedor(models.Model):
    idvende = models.AutoField(primary_key=True)  # ID do vendedor, gerado automaticamente
    codivende = models.CharField(max_length=10)  # Código do vendedor
    nomevende = models.CharField(max_length=100)  # Nome do vendedor
    razasocvende = models.CharField(max_length=100)  # Razão social do vendedor
    fonevende = models.CharField(max_length=20)  # Telefone do vendedor
    porcvende = models.FloatField()  # Percentual de comissão do vendedor

    class Meta:
        db_table = 'vendedor'  # Nome da tabela no banco de dados

# Modelo para Produto
class Produto(models.Model):
    idprod = models.AutoField(primary_key=True)  # ID do produto, gerado automaticamente
    codiprod = models.CharField(max_length=20)  # Código do produto
    descprod = models.CharField(max_length=100)  # Descrição do produto
    valorprod = models.FloatField()  # Valor do produto
    situprod = models.CharField(max_length=1)  # Situação do produto (ativo/inativo)
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)  # Chave estrangeira para Fornecedor
    imagens = models.CharField(max_length=2000)

    class Meta:
        db_table = 'produto'  # Nome da tabela no banco de dados

# Modelo para Fornecedor
class Fornecedor(models.Model):
    idforn = models.AutoField(primary_key=True)  # ID do fornecedor, gerado automaticamente
    codiforn = models.CharField(max_length=10)  # Código do fornecedor
    nomeforn = models.CharField(max_length=100)  # Nome do fornecedor
    razasocforn = models.CharField(max_length=100)  # Razão social do fornecedor
    foneforn = models.CharField(max_length=20)  # Telefone do fornecedor

    class Meta:
        db_table = 'fornecedor'  # Nome da tabela no banco de dados

# Modelo para Cliente
class Cliente(models.Model):
    idcli = models.AutoField(primary_key=True)  # ID do cliente, gerado automaticamente
    codcli = models.CharField(max_length=10)  # Código do cliente
    nomecli = models.CharField(max_length=100)  # Nome do cliente
    razasoccli = models.CharField(max_length=100)  # Razão social do cliente
    datacli = models.DateField()  # Data de cadastro do cliente
    cnpjcli = models.CharField(max_length=20)  # CNPJ do cliente
    fonecli = models.CharField(max_length=20)  # Telefone do cliente
    cidcli = models.CharField(max_length=50)  # Cidade do cliente
    estcli = models.CharField(max_length=100)  # Estado do cliente

    class Meta:
        db_table = 'cliente'  # Nome da tabela no banco de dados

# Modelo para Itens da Venda
class ItensVenda(models.Model):
    iditvend = models.AutoField(primary_key=True)  # ID do item de venda, gerado automaticamente
    idvend = models.ForeignKey('Venda', on_delete=models.CASCADE)  # Chave estrangeira para Venda
    idprod = models.ForeignKey('Produto', on_delete=models.CASCADE)  # Chave estrangeira para Produto
    valoritvend = models.FloatField()  # Valor do item na venda
    qtditvend = models.IntegerField()  # Quantidade do item vendido
    descitvend = models.FloatField()  # Desconto do item na venda

    class Meta:
        db_table = 'itensvenda'  # Nome da tabela no banco de dados

# Modelo para Venda
class Venda(models.Model):
    idvend = models.AutoField(primary_key=True)  # ID da venda, gerado automaticamente
    codivend = models.CharField(max_length=10)  # Código da venda
    idcli = models.ForeignKey('Cliente', on_delete=models.CASCADE)  # Chave estrangeira para Cliente
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)  # Chave estrangeira para Fornecedor
    idvende = models.ForeignKey('Vendedor', on_delete=models.CASCADE)  # Chave estrangeira para Vendedor
    valorvend = models.FloatField()  # Valor total da venda
    descvend = models.FloatField()  # Desconto total da venda
    totalvend = models.FloatField()  # Total da venda após descontos
    datavend = models.DateField()  # Data da venda
    valorcomissao = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da comissão do vendedor

    class Meta:
        db_table = 'venda'  # Nome da tabela no banco de dados

# Modelo para Backup de Cliente
class ClienteBkp(models.Model):
    idcli = models.AutoField(primary_key=True)  # ID do cliente, gerado automaticamente
    codcli = models.CharField(max_length=10)  # Código do cliente
    nomecli = models.CharField(max_length=100)  # Nome do cliente
    razasoccli = models.CharField(max_length=100)  # Razão social do cliente
    datacli = models.DateField()  # Data de cadastro do cliente
    cnpjcli = models.CharField(max_length=20)  # CNPJ do cliente
    fonecli = models.CharField(max_length=20)  # Telefone do cliente
    cidcli = models.CharField(max_length=50)  # Cidade do cliente
    estcli = models.CharField(max_length=100)  # Estado do cliente

    class Meta:
        db_table = 'clientesbkp'  # Nome da tabela no banco de dados