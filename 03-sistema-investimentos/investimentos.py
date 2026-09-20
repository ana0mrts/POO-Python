from abc import ABC, abstractmethod
from datetime import datetime

class ContaInvestimento(ABC):
    def __init__(self, saldo_inicial=0.0):
        self._saldo = float(saldo_inicial)

    def depositar(self, v: float):
        if v > 0:
            self._saldo += v

    def sacar(self, v: float):
        if v > 0 and self._saldo >= v:
            self._saldo -= v
        else:
            raise ValueError("Saldo insuficiente.")

    def get_saldo(self) -> float:
        return self._saldo

    @abstractmethod
    def atualizar(self):
        pass


class ContaPoupanca(ContaInvestimento):
    def __init__(self, taxa_mensal: float):
        super().__init__(0.0)
        self._taxa_mensal = float(taxa_mensal)
        self._depositos = []

    def depositar(self, v: float):
        super().depositar(v)
        self._depositos.append(float(v))

    def sacar(self, v: float):
        super().sacar(v)
        if len(self._depositos) > 0:
            self._depositos.pop(0)

    def atualizar(self):
        rendimento = 0.0
        for dep in self._depositos:
            rendimento += dep * (self._taxa_mensal / 100.0)
        self._saldo += rendimento

    def __str__(self):
        return f"ContaPoupanca: saldo={self._saldo}, taxa={self._taxa_mensal}, depositos={self._depositos}"


class RendaFixa(ContaInvestimento):
    def __init__(self, rendimento: float, prazo_saque_str: str, valor_inicial: float):
        super().__init__(valor_inicial)
        self._rendimento = float(rendimento)
        self._prazo_saque = datetime.strptime(prazo_saque_str, "%d/%m/%Y")

    def sacar(self, v: float):
        if datetime.now() <= self._prazo_saque:
            raise ValueError("Prazo de saque não atingido.")
        super().sacar(v)

    def atualizar(self):
        self._saldo += self._saldo * (self._rendimento / 100.0)

    def __str__(self):
        return f"RendaFixa: saldo={self._saldo}, rendimento={self._rendimento}, prazo={self._prazo_saque.strftime('%d/%m/%Y')}"


class Criptomoeda(ContaInvestimento):
    def __init__(self, cotacao_inicial: float):
        super().__init__(0.0)
        self.cotacao = float(cotacao_inicial)
        self._quantidade = 0.0

    def atualizar(self):
        self._saldo = self._quantidade * self.cotacao

    def comprar(self, quantidade: float):
        self._quantidade += float(quantidade)
        self.atualizar()

    def vender(self, quantidade: float) -> float:
        if quantidade > self._quantidade:
            raise ValueError("Quantidade insuficiente.")
        self._quantidade -= float(quantidade)
        valor = quantidade * self.cotacao
        self.atualizar()
        return valor

    def __str__(self):
        return f"Criptomoeda: saldo={self._saldo}, cotacao={self.cotacao}, quantidade={self._quantidade}"
