def computepay(h, r):
    if h<40 :
        pay=r*h
    else :
    	pay=40*r+(h-40)*r*1.5
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(int(hrs), float(rate))
print(p)