x = int(raw_input("please enter an integer: "))
if x < 0:
    x = 0
    print 'negative changed to zero'
elif x == 0:
    print 'zero'
elif x == 1:
    print 'Single'
else:
    print 'More'
