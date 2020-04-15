def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk)!=10:
        return False
    else:
        ver=0
        hor=0
        for i in walk:
            if i=='n':
                ver=ver+1
            elif i=='s':
                ver=ver-1
            elif i=='w':
                hor=hor-1
            else:
                hor=hor+1
        if ver==0 and hor==0:
            return True
        else:
            return False
    
    pass