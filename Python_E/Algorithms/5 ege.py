def tas5(N):
    nbin = bin(N)[2:]
    if nbin[-1] == '0':
        nbin += nbin[-2:]
    else:
        nbin = '1' + nbin + '1'
    return int(nbin,2)

for n in range(4,200):
    if tas5(n) > 130:
        print(tas5(n))
