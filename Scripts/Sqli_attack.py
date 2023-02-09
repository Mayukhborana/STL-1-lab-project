import os
import time
n=60
while n:
    os.system("curl http://localhost:8880?name=Alexander; USE webappdb; INSERT INTO greetings ( id, name, greeting ) VALUES ( 99, 'Vladimir', 'Hi' ); SELECT greeting FROM webappdb.greetings WHERE name='Alexander'; " )
    time.sleep(5) #### delay/sleep for 5 sec
    n=n-1 
      