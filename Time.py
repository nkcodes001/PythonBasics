import time
initial=time.time()
print(initial)
k=0
while(k<54):
    print("This is NK")
    time.sleep(2)
    k=k+1
    
print("while loop Runs in ", time.time()-initial)

initial2=time.time()


for i in range(45):
    print("NKLZ")
print("For looop ran in ", time.time()-initial2)    

    
localtime=time.asctime(time.localtime(time.time()))
print("Local time: ",localtime)
