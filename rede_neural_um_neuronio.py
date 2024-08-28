#importando pacotes necessários
import math

input = 1
output_desire = 0

input_weight = 0.1

learning_rate = 0.01

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print("entrada", input, "desejado", output_desire)

erro = math.inf

iteration = 0

while not erro == 0:
    sum = input * input_weight

    output = activation(sum)

    print("saida", output)

    erro = output_desire - output

    print(erro)

    if not erro == 0:
        input_weight = input_weight + learning_rate * input * erro

    iteration += 1

    print("A rede demorou", iteration, "vezes para aprender")

print("A rede aprendeu!!")
print("o peso é", input_weight)