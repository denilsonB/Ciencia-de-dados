import matplotlib.pyplot as plt
import numpy as np

recebidos = [160,184,241,149,180,161,132,202,160,139,149,177]
processados = [160,184,237,148,181,150,123,156,126,104,124,140]
meses = ["janeiro","Fevereiro ","Março","Abril"," Maio","Junho","Julho", 
"Agosto","Setembro","Outubro","Novenbro","Dezembro"]

plt.plot(meses,recebidos,"gray",processados,"darkblue",linewidth=4)
plt.ylim(0,300)

titulo = "Volume de tickeds ao longo do tempo"

plt.xlabel("Meses",fontsize=15)
plt.ylabel("Numero de tickets",fontsize=15)
plt.title(titulo, fontsize=12, loc="left", pad=10)


fontRecebidos = {'family': 'arial',
        'color':  'gray',
        'weight': 'normal',
        'size': 16,
        }

plt.text('Dezembro',165,"Recebidos",fontdict=fontRecebidos)

fontProcessados = {'family': 'arial',
        'color':  'darkblue',
        'weight': 'normal',
        'size': 16,
        }

plt.text('Dezembro',130,"Processados",fontdict=fontProcessados)


for i in range(7,12):
    plt.annotate('%d'%recebidos[i],xy=(meses[i],recebidos[i]),xytext=(meses[i],recebidos[i]+5),color="black",fontsize=10)
    
for i in range(7,12):
    plt.annotate('%d'%processados[i],xy=(meses[i],processados[i]),xytext=(meses[i],processados[i]+5),color="black",fontsize=10)

plt.show()





















