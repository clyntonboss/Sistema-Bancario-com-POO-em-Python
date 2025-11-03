# --- Classe Cliente ---
class Cliente:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = ''.join(filter(str.isdigit, cpf))  # Armazena apenas números
        self.endereco = endereco

# --- Classe ContaBancaria ---
class ContaBancaria:
    AGENCIA_PADRAO = "0001"
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500.0

    def __init__(self, cliente: Cliente, numero_conta: int):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.agencia = ContaBancaria.AGENCIA_PADRAO
        self.saldo = 0.0
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor: float):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > self.saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > ContaBancaria.LIMITE_SAQUE_VALOR:
            print(f"Operação falhou! Limite por saque: R$ {ContaBancaria.LIMITE_SAQUE_VALOR:.2f}.")
        elif self.numero_saques >= ContaBancaria.LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(self.extrato, end="")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

# --- Funções auxiliares para cadastro ---
def cadastrar_cliente(lista_clientes):
    nome = input("Nome: ").strip()
    data_nascimento = input("Data de Nascimento: ").strip()
    cpf = input("CPF: ").strip()
    endereco = input("Endereço: ").strip()

    # Verifica duplicidade de CPF
    for c in lista_clientes:
        if c.cpf == ''.join(filter(str.isdigit, cpf)):
            print("Cliente com este CPF já cadastrado!")
            return None

    cliente = Cliente(nome, data_nascimento, cpf, endereco)
    lista_clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    return cliente

def cadastrar_conta(lista_contas, cliente):
    numero_conta = len(lista_contas) + 1
    conta = ContaBancaria(cliente, numero_conta)
    lista_contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    return conta

# --- Inicialização ---
clientes = []
contas = []

# Exemplo de uso:
cliente1 = cadastrar_cliente(clientes)
if cliente1:
    conta1 = cadastrar_conta(contas, cliente1)
    conta1.depositar(1000)
    conta1.sacar(200)
    conta1.exibir_extrato()