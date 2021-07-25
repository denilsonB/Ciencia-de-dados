from scipy . stats import shapiro
import numpy as np

data = [15,20,15,3,2]
stat, pvalue = shapiro(data)

print(stat, pvalue)

if(pvalue > 0.05):
    print("Fora da distribuição normal")
else:
    print("Dados dentro do normal")
