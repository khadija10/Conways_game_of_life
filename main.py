import numpy

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

def compute_number_neighbors(paded_frame, index_line, index_column):
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules voisines vivantes.
    """
    #somme des voisins en ignorant la cellule centrale
    neighbors = paded_frame[index_line-1:index_line+2, index_column-1:index_column+2] #slicing sur les 8 voisins
    number_neighbors = numpy.sum(neighbors) - paded_frame[index_line, index_column] #enlever la centrale
    return number_neighbors

#print(compute_number_neighbors(frame, 2, 2))

def compute_next_frame(frame):
    """
    Cette fonction prend en entrée une frame et calcule la frame suivante
    à partir des règles du jeu de la vie
    """
    paded_frame = numpy.pad(frame, 1, mode="constant") # je vous offre le code pour le zéro padding c'est cadeau !

    #init un frame 
    new_frame = numpy.zeros_like(frame)
    """
    # Étape 1 : 2 boucles for imbriquées pour parcourir la matrice avec bordure (zero padding) element par element.
    Faites attention à l'index de début et d'arrêt ! (il s'agit de la matrice avec bordure)
    
    # L'étape 2 et 3 se font au cours de la même itération (attention à l'indentation !)
    
    # Étape 2 : Pour chacun des éléments, calculez le nombre de voisins.
    On fait appelle à la fonction (compute_number_neighbors)
    
    # Étape 3 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin) afin de voir
si il y a des modifications à faire.
    Si c'est le cas effectuez les modifications directement dans la matrices frame (Attention à l'indice
    utilisé ! )"""

    for index_line in range(1, paded_frame.shape[0] - 1): # 1 à m-1
        for index_column in range(1, paded_frame.shape[0] -1): #1 à n-1
            #Calculer le nombre de voisins vivants
            number_neighbors = compute_number_neighbors(paded_frame, index_line, index_column)
            #Appliquer le jeu de la vie
            if paded_frame[index_line, index_column] == 1 : # vivante
                if number_neighbors == 2 or number_neighbors == 3 : # reste vivante
                    new_frame[index_line - 1, index_column -1] = 1
            else:
                if number_neighbors == 3 : # devient vivante
                    new_frame[index_line - 1, index_column - 1] = 1

    return frame

while True:
    # boucle infini qui affiche toutes les frames successives (ctrl + c pour arrêter le script)
    print(frame)
    frame = compute_next_frame(frame)
