a = str(input());count = 0;i = 0
while i < len(a):
    if a[i:i+2] == 'c=':
        count += 1;a = a[:i] + ' ' + a[i+2:];i += 1
    elif a[i:i+2] == 'c-':
        count += 1;a = a[:i] + ' ' + a[i+2:];i += 1
    elif a[i:i+3] == 'dz=':
        count += 1;a = a[:i] + ' ' + a[i+3:];i += 1
    elif a[i:i+2] == 'd-':
        count += 1;a = a[:i] + ' ' + a[i+2:]; i += 1
    elif a[i:i+2] == 'lj':
        count += 1;a = a[:i] + ' ' + a[i+2:];i += 1
    elif a[i:i+2] == 'nj':
        count += 1;a = a[:i] + ' ' + a[i+2:];i += 1
    elif a[i:i+2] == 's=':
        count += 1;a = a[:i] + ' ' + a[i+2:]; i += 1
    elif a[i:i+2] == 'z=':
        count += 1;a = a[:i] + ' ' + a[i+2:];i += 1
    else:
        i += 1
new_string = ''.join(a.split())
print(count + len(new_string))