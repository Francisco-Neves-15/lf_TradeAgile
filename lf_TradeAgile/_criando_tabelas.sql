CREATE TABLE vendedor (
    idvende INT AUTO_INCREMENT PRIMARY KEY,
    codivende VARCHAR(10) NOT NULL,
    nomevende VARCHAR(100) NOT NULL,
    razasocvende VARCHAR(100) NOT NULL,
    fonevende VARCHAR(20) NOT NULL,
    porcvende FLOAT NOT NULL
);

CREATE TABLE fornecedor (
    idforn INT AUTO_INCREMENT PRIMARY KEY,
    codiforn VARCHAR(10) NOT NULL,
    nomeforn VARCHAR(100) NOT NULL,
    razasocforn VARCHAR(100) NOT NULL,
    foneforn VARCHAR(20) NOT NULL
);

CREATE TABLE produto (
    idprod INT AUTO_INCREMENT PRIMARY KEY,
    codiprod VARCHAR(20) NOT NULL,
    descprod VARCHAR(100) NOT NULL,
    valorprod FLOAT NOT NULL,
    situprod CHAR(1) NOT NULL,
    idforn INT,
    FOREIGN KEY (idforn) REFERENCES fornecedor(idforn)
);

CREATE TABLE cliente (
    idcli INT AUTO_INCREMENT PRIMARY KEY,
    codcli VARCHAR(10) NOT NULL,
    nomecli VARCHAR(100) NOT NULL,
    razasoccli VARCHAR(100) NOT NULL,
    datacli DATE NOT NULL,
    cnpjcli VARCHAR(20) NOT NULL,
    fonecli VARCHAR(20) NOT NULL,
    cidcli VARCHAR(50) NOT NULL,
    estcli VARCHAR(100) NOT NULL
);

CREATE TABLE venda (
    idvend INT AUTO_INCREMENT PRIMARY KEY,
    codivend VARCHAR(10) NOT NULL,
    idcli INT,
    idforn INT,
    idvende INT,
    valorvend FLOAT NOT NULL,
    descvend FLOAT NOT NULL,
    totalvend FLOAT NOT NULL,
    datavend DATE NOT NULL,
    valorcomissao DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (idcli) REFERENCES cliente(idcli),
    FOREIGN KEY (idforn) REFERENCES fornecedor(idforn),
    FOREIGN KEY (idvende) REFERENCES vendedor(idvende)
);

CREATE TABLE itensvenda (
    iditvend INT AUTO_INCREMENT PRIMARY KEY,
    idvend INT,
    idprod INT,
    valoritvend FLOAT NOT NULL,
    qtditvend INT NOT NULL,
    descitvend FLOAT NOT NULL,
    FOREIGN KEY (idvend) REFERENCES venda(idvend),
    FOREIGN KEY (idprod) REFERENCES produto(idprod)
);

CREATE TABLE clientesbkp (
    idcli INT AUTO_INCREMENT PRIMARY KEY,
    codcli VARCHAR(10) NOT NULL,
    nomecli VARCHAR(100) NOT NULL,
    razasoccli VARCHAR(100) NOT NULL,
    datacli DATE NOT NULL,
    cnpjcli VARCHAR(20) NOT NULL,
    fonecli VARCHAR(20) NOT NULL,
    cidcli VARCHAR(50) NOT NULL,
    estcli VARCHAR(100) NOT NULL
);