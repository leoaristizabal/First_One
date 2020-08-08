friends = ["Dariophone", "Karencion", "Rault", "Fran", "Mel"]
friends[2]= "Raoolt"
print(friends[0:3])


lucky_numbers = [4,8,15,16,23,42]
colors = ["Green", "Red", "Blue", "White","White","White", "yellow"]
colors2 = ["Green", "Red", "Blue"]
colors.extend(lucky_numbers) #juntar dos listas
colors.append("Purple") #Agregar un solo elemento al final de la lista
colors.insert(1,"Pink") # insertar un elemento a una posicion especifica segun el index
colors.remove("Red") #Remover un solo elemento
colors.pop() #Eliminar ultimo elemento de la lista directamente
print(colors.index("Blue")) #Indica la posicion de un elemento
print(colors.count("White")) #Contar cuantas veces esta un elemento
colors2.sort() #Ordenar lista en orden ascendent eo alfabetico
print(colors2)
colors2.reverse() # Devolver elemmentos, escribirlos en orden contrario
print(colors2)
colors2 = colors.copy() #copiar elementos de otra lista
print(colors2)
print(colors)


