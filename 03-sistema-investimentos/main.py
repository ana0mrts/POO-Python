from investimentos import *

#Conta Poupanca com taxa mensal de 0.5%
poupanca = ContaPoupanca(0.5)
poupanca.depositar(1000)
poupanca.depositar(500)

#Conta RendaFixa com rendimento de 90.2%, 
#data limite para saque 01/06/2025 e valor 
#inicial de 5000 reais
cdb = RendaFixa(90.2, "01/06/2025", 5000)
lci = RendaFixa(88.9, "04/09/2026", 3000)
cdb.depositar(2000)
try:
  lci.sacar(3000)
except Exception as e:
  print(e)

#Biicoin com cotação inicial de 231.2 reais
bitcoin = Criptomoeda(231.2)
bitcoin.comprar(250)

investimentos = [poupanca, cdb, lci, bitcoin]
print("Meus investimentos")
for i in investimentos:
  print(i)

##saque de 200 da poupanca
poupanca.sacar(200)
##saque de 100 do cdb
cdb.sacar(100)
##alterada cotacao do bitcoin e vendido 40 bitcoins
bitcoin.cotacao = 500
print(f"Recebidos R$ {bitcoin.vender(40):.2f} da venda de bitcoins")

print("Atualizando e exibindo todos os investimentos")
for i in investimentos:
  i.atualizar()
  print(i)
