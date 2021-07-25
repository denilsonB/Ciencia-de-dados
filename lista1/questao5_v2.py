import matplotlib.pyplot as plt
import numpy as np
x = np.arange(5)
numeros = [15,20,15,3,2]	
plt.bar(x,numeros)
plt.xticks(x,['20-30','30-40','40-50','50-60','60-70'])
plt.xlabel('Idade')
plt.ylabel('Frequencia')
plt.title("Histograma")
plt.show()
