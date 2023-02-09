import os
import time
#####################~~~~~Script for Collection of Benign data~~~~~~~~#####################

#################################Ftp data collection##################
n=120 #for 10 mintute
while n:
    os.system("curl ftp://10.0.2.9")
    time.sleep(5) # delay/sleep for 5 sec
    n=n-1 
##################################Apache2 Web server data#########################

m=120 #for 10 mintute
while m:
    os.system("curl http://10.0.2.9")
    time.sleep(5)  # delay/sleep for 5 sec
    m=m-1

############################## XSS data ##############################
n=60 ############for 5 mintute
while n:
    os.system("curl http://10.0.2.9:8880?name=Mayukh " )
    time.sleep(5) #### delay/sleep for 5 sec
    n=n-1 

##########################################Sql data ###############################
n=60  ############for 5 mintute
while n:
    os.system("curl http://10.0.2.9:8880?name=Alexander" )
    time.sleep(5) #### delay/sleep for 5 sec
    n=n-1 
