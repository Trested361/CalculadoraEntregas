print("=== Calculadora de Entregas Lorenzon ===")

entrega = int(input("Quantas entregas você fez hoje? "))
entrega4 = int(input(f"Dessas {entrega} entregas, quantas foram de menos de 3km? "))
entrega6 = int(input(f"Dessas {entrega} entregas, quantas foram de mais de 3km? "))

calc4 = entrega4 * 4
calc6 = entrega6 * 6
calcent = calc4 + calc6
calctotal = calcent + 60

print("Perfeito Duda. Vamos aos calculos...")
print(f"Voce realizou {entrega4} entregas de -3km, que totalizou R${calc4}")
print(f"Você realizou {entrega6} entregas de +3km, que totalizou R${calc6}")
print(f"O valor total do seu dia foi de R${calctotal}")