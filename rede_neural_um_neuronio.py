input = 1
output_desire = 0

input_weight = 0.5

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

sum = input * input_weight

output = activation(sum)
