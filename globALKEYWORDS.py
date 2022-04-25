

l=10 # GLobal variable means any function can use
def func1(n):
    print(l)
    print(n,"I have printed")
    
func1("This is me")    
print(l)


def func2(n):
    l=6 #local
    m=3
   # l=l+43
    print(n,l,m)
    
func2("Print here with change in global variables")    

#print(m )-------> This will throw an error!!!!!!!!!!!

# as we can see that the l is not defined in func1 but we can use it!!!! sooo........Thats it


# global keywordf is used in order to change the global variables inside the function!!..we cant change global variable inside the function....so we use global key word to change
# global keyword goes alllllllllllllll the wayy to the top of the function!!!!


def func3():
    global l
    l=l+55
    print(l)
    
func3()    