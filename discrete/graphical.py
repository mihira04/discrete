print('Please enter degree sequence separated by spaces.')
A=input().split()
print('The following sequence has been entered')
B=[int(n) for n in A]
print(B)
def graphical(sequence):
    m=len(sequence)
    sequence.sort(reverse=True)
    while m>1 and sequence[-1]>=0:
        k=sequence[0]
        if k+1>m:
            return False
        else:
            for i in range(1,k+1):
                sequence[i]=sequence[i]-1
        sequence[0]=sequence[-1]
        m=m-1
        sequence.sort(reverse=True)
    if sequence[-1]==0:
        return True
    else:
        return False

print(graphical(B))
