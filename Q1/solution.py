avai_len = input()
avai_sizes = input().split(' ')
req_len = input()
req_sizes = input().split(' ')

def keyFunc(i):
    tens = 10000
    if i[-1] == 'S':
        return tens - i.count('X')
    elif i[-1] == 'M':
        return tens * 2
    else:
        return tens * 3 + i.count('X')

req_sizes.sort(key=keyFunc, reverse=True)
avai_sizes.sort(key=keyFunc, reverse=True)

def determine(req, avai):
    for r in req:
        for a in avai:
            if(keyFunc(a) >= keyFunc(r)):
                avai = avai[1:]
                break
            else:
                return False
    return True

print('Yes' if determine(req_sizes, avai_sizes) else 'No')
