import os

in_1 = 0
in_0 = 0
data_input = []
data_low_out = []
data_high_out = []
out_1 = 0



for i in range(len(data_input)):
    out = 0.0004902 * data_input[i] + 0.0004902 * in_1 + 0.9608 * out_1
    in_1 = data_input[i]
    out_1 = out
    data_low_out [i] = out

in_1 = 0
in_0 = 0
out_1 = 0

for i in range(len(data_low_out)) :
    out = 5.982 * data_low_out[i] -5.982 * in_1 + 0.994 * out_1
    in_1 = data_low_out[i]
    out_1 = out
    data_high_out[i] = out

