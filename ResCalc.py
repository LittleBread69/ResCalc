
def ResCalc(arn: int, ard: int, minHeight: int, maxHeight: int):
    miPx = minHeight
    maPx = maxHeight
    
    n = miPx
    retpx = []
    while n <= maPx:
        for i in range(miPx, maPx):
            if(i % 2 == 1):
                n += 1
                pass
            elif (i * arn) % ard == 0:
                n += 1
                #print([i, int(i*(arn/ard))])
                retpx.append([i, int(i*(arn/ard))])
            else:
                n += 1
    #print(retpx)
    return retpx
#ResCalc(int(input()), int(input()), int(input()), int(input()))
