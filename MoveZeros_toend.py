l=[1,1,0, 3,0, 12,0,0]
def move(l):
    #0,1,0,3,12
    nonzero_index=-1
    for i in range(len(l)):
        if(l[i]>0):
           nonzero_index+=1
           l[nonzero_index],l[i]=l[i],l[nonzero_index]
    print(l)
  
move(l)
