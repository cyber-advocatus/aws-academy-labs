# Lab 6 — Auto Scaling e Load Balancing

## 📋 Descrição

Implementação de Auto Scaling e Elastic Load Balancing para criar uma arquitetura escalável e de alta disponibilidade.

## 🏗️ Arquitetura Final

```
Internet
    ↓
Application Load Balancer (LabELB)
    ↓          ↓
EC2 (AZ-A)  EC2 (AZ-B)   ← Auto Scaling Group
(Lab Instance) (Lab Instance)
    ↑ escala automaticamente ↑
  CloudWatch Alarms
```

## ✅ O que foi feito

- Criação de AMI a partir do Web Server 1 (WebServerAMI)
- Criação do Target Group (LabGroup)
- Criação do Application Load Balancer (LabELB)
- Criação do Launch Template (LabConfig)
- Criação do Auto Scaling Group (Lab Auto Scaling Group)
- Teste de escalabilidade com Load Test
- Encerramento do Web Server 1 original

## 🔧 Configurações

### AMI
```
Nome: WebServerAMI
Descrição: Lab AMI for Web Server
```

### Target Group
```
Nome: LabGroup
Tipo: Instances
VPC: Lab VPC
```

### Load Balancer
```
Nome: LabELB
Tipo: Application Load Balancer
VPC: Lab VPC
Subnets: Public Subnet 1 e Public Subnet 2
Security Group: Web Security Group
Listener: HTTP:80 → LabGroup
```

### Launch Template
```
Nome: LabConfig
AMI: WebServerAMI
Tipo: t2.micro
Key pair: vockey
Security Group: Web Security Group
CloudWatch detalhado: Habilitado
```

### Auto Scaling Group
```
Nome: Lab Auto Scaling Group
Launch Template: LabConfig
VPC: Lab VPC
Subnets: Private Subnet 1 e Private Subnet 2
Load Balancer: LabGroup
Mínimo: 2
Desejado: 2
Máximo: 6
Política: Target Tracking
Métrica: CPU Utilization
Target: 60%
Tag: Name = Lab Instance
```

## 📊 Alarmes CloudWatch criados automaticamente

```
AlarmHigh: CPU > 60% por 3 minutos → adiciona instâncias
AlarmLow:  CPU < 42% por 15 minutos → remove instâncias
```

## 💡 Conceitos aprendidos

- **AMI** — Template para replicar instâncias configuradas
- **Application Load Balancer** — Distribui tráfego HTTP (camada 7)
- **Target Group** — Grupo de instâncias que recebem tráfego
- **Launch Template** — Configuração para novas instâncias do Auto Scaling
- **Auto Scaling Group** — Gerencia escala automática de instâncias
- **Target Tracking Policy** — Mantém CPU próxima ao target (60%)
- **CloudWatch Alarms** — Disparam ações de escala
- **Escala horizontal** — Adiciona/remove instâncias conforme demanda
- **Alta disponibilidade** — Múltiplas AZs com Load Balancer

## 🏆 Resultado

**35/35 pontos** ✅
