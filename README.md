# Sistema Bancário com Python – POO

![Python](https://img.shields.io/badge/Python-3.x-blue)
![DIO](https://img.shields.io/badge/DIO-Digital%20Innovation%20One-orange)

## Descrição do Projeto

Este projeto é um **sistema bancário desenvolvido em Python** utilizando **Programação Orientada a Objetos (POO)**.  
O sistema permite cadastrar clientes, criar contas bancárias vinculadas a esses clientes, realizar depósitos, saques e exibir extratos de forma modular e organizada.

O projeto foi desenvolvido como parte da certificação:

**Certificação:** Luizalabs – Dominando Funções e Boas Práticas em Python™  
**Curso:** Programação Orientada a Objetos com Python™  
**Módulo:** Modelando o Sistema Bancário em POO com Python™  
**Plataforma:** Digital Innovation One (DIO)

---

## Funcionalidades

- Cadastro de **clientes**, armazenando:
  - Nome
  - Data de nascimento
  - CPF (apenas números)
  - Endereço

- Cadastro de **contas bancárias**, armazenando:
  - Agência (padrão: 0001)
  - Número da conta (sequencial)
  - Cliente vinculado à conta

- Operações bancárias:
  - **Depósito** com validação de valores positivos
  - **Saque** com limite por operação e quantidade máxima de saques
  - **Extrato** exibindo movimentações e saldo atual

- Validação de **CPF duplicado** ao cadastrar clientes
- Mensagens claras em todas as operações, incluindo falhas

---

## Estrutura de Classes

### Cliente
- **Atributos:** `nome`, `data_nascimento`, `cpf`, `endereco`
- Representa um cliente do banco

### ContaBancaria
- **Atributos:** `cliente`, `numero_conta`, `agencia`, `saldo`, `extrato`, `numero_saques`
- **Métodos:** `depositar`, `sacar`, `exibir_extrato`
- Limite de saques: 3 por dia
- Limite por saque: R$ 500,00

---

## Como Executar

1. Clone ou faça download do repositório:

```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git

    Entre na pasta do projeto:

cd nome-do-repositorio

    Execute o script principal:

python sistema_bancario.py

    Siga as instruções interativas para cadastrar clientes, criar contas e realizar operações bancárias.

Exemplo de Uso

# Cadastro de cliente
cliente1 = cadastrar_cliente(clientes)

# Criação de conta vinculada ao cliente
conta1 = cadastrar_conta(contas, cliente1)

# Operações
conta1.depositar(1000)
conta1.sacar(200)
conta1.exibir_extrato()

Saída esperada:

Depósito de R$ 1000.00 realizado com sucesso.
Saque de R$ 200.00 realizado com sucesso.

================ EXTRATO ================
Depósito: R$ 1000.00
Saque: R$ 200.00

Saldo: R$ 800.00
==========================================

Tecnologias Utilizadas

    Python 3.x

    Conceitos de Programação Orientada a Objetos

    Boas práticas de modularização e encapsulamento

Autor: Rogério Clynton Ribeiro

Portfólio: ClyntonBoss

e-Mail: clyntonribeiror@gmail.com
