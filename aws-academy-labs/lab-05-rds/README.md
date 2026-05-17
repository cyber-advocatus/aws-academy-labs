# Lab 5 — Criar Servidor de Banco de Dados RDS

## 📋 Descrição

Criação de um servidor de banco de dados Amazon RDS MySQL e conexão com uma aplicação web rodando em EC2.

## 🏗️ Arquitetura

```
Internet
    ↓
Web Server (EC2)
    ↓ porta 3306
RDS MySQL (lab-db)
```

## ✅ O que foi feito

- Criação do Security Group para o banco (DB Security Group)
- Criação da instância RDS MySQL (lab-db)
- Conexão da aplicação web ao banco de dados
- Interação com dados via aplicação (Address Book)

## 🔧 Configurações

### DB Security Group
```
Nome: DB Security Group
Descrição: Permit access from Web Security Group
VPC: Lab VPC
Regra de entrada:
  Tipo: MySQL/Aurora
  Porta: 3306
  Source: Web Security Group
```

### Instância RDS
```
Engine: MySQL Community
Identificador: lab-db
Username: main
Classe: db.t3.micro
Storage: 20 GiB (gp2)
VPC: Lab VPC
Security Group: DB Security Group
Public access: No
```

### Conexão da aplicação
```
Endpoint: lab-db.xxxxxx.us-east-1.rds.amazonaws.com
Database: lab
Username: main
Password: lab-password
```

## 💡 Conceitos aprendidos

- **RDS** — Banco de dados relacional gerenciado pela AWS
- **Serviço gerenciado** — AWS cuida de backups, patches, failover
- **Security Group em camadas** — Web SG → DB SG (isolamento!)
- **Princípio do menor privilégio** — Banco só aceita conexão do servidor web
- **Endpoint** — Endereço de conexão do banco de dados
- **Multi-AZ** — Alta disponibilidade (não usado neste lab)
- **Subnet group** — Subnets onde o RDS pode ser criado

## 🏆 Resultado

**20/20 pontos** ✅
