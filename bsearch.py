def bsearch(seq,v):
    l = 0
    r = len(seq)-1
    mid = 0
    
    while l<=r:
        mid = (l+r)//2
        if seq[mid]==v:
            return True
        elif seq[mid]<v:
            l = mid+1
        elif seq[mid]>v:
            r = mid-1
        
    
    return False

print(bsearch([1,5,65,77,88,99],99))
