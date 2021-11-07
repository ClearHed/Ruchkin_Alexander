
s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"



def meet(s):
    # for x in s:
        # NewS = s.upper().split(';')
        # x.split(':')
        # return NewS
        
    NewS = sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';'))
    return ''.join(NewS)


print(meet(s))