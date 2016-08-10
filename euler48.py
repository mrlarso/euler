def series(n):
    series_sum = 0
    for i in range(1,n+1):
        series_sum += i**i
    return series_sum

print str(series(1000))[-10:]
