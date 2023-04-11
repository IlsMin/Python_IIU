cnt = int(input("кол-во элементов цифрового списка ? "))
done =0
lst =[]
while(done<cnt):
    lst.append( int(input("введите цифру(0...9): ")))
    done+=1
lst.sort()
print(lst)
