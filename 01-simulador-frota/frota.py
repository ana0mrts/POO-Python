import random
from frota import Carro

if __name__ == "__main__":
c1 = Carro("R8", "Audi", "Preto", 0, False, 50.0, 10.0)
c2 = Carro("Supra MK4", "Toyota", "Prata", 0, False, 50.0, 10.0)

try:
try:
c1.desligar()
c2.desligar()
except Exception as e:
print(e)

c1.ligar()
c2.ligar()

while c1.odometro < 600 and c2.odometro < 600:
if not c1.motor_on and not c2.motor_on:
break

if c1.motor_on:
c1.acelerar(random.randint(1, 10), random.randint(1, 10))

if c1.odometro >= 600:
print(f"{c1.modelo} ganhou com {c1.odometro} KM e {c2.modelo} perdeu com {c2.odometro}Km!")
break

if c2.motor_on:
c2.acelerar(random.randint(1, 10), random.randint(1, 10))

if c2.odometro >= 600:
print(f"{c2.modelo} ganhou com {c2.odometro} KM e {c1.modelo} perdeu com {c1.odometro}Km!")
break

if c1.motor_on:
c1.desligar()
if c2.motor_on:
c2.desligar()

except Exception as e:
print(e)
