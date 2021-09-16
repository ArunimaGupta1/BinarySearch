def bsearch(seq,v,l,r):
    if r-l==0:
        return False
    mid = (l+r)//2
    if v==seq[mid]:
        return True
    elif v<seq[mid]:
        return(bsearch(seq,v,l,mid))
    elif v>seq[mid]:
        return(bsearch(seq,v,mid+1,r))

print(bsearch([1,2,3,5,9],2,0,5))
