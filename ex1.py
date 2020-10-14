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
            

    


#!/usr/bin/python

# Function: function_name
# ------------------------------------------------------------------------------
# Function that reads a file containing a crossword and stores it in a matrix
#
#   returns:
#       crossword = the matrix representation of the crossword
#       i = vertical size of the crossword
#       j = horizontal size of the crossword
#
def readCrossword():
    file = open("crossword_CB_v2.txt", "r") # Open the file
    i = 0
    j = 0
    crossword = []
    for line in file: # For every line in the file
        temp_line = []
        j = 0
        for word in line.split(): # For every caracter in the file
            if word == '#': # If position is blank or filled
                temp_line.append(int(-1))
            else:
                temp_line.append(int(0))
            j +=1
        crossword.append(temp_line) # Add calculated line to crossword
        i +=1
    return crossword, i, j

# Function: readDictionary
# ------------------------------------------------------------------------------
# Stores the list of words of a file onto a dictionary indexed by the size of
# the word
#
#   returns: a list of the words in the file indexed by size
#
def readDictionary(lenghts):
    file = open("diccionari_CB_v2.txt", "r") # Open the file
    word_list = [] # List with all the words from the dictionary
    max_len = 1

    for line in file:
        if (len(line[:-1]) in lenghts):
            word_list.append(line[:-1]) # Add word without the '\n'
            if len(line) > max_len: # Calculate the longest words length
                max_len = len(line)

    dictionary = [None] * (max_len-2) # Create empy dictionary

    for word in word_list:
        if dictionary[len(word)-2] == None: # If position is empty
            dictionary[len(word)-2] = [word] # Add new list with first word
        else:
            dictionary[len(word)-2].append(word) # Append word to list
    return dictionary


# Function: horizontalBeginning
# ------------------------------------------------------------------------------
# Calculates if a given position in the crossword is the beginning of a
# horizontal word
#
#   crossword: crossword whose position will be calculated if it's the beginning
#              of a horizontal word
#   i: vertical coordinate of the position
#   j: horizontal coordinate of the position
#   m: horizontal size of the crossword
#
#   returns: True if position is the beginning of a horizontal word.
#            False otherwise
#
def horizontalBeginning(crossword, i, j, m):
    # Possible two situations:
    #   ///[ ][ ] --> nothing-blank-blank
    #   [#][ ][ ] --> filled-blank-blank
    if (j == 0 and crossword[i][j+1] == 0) or (j < m-1 and crossword[i][j+1] == 0 and crossword[i][j-1] == -1 ):
        return True
    else:
        return False

# Function: verticalBeginning
# ------------------------------------------------------------------------------
# Calculates if a given position in the crossword is the beginning of a vertical
# word
#   crossword: crossword whose position will be calculated if it's the beginning
#              of a vertical word
#   i: vertical coordinate of the position
#   j: horizontal coordinate of the position
#   n: vertical size of the crossword
#
#   returns: True if position is the beginning of a vertical word.
#            False otherwise
#
def verticalBeginning(crossword, i, j, n):
    # Possible two situations:
    #   ///
    #   [ ] --> nothing-blank-blank
    #   [ ]
    #
    #   [#]
    #   [ ] --> filled-blank-blank
    #   [ ]
    if (i == 0 and crossword[i+1][j] == 0) or (i < n-1 and crossword[i+1][j] == 0 and crossword[i-1][j] == -1 ):
        return True
    else:
        return False

# Function: calculateLengthHorizontal
# ------------------------------------------------------------------------------
# Given a horizontal slot beginnin, calculates it's size
#
#   crossword: crossword whose slots' size will be calculated
#   i: vertical coordinate of the slot
#   j: horizontal coordinate of the slot
#   m: horizontal size of the crossword
#
#   returns: length of the slot
#
def calculateLengthHorizontal(crossword, i, j, m):
    length = 1
    while (j < m-1) and (crossword[i][j+1] != -1):
        length += 1
        j += 1
    return length

# Function: calculateLengthVertical
# ------------------------------------------------------------------------------
# Given a vertical slot beginnin, calculates it's size
#
#   crossword: crossword whose slots' size will be calculated
#   i: vertical coordinate of the slot
#   j: horizontal coordinate of the slot
#   n: vertical size of the crossword
#
#   returns: length of the slot
#
def calculateLengthVertical(crossword, i, j, n):
    length = 1
    while (i < n-1) and (crossword[i+1][j] != -1):
        length += 1
        i += 1

    return length

# Function: calculateSlots
# ------------------------------------------------------------------------------
# Given a crossword, calculates all the beginning of words, their orientation,
# position and length
#
#   crossword: matrix representation of a crossword whose slots will be calculated
#   n: vertical size of the crossword
#   m: horizontal size of the crossword
#
#   returns: list with the slots' information
#
def calculateSlots(crossword, n, m):
    slots = []
    lenghts = []
    for i in range(n):
        for j in range(m):
            if crossword[i][j] != -1:
                if horizontalBeginning(crossword, i, j, m):
                    lenght = calculateLengthHorizontal(crossword, i, j, m)
                    slots.append(['H', i, j, lenght])
                    if lenght not in lenghts:
                        lenghts.append(lenght)
                if verticalBeginning(crossword, i, j, n):
                    lenght = calculateLengthVertical(crossword, i, j, n)
                    slots.append(['V', i, j, lenght])
                    if lenght not in lenghts:
                        lenghts.append(lenght)



    # Order the slots list
    slots.sort(key = lambda x: x[3], reverse=True)

    return slots, lenghts

# Function: main
# ------------------------------------------------------------------------------
# Executes the main program
#
#def main():
#    crossword, n, m = readCrossword()
#    slots = calculateSlots(crossword, n, m)
#    dictionary = readDictionary()

#if __name__ == "__main__":
#    main()



# Function: max_word
# ------------------------------------------------------------------------------
# Find the first word with maximal length in the crossword
#
#   slots: list with the slots' information
#   m: vertical size of the crossword
#   n: horizontal size of the crossword
#
#   returns: word with maximal length (if there is many, returns the first of the slots' list)
#       => ['V'/'H' , row, column, length]
#
def max_word(slots, m, n):
    i=0     # i : row index in the slots' list
    max=0   # maximum word length founded in the crossword
    while i < len(slots):
        if(slots[i][3]>max):    # slots[i][3] = length
            max=slots[i][3]
            position=slots[i]
    return position



# Function: find_constraint
# ------------------------------------------------------------------------------
# Finds if there is any constraint for a word
# (a constraint is letter already founded whiwh has to be in this word)
#
#   word : given word in the slots' list
#   solution : partial solution of the crossword
#
#   constraint_list : list with all constraints of letters for one slot
#       => [position, letter]
#
def find_constraint(word,solution):
    i=word[1]
    j=word[2]
    length=word[3]
    constraint_list = []
    if word[0]=='V':
        while i <= word[1]+length:
            if solution[i][j] != '0':
                constraint_list = constraint_list + [i,solution[i][j]]
            i+=1

    else :      # if word[0]=='H'
        while j <= word[2]+length:
            if solution[i][j] != '0':
                constraint_list = constraint_list + [j,solution[i][j]]
            j+=1

    return constraint_list



# Function: find_word
# ------------------------------------------------------------------------------
# Searchs in the dictionary if there is a word with a length and constraints
#
#   length: length of the searched word
#   constraint_list: letter constraint in the searched word
#   dictionary: result of the function 'readDictionary'
#
#   returns 0 if there isn't such a word in the dictionary
#   returns a solution for the searched word if it exists
#
def find_word(length, constraint_list, dictionary):
    word=' '
    for word in dictionary :
        if len(word)==length:
            i=0
            while i<=len(constraint_list):
                letter = constraint_list[i][1]
                position = constraint_list[i][0]
                if word[position] != letter:
                    break
                else:
                    i+=1
    if word==' ':
        return 0
    else :
        return word


# Function: satisfies_constraint
# ------------------------------------------------------------------------------
# Calculates if a given word satisfies a list of constraints
#
#   word: word that must satisfie the constraints
#   constraints: list of constraint tuples
#
#   returns True if th word satisfies the constraints, False icc.
#
def satisfies_constraint(word, constraints):
    for tuple in constraints:
        if word[tuple[0]] != tuple[1]:
            return False
    return True


# Function: write_word
# ------------------------------------------------------------------------------
# Writes the given word in a concrete slots of the crossword
#
#   crossword: matrix representation of the crossword
#   word: word that will be written in the crossword
#   slot: slot information about where he word should be written
#
#   returns modfied version of the crossword with the given word written
#
def write_word(crossword, word, slot):
    i = slot[1]
    j = slot[2]
    k = 0

    if slot[0] == "V":
        while k < slot[3]:
            crossword[i+k][j] = word[k]
            k+=1
    else:
        while k < slot[3]:
            crossword[i][j+k] = word[k]
            k+=1
    return crossword


def calculate_constraints(crossword, word, slots, slot):
    i = slot[1]
    j = slot[2]
    n = len(crossword[0])
    count = 0
    k = 0

    if slot[0] == "V":
        while k < slot[3]:
            if crossword[i+k][j+(0 if j>n else 1)] == 0 or crossword[i+k][j-(1 if j>0 else 0)] == 0:
                l = j
                #print("l1:",l)
                while l > 0 and crossword[i+k][l-1] == 0:
                    l-=1
                    #print("l2:",l)
                count = 0
                for s in slots:
                    if s[1]==i+k and s[2]==l:
                        #print("slots:", slots)
                        #print("j-l: ", j, "-", l, "=", j-l)
                        #print("crossword[",i,"][",j,"]: ", crossword[i][j])
                        slots[count].append([(j-l),crossword[i][j]])
                        #print("slots new:", slots)
                        break
                    count+=1
            k+=1
    else:
        #print("k < slot[3]:",k,"<",slot[3])
        while k < slot[3]:
            #print("crossword[",i+(0 if i>n else 1),"][",j+k,"] --- ","crossword[",i-(1 if i>0 else 0),"][",j+k,"]")

            if crossword[i+(0 if i>n else 1)][j+k] == 0 or crossword[i-(1 if i>0 else 0)][j+k] == 0:
                l = i
                #print("l1:",l)
                while l>0 and crossword[i-l][j+k] == 0:
                    l-=1
                    #print("l2:",l)
                count = 0
                for s in slots:
                    if s[1]==l and s[2]==j+k:
                        #print("slots:", slots)
                        #print("i-l: ", i, "-", l, "=", i-l)
                        #print("crossword[",i,"][",j,"]: ", crossword[i][j])
                        #print("slots new:", slots)
                        slots[count].append([(i-l),crossword[i][j]])
                        break
                    count+=1
            k += 1

    return slots


# Function: crossword_solution
# ------------------------------------------------------------------------------
# Gives a final solution for the given crossword
#
#   slots: list with the slots' information
#   m: vertical size of the crossword
#   n: horizontal size of the crossword
#   dictionary: given dictionary
#   crossword: given crossword
#
#   returns a crossword as final solution
#
def crossword_backtracking(slots, m, n, dictionary, crossword):

    print("\n----------------------------------------------------------\ncrossword:")
    for line in crossword:
        for letter in line:
            if letter == -1:
                print("#", end='')
                print(" ", end='')
            else:
                print(letter, end='')
                print(" ", end='')
        print()

    print("\nslots:")
    for sloti in slots:
        print(sloti)

    if slots == []:
        return crossword
    for slot in slots:
        for word in dictionary[slot[3]-2]:
            if satisfies_constraint(word, slot[4::]):
                crossword = write_word(crossword, word, slot)
                #print("\n5 - slot:",slot, "word:", word, "slots:")
                #for sloti in slots:
                #    print(sloti)
                slots = calculate_constraints(crossword, word, slots, slot)
                #print("\n6 - slot:",slot, "word:", word, "slots:")
                #for sloti in slots:
                #    print(sloti)
                sol = crossword_backtracking(slots[1::], m, n, dictionary, crossword)
                if sol != []:
                    return sol
    return []


def main():
    print("Reading crossword...")
    crossword, n, m = readCrossword()

    print("Calculating slots...")
    slots, lenghts = calculateSlots(crossword, n, m)

    print("Reading dictionary")
    dictionary = readDictionary(lenghts)

    print("Calculating solution...")
    solution = crossword_backtracking(slots, m, n, dictionary, crossword)

    print("Solution:")
    print(solution)

if __name__ == "__main__":
    main()
