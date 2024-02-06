def histogram(list):
    o = []
    for i in list:
        o.append('*' * i)
    print(*o)
        
    
histogram([4,9,7]) 