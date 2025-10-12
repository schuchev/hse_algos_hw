def two_sum(arr,k):
    d={}
    for i in range(len(arr)):
        if k-arr[i] in d:
            return (d[k-arr[i]],i)
        d[arr[i]]=i

