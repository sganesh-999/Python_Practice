s = "abbc"
goal = "abbc"

def buddyStrings(s,goal):
    # any single pair is swapped it should create new string 
    if(len(s)!=len(goal)):
        print('1---')
        return False
    if s == goal:
        print('2---')
        return len(set(s)) < len(s)
    diff=[(a,b) for a,b in zip(s,goal) if a != b]
    return len(diff)==2 and  diff[0]==diff[1][::-1]

print(buddyStrings(s, goal))
