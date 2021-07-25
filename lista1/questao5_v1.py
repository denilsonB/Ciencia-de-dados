import matplotlib.pyplot as plt
import numpy as np
x = np.arange(5)
numeros = [15,10,10,15,5]	
plt.bar(x,numeros)
plt.xticks(x,['1.50-1.60','1.60-1.70','1.70-1.80','1.80-1.90','1.90-2.00'])
plt.xlabel('Altura')
plt.ylabel('Frequencia')
plt.title("Histograma")
plt.show()
