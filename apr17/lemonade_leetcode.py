def lemonadeChange(self, b):
    """
    :type bills: List[int]
    :rtype: bool
    """
    p5 = 0
    p10 = 0
    for i in b:
        if i == 5:
            p5 = p5+1
        elif i == 10:
            if p5 > 0:
                p10 = p10+1
                p5 = p5-1
            else:
                return False
        elif i == 20 and p5 > 0:
            if p10 > 0:
                p10 = p10-1
                p5 = p5-1
            elif p5 > 2:
                p5 = p5-3
            else:
                return False
        else:
            return False
    return True
