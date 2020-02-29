def seriessum(xl):
    sum=0
    for x in range(1,xl+1):
        sum=sum+(x/2**x)
        print(sum)
seriessum(10)
