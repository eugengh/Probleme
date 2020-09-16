#Problema 1
print("Problema 1:")
print("struguri            "+"100           "+"kg")
print("Mere               "+" 10            "+"tone")
print("Cartofi             "+"250           "+"kg")
print("Varza               "+"1000          "+"q")
#Problema 2
print("Problema 2:")
print("a=5")
print("b=2")
a=5
b=2
print("a+b="+str(a+b))
print("a-b="+str(a-b))
print("a//b="+str(a//b))
print("a % b="+str(a%b))
print("a * b="+str(a*b))
print("a ** b="+str(a**b))
#Problema 3
print("Problema 3:")
#latura = l
l=7
P=12*l
a=6*(l**2)
v=l**3
print("Latura cubului are o lungime de " +str(l)+" cm")
print("Perimentrul suprafetei intregi este: "+str(P)+ " cm")
print("Aria cubului este : "+str(a)+" cm^2")
print("Volumul cubului este : "+str(a)+" cm^3")
#Problema 4
print("Problema 4:")
n=5
cm= n*100
ml = n*1000000
l= n*12
s=n*52
z=n*365
print("5 m = "+str(cm) +" cm")
print("5kg = " +str(ml)+" ml")
print("5ani = " +str(l)+" luni" + " sau "+ str(s)+ " saptamani" + " sau " + str(z)+ " zile")
#Problema 5
print("Problema 5:")
print("x    "+ " y         "+ " x or y  " + " x and y  " + " not x     " + "not y ")
x=True
y=False
print("True "+ " False " ,(x or y) , (x and y ) , (not x) , (not y), sep="     ")
x=False
y=True
print("False "+"True " ,(" "+str(x or y)) , (x and y ) , (not x) , (" "+str(not y)), sep="     ")
x=False
y=False
print("False "+"False" ,("  "+str(x or y)) , (x and y ) , (" "+str(not x)) , ("  "+str(not y)), sep="    ")
x=True
y=True
print("True "+" True" ,("   "+str(x or y)) , (" "+str(x and y )) , ("  "+str(not x)) , (" "+str(not y)), sep="    ")
#Problema 6
print("Problema 6:")
print("Numarul este 5321")
n=5321
print("Ultima cifra a lui n este: " + str(n%10))
print("Penultima cifra a lui n este " + str((n%100)//10))
print("Restul impartirii lui n la 9 este "+ str(n%9))
print("Catul impartirii lui n la 9 este "+ str(n//9))
a=(n%10000)//1000
b=(n%1000)//100
c= (n%100)//10
d= n%10
print("Suma cifrelor lui n este " + str(a+b+c+d))