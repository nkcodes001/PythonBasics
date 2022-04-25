a=9
b=18
c=sum((a,b))   #in built function!!!!!
print(c)


#for user defined function we use def keyword

def funn1():
    print("Hello ur in funn1") # none comes bcoz in pythgon calling a function can be printed multiple times and we neeed not type printb again and again
    
print(funn1())    

funn1()
funn1()
funn1()
funn1()

#functions with input

def func1(a,b):
    print("Sum of the input u gave was ",a+b)

def Avg(a,b):
    """This print Average of 2 Nos."""
    average=(a+b)/2
    print("average is ", average)
    return average;

func1(10,199)
Avg(10,15)
v=Avg(23,49)
print(v) #This will be printed iff we return avg in the function else it prints None!!,,,
print(Avg.__doc__)
