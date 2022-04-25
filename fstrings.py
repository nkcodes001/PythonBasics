# F strings
import math #bcoz we r using cos function

me = "Harry"
a1 =3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
a = f"this is {me} {a1} {math.cos(90)} {65*86}"
# time
print(a)
  
