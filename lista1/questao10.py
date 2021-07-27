from sklearn.datasets import load_iris#dataset da iris
from sklearn.model_selection import train_test_split #Separar os dados
from sklearn.model_selection import cross_val_score #F-measure
from sklearn.naive_bayes import GaussianNB #Naive Bayes
from sklearn import neighbors #K-NN
from sklearn import metrics #calcula os testes

n_neighbors = 3 #numero de vizinhos do K-NN

dadosIris, irisClasses = load_iris(return_X_y = True)

gaussNB = GaussianNB()#Instanciando o Naive Bayes Gaussiano
knn = neighbors.KNeighborsClassifier(n_neighbors) #Instanciando Naive-Bayes

#funcao para calcular o cross validation
scoresGNB = cross_val_score(gaussNB, dadosIris, irisClasses, cv=5, scoring = 'f1_weighted')#croos validation do NBG
scoresKNN = cross_val_score(knn, dadosIris, irisClasses, cv=5, scoring = 'f1_weighted')#cross validation do KNN



cont = 1
print("Resultados K-NN: ")
for results in scoresKNN:
    print(f'Teste {cont}: {results:3f}')
    cont = cont+1   

cont = 1
print("\nResultados Naive Bayes: ")
for results in scoresGNB:
    print(f'Teste {cont}: {results:3f}')
    cont = cont+1


