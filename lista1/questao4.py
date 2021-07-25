import statistics

v1=[15,10,10,15,5]#quantidade de pessoas com determinada altura
v2=[15,20,15,3,2]#quantidade de pessoas com determinada altura


mediav1 = statistics.mean(v1)
mediav2 = statistics.mean(v2)


medianav1 = statistics.median(v1)
medianav2 = statistics.median(v2)

print("mediana v1: ",medianav1)
print("mediana v2: ",medianav2)
print("=====")
print("media v1: ",mediav1)
print("media v2: ",mediav2)

print(medianav1<mediav1)#4.a
print(medianav2>mediav2)#4.b
