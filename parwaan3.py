import time
def timer(t):

  while t>0:
    m,s =divmod(t,60)
    h,m =divmod(m,60)

    time_left=str(h).zfill(2)+":"+ str(m).zfill(2) + ":"+ str(s).zfill(2)
    print(time_left + "\r", end="")
    time.sleep(1)
    t-=1

  print()
    
timer(120) # enter time in seconds for which you want to run the timer...