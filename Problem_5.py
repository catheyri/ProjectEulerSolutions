def mult():
    for i in range(1, 20*19*18*17*16*15*14*13*12*11):
        for j in range(11,20):
            if ((i*20)%j) == 0:
                if j == 19:
                    return(i*20)
            else: break

print(mult())
