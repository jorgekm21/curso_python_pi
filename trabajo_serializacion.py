import pickle

""" lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres","wb") #WB es escritura binaria

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario) #Borra el archivo """

fichero=open("lista_nombres", "rb") #RB es lectura binaria

lista=pickle.load(fichero)

print(lista)