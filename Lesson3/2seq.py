separs = [',','/',';'] 
st = input(f"Введите набор цифр, разделенных одним из символов {separs}: ")
for separ in separs :
    if(st.find(separ)>0):
        break;  #TODO: check - if there are another separators too

lst= st.split(sep=separ)
#print (lst, type(lst))
lset = set() 
for  l in lst:
    if(l.isdigit()):
        lset.add(int(l))
print (lset) 

