from hashlib import sha256
from typing import Text
import random
import string
hashrate=0
count=0
import time
start=time.time()
while True:
    count+=1
    if(time.time()-start>60):
        hashrate=count
        count=0
        print("hashrate: ",hashrate)
        start=time.time()
    #N es el numero de texto random
    N=20
    Text=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(N))
    hash = sha256(Text.encode("utf-8")).hexdigest()
    isvalid=True
    #prefix of "0"
    for inde in range(7):
        if(hash[inde]!="0"):
            isvalid=False
    if(isvalid):
        print("Text: ",Text," hash: ",hash)
