# Lab 2 — Criar VPC e Servidor Web

## 📋 Descrição

Criação de uma VPC completa com subnets públicas e privadas em duas Zonas de Disponibilidade, configuração de Security Groups e lançamento de um servidor web EC2.

## 🏗️ Arquitetura

```
VPC: lab-vpc (10.0.0.0/16)
├── Availability Zone A (us-east-1a)
│   ├── Subnet Pública 1:  10.0.0.0/24
│   ├── Subnet Privada 1:  10.0.1.0/24
│   └── NAT Gateway
└── Availability Zone B (us-east-1b)
    ├── Subnet Pública 2:  10.0.2.0/24  ← Servidor Web aqui!
    └── Subnet Privada 2:  10.0.3.0/24
```

## ✅ O que foi criado

- VPC com CIDR 10.0.0.0/16
- 2 Subnets públicas (uma por AZ)
- 2 Subnets privadas (uma por AZ)
- Internet Gateway
- NAT Gateway
- Tabelas de rotas pública e privada
- Security Group (porta 80 HTTP)
- Instância EC2 com servidor web Apache

## 🔧 Configurações

### Security Group
```
Nome: Web Security Group
Regra de entrada:
  Tipo: HTTP
  Porta: 80
  Source: 0.0.0.0/0
```

### Instância EC2
```
Nome: Web Server 1
AMI: Amazon Linux 2023
Tipo: t2.micro
Subnet: lab-subnet-public2
IP público: Habilitado
```

## 📜 Script User Data

```bash
#!/bin/bash
dnf install -y httpd wget php mariadb105-server
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-ACCLFO-2/2-lab2-vpc/s3/lab-app.zip
unzip lab-app.zip -d /var/www/html/
chkconfig httpd on
service httpd start
```

## 💡 Conceitos aprendidos

- **VPC** — Rede privada virtual na AWS
- **CIDR** — Notação de endereçamento IP (/16 = 65.536 IPs)
- **Subnet pública** — Acessa internet via Internet Gateway
- **Subnet privada** — Acessa internet via NAT Gateway
- **Internet Gateway** — Entrada e saída de internet
- **NAT Gateway** — Somente saída (protege recursos privados)
- **Security Group** — Firewall no nível da instância (Stateful)
- **User Data** — Script executado automaticamente na inicialização

## 🏆 Resultado

**30/30 pontos** ✅
