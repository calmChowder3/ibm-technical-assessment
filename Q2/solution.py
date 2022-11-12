num_inputs = input()
input_list = []
for i in range(int(num_inputs)):
    codes = input().split(' ')
    input_list.append(codes)

errorCodes = []
for r in input_list:
    if r[1] == 'false':
        errorCodes.append(r[2])

if not len(errorCodes):
    print('Yes')
else:
    print('No')
    print(*errorCodes, sep=' ')
