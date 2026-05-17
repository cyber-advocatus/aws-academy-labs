# Lambda Stopinator — AWS Lambda + EventBridge

## 📋 Descrição

Função Lambda que para automaticamente uma instância EC2 a cada minuto, usando Amazon EventBridge como trigger.

## 🏗️ Arquitetura

```
EventBridge (a cada 1 minuto)
        ↓
Lambda Function (myStopinator)
        ↓
Para a instância EC2 (instance1)
```

## ✅ O que foi feito

- Criação da função Lambda (myStopinator) com Python 3.11
- Configuração do trigger EventBridge (rate: 1 minuto)
- Código para parar instância EC2 automaticamente
- Verificação via CloudWatch metrics (100% success rate!)

## 🔧 Configurações

### Lambda Function
```
Nome: myStopinator
Runtime: Python 3.11
Role: myStopinatorRole
```

### EventBridge Rule
```
Nome: everyMinute
Tipo: Schedule expression
Expression: rate(1 minute)
```

## 📜 Código da função

```python
import boto3

region = 'us-east-1'
instances = ['INSTANCE_ID_AQUI']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
```

## 💡 Conceitos aprendidos

- **Lambda** — Computação serverless (sem gerenciar servidores)
- **Trigger** — O que dispara a função (EventBridge, S3, API Gateway...)
- **EventBridge** — Serviço de agendamento e eventos
- **Rate expression** — `rate(1 minute)` = a cada 1 minuto
- **Cron expression** — Para agendamentos mais complexos
- **IAM Role** — Permissões que a função Lambda precisa
- **CloudWatch Metrics** — Monitoramento das execuções Lambda

## 💰 Caso de uso real

```
# Para parar servidores de desenvolvimento após o expediente:
# Dispara às 18:01 todo dia útil
cron(1 18 ? * MON-FRI *)

# Para ligar de manhã:
cron(0 8 ? * MON-FRI *)

# Economia: ~40% de redução nos custos de EC2!
```

## 🏆 Resultado

**20/20 pontos** ✅
