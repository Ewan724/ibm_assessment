N = int(input())
ava_size = input().split(' ')
M = int(input())
req_size = input().split(' ')
ava_size_arr = []
req_size_arr = []
for i in ava_size:
    if 'S' in i:
        ava_size_arr.append((len(i) - 1) * -1)
    elif i == 'M':
        ava_size_arr.append(0)
    else:
        ava_size_arr.append((len(i) - 1))
for i in req_size:
    if 'S' in i:
        req_size_arr.append((len(i) - 1) * -1)
    elif i == 'M':
        req_size_arr.append(0)
    else:
        req_size_arr.append((len(i) - 1))
ava_size_arr.sort()
req_size_arr.sort()
can_fulfill = True
for i in range(M):
    if ava_size_arr[-1 * (i + 1)] < req_size_arr[-1 * (i + 1)]:
        can_fulfill = False
        break
if can_fulfill == True:
    print('Yes')
else:
    print('No')
