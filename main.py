
"""
file=open("third.txt","a")

file.write("my name is shahzad\n")

file.close()


file=open("third.txt","r")

data=file.read()

print(data)


file.close()

file1=open("third.txt","r")
data1=file1.read()
print(data1)
file1.close()
file2=open("third.txt","w")
file2.write(" good read \n")
file2.close()
file3=open("first.txt","a")
file3.write("me with myself\n")
file3.close()


file4=open("third.txt","w")
data2=file4.write("nayyab\nbisma\nneha\nmehar\nsaba\n")
print(data2)
file4.close()
"""
"""""

with open("first.txt","a") as file6:
    file6.write("\nhello world\n")
    file6.write("\nhello world\n")
    file6.write("\nhello world\n")


with open("first.txt","r") as file5:
    da=file5.read()
    print(da)


"""

with open("first.txt","w") as file7:
    file7.write("BOOKS NAME:Read in 2025\n")
with open("first.txt","r") as file8:
    d=file8.read()
    print(d)
with open("first.txt","a") as file9:  
    file9.write("JKP by NIMRAH Ahmed \n")
    file9.write("JMTM by aasma rehman \n")
    file9.write("B3b by mehar \n")
    file9.write("BAB E DEHR by mehar\n")
    file9.write("NAmal by Nimrah Ahmed\n")
    file9.write("mala by Nimrah Ahmed\n")
    file9.write("musuf by Nimrah Ahmed\n")
    file9.write("bismil by mehar\n")
    file9.write("kahaf by  Raabia khan\n")
    file9.write('dairy by aasma rehman\n')
    
    
