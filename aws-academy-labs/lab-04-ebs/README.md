# Lab 4 — Trabalhando com Amazon EBS

## 📋 Descrição

Criação e gerenciamento de volumes EBS: anexar à instância EC2, criar sistema de arquivos, criar snapshot e restaurar dados.

## ✅ O que foi feito

- Criação de volume EBS de 1 GiB
- Anexação do volume à instância EC2
- Criação de sistema de arquivos ext3
- Montagem do volume em /mnt/data-store
- Criação de arquivo de teste
- Criação de snapshot (backup)
- Deleção do arquivo (simulando perda)
- Restauração via snapshot
- Confirmação da recuperação dos dados

## 🔧 Configurações

### Volume EBS
```
Tipo: SSD de uso geral (gp2)
Tamanho: 1 GiB
Tag Name: My Volume
```

### Snapshot
```
Tag Name: My Snapshot
```

### Volume restaurado
```
Tag Name: Restored Volume
Criado a partir do snapshot
```

## 📜 Comandos utilizados

```bash
# Ver armazenamento disponível
df -h

# Criar sistema de arquivos ext3
sudo mkfs -t ext3 /dev/sdf

# Criar diretório de montagem
sudo mkdir /mnt/data-store

# Montar o volume
sudo mount /dev/sdf /mnt/data-store

# Configurar montagem automática no boot
echo "/dev/sdf   /mnt/data-store ext3 defaults,noatime 1 2" | sudo tee -a /etc/fstab

# Verificar arquivo de configuração
cat /etc/fstab

# Criar arquivo de teste
sudo sh -c "echo some text has been written > /mnt/data-store/file.txt"

# Verificar conteúdo
cat /mnt/data-store/file.txt

# Deletar arquivo (simular perda)
sudo rm /mnt/data-store/file.txt

# Montar volume restaurado
sudo mkdir /mnt/data-store2
sudo mount /dev/sdg /mnt/data-store2

# Verificar recuperação
ls /mnt/data-store2/
```

## 💡 Conceitos aprendidos

- **EBS** — Armazenamento persistente em bloco para EC2
- **Armazenamento em bloco** — Altera só o bloco modificado (eficiente!)
- **Sistema de arquivos ext3** — Formato de filesystem Linux
- **Ponto de montagem** — Diretório onde o volume é acessado
- **Snapshot** — Backup incremental do volume EBS (salvo no S3)
- **Snapshot de linha de base** — Primeiro snapshot (completo)
- **Restauração** — Criar novo volume a partir de snapshot

## 🏆 Resultado

**25/25 pontos** ✅
