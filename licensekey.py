s = '2-4A0r7-4k' 
# 24-A0R-74K
k = 3
def process(s,k):
    #split
     temp=list("".join(s.upper().split("-")))
     #reverse
     temp=temp[::-1]
     print('temp',temp)
     updated_str=list()
     #combine k charaters form list and join into str
     for i in range(0,len(temp),k):
         updated_str.append("".join(temp[i:i+k][::-1]))
     print('updated_str',updated_str)
     #reverse
     updated_str=updated_str[::-1]
     print('updated_str',updated_str)
     print("-".join(updated_str))
         
     
process(s,k)
