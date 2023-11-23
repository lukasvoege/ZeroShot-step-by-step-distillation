from readability import Readability 

with open("fre_calc.txt", "r") as f:
    st = f.read()                    

r = Readability(st) 
print(r.flesch().score)