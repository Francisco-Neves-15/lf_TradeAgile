-- Inserindo dados na tabela vendedor
INSERT INTO vendedor (codivende, nomevende, razasocvende, fonevende, porcvende) VALUES
('V001', 'João da Silva', 'João da Silva Ltda', '123456789', 5.0),
('V002', 'Maria Oliveira', 'Maria Oliveira & Cia', '987654321', 7.5);

-- Inserindo dados na tabela fornecedor
INSERT INTO fornecedor (codiforn, nomeforn, razasocforn, foneforn) VALUES
('F001', 'Fornecedor A', 'Fornecedor A S.A.', '555123456'),
('F002', 'Fornecedor B', 'Fornecedor B Ltda', '555654321');

-- Inserindo dados na tabela produto
INSERT INTO produto (codiprod, descprod, valorprod, situprod, idforn_id) VALUES
('P001', 'Produto X', 50.0, 'A', 1),
('P002', 'Produto Y', 75.0, 'A', 2);

-- Inserindo dados na tabela cliente
INSERT INTO cliente (codcli, nomecli, razasoccli, datacli, cnpjcli, fonecli, cidcli, estcli) VALUES
('C001', 'Cliente A', 'Cliente A Ltda', '2024-01-01', '12.345.678/0001-90', '111223344', 'São Paulo', 'SP'),
('C002', 'Cliente B', 'Cliente B S.A.', '2024-02-01', '98.765.432/0001-12', '556677889', 'Rio de Janeiro', 'RJ');

-- Inserindo dados na tabela venda
INSERT INTO venda (codivend, idcli_id, idforn_id, idvende_id, valorvend, descvend, totalvend, datavend, valorcomissao) VALUES
('V0001', 1, 1, 1, 100.0, 10.0, 90.0, '2024-07-31', 10.00),
('V0002', 2, 2, 2, 200.0, 20.0, 180.0, '2024-07-30', 15.00);

-- Inserindo dados na tabela itensvenda
INSERT INTO itensvenda (idvend_id, idprod_id, valoritvend, qtditvend, descitvend) VALUES
(1, 1, 50.0, 2, 5.0),
(2, 2, 75.0, 3, 10.0);

-- Inserindo dados na tabela clientesbkp
INSERT INTO clientesbkp (codcli, nomecli, razasoccli, datacli, cnpjcli, fonecli, cidcli, estcli) VALUES
('C003', 'Backup Cliente A', 'Backup Cliente A Ltda', '2024-01-10', '11.111.111/0001-11', '112233445', 'São Paulo', 'SP'),
('C004', 'Backup Cliente B', 'Backup Cliente B S.A.', '2024-02-15', '22.222.222/0001-22', '554433221', 'Rio de Janeiro', 'RJ');

ALTER TABLE produtos
ADD imagens varchar(2000);

update produto set imagens = 'https://thepersonalshop.co.uk/cdn/shop/products/personalised-free-text-plant-pot-the-personal-shop-30426294616215_800x.jpg?v=1631455685'
where codiprod = 'P001'

update produto set imagens = 'https://www.harlaarts.com/cdn/shop/files/134L-IV_800x.png?v=1709279000'
where codiprod = 'P002'
('https://thepersonalshop.co.uk/cdn/shop/products/personalised-free-text-plant-pot-the-personal-shop-30426294616215_800x.jpg?v=1631455685'),
('https://www.harlaarts.com/cdn/shop/files/134L-IV_800x.png?v=1709279000');