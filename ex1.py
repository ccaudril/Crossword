from numpy import array as a

# searches in the dictionnary every word with a certain length
def search_word(length):
    l = list()
    with open("diccionari_CB_v2.txt","r") as file:
        i=0
        j=0
        while j<=length(file):
            if length(file[j]==length):
                l[i]=file
            i+=1
    return l

# creates a matrix starting from the crossword
def create_matrix():
    tab = a.array([])
    with open("crossword_CB_v2.txt","r") as file:
        i=0
        j=0
        for element in file:
            tab[i][j] = element[i][j]
    return tab

# finds longest word that has to be guessed
def find_word(matrix):
    dim = matrix.shape
    m = str(dim[0])     # number of rows
    n = str(dim[1])     # number of columns
    length = 0          # to store 
    for i in range (0,m):
    for j in range (0,n):

    # begins with horizontal words
        if matrix[i][j]=='#':
            
            if i<m:
                i++
            else:
                j++

        else: # if matrix[i][j]==0


        elif i=m && j<n:
            i=0
            j+=1
        elif i=m && j=n:

        elif matrix[i][j]==0 && i<m:
            length+=1
            

    
