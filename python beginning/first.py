a, c, b, end, love = '*', 1, 15, ' ', '***I*LOVE*U2***'
while c <=30:
    if c != 15:
        print(end*b+a*c)
    else:
        print(end*(int(b))+love)
    c+=2
    b-=1