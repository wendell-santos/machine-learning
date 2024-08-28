input = 1
output_desire = 0

input_weight = 0.5

learning_rate = 0.01

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print("entrada", input, "desejado", output_desire)
while not erro == 0:
    sum = input * input_weight

    output = activation(sum)

    print("saida", output)

    erro = output_desire - output

    print(erro)

    if not erro == 0:
        input_weight = input_weight + learning_rate * input * erro