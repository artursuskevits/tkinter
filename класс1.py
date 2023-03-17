import time
import datetime
 
h = 0
m = 0
s =30 
   
total_seconds = 30
 
    
while total_seconds > 0:
 
    #
    timer = datetime.timedelta(seconds = total_seconds)
        
        
    print(timer, end="\r")
 
       
    time.sleep(1)
 
        
    total_seconds -= 1





