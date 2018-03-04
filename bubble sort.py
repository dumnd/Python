alist = [8,2,10,656,7777,0,-1,0.56,10000,678,7438,30472932,24762]


for num in range(len(alist)-1,0,-1):
    for i in range(num):
        if alist[i]>alist[i+1]:
            store = alist[i]
            alist[i] = alist[i+1]
            alist[i+1] = store

print(alist)
