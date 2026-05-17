# Lab 3 — Introdução ao Amazon EC2

## 📋 Descrição

Exploração do Amazon EC2: criação de instância, monitoramento, configuração de Security Group, redimensionamento e proteções.

## ✅ O que foi feito

- Lançamento de instância EC2 com servidor web
- Monitoramento via CloudWatch e System Log
- Atualização do Security Group para HTTP
- Redimensionamento da instância (t2.micro → t2.small)
- Aumento do volume EBS (8GB → 10GB)
- Teste de Termination Protection e Stop Protection

## 🔧 Configurações

### Instância EC2
```
Nome: Web Server
AMI: Amazon Linux 2023
Tipo: t2.micro (depois redimensionado para t2.small)
Key pair: vockey
Security Group: Web Server security group
Termination Protection: Habilitada
Stop Protection: Habilitada
```

### Security Group
```
Nome: Web Server security group
Regra de entrada:
  Tipo: HTTP
  Porta: 80
  Source: 0.0.0.0/0
```

## 📜 Script User Data

```bash
#!/bin/bash
dnf install -y httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
```

## 💡 Conceitos aprendidos

- **AMI** — Template para criar instâncias EC2
- **Tipos de instância** — t2.micro, t2.small (família, geração, tamanho)
- **User Data** — Automação na inicialização da instância
- **Termination Protection** — Impede deleção acidental
- **Stop Protection** — Impede parada acidental
- **CloudWatch** — Monitoramento de métricas
- **System Log** — Log do console da instância
- **Redimensionamento** — Mudar tipo de instância (requer parada)
- **EBS** — Armazenamento persistente da instância

## 🏆 Resultado

**25/25 pontos** ✅
