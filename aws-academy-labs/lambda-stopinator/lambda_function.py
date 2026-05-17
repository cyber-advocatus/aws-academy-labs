import boto3

# Configurações
region = 'us-east-1'
instances = ['REPLACE_WITH_INSTANCE_ID']

# Cliente EC2
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    """
    Função Lambda que para instâncias EC2 automaticamente.
    
    Trigger: Amazon EventBridge (rate: 1 minute)
    
    Caso de uso real:
    - Parar servidores de desenvolvimento após expediente
    - Economizar custos com instâncias ociosas
    """
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
    
    return {
        'statusCode': 200,
        'body': f'Instances stopped: {instances}'
    }
