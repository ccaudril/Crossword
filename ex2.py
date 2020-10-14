#!/usr/bin/python

# Function: readCrossword
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

# Function: calculate_constraints
# ------------------------------------------------------------------------------
# Add to the current slot new constraints due to the new word
#
#   crossword: matrix representation of the crossword
#   word: new word in the crossword => brings new constraints
#   slots : slot list for the entire crossword
#   slot: slot corresponding to the new word
#
#   returns slots with the new constraints in addition
#
def calculate_constraints(crossword, word, slots, slot):
    i = slot[1]
    j = slot[2]
    n = slot[3]
    if slot[0] == "V":
        while i < slot[1]+n:
            for s in slots:
                if s[0]=='H' and s[1]==i and s[2]<=j and j<=s[2]+s[3]:  # means that both words cross
                    letter_constraint = crossword[i][j]
                    position_constraint = j-s[2]
                    s.append([position_constraint,letter_constraint])
            i += 1
    else:
        while j < slot[2]+n:
            for s in slots:
                if s[0]=='V' and s[1]<=i and i<=s[1]+s[3] and s[2]==j: # means that both words cross
                    letter_constraint = crossword[i][j]
                    position_constraint = i-s[1]
                    s.append([position_constraint,letter_constraint])
            j += 1
    return slots


# Function: crossing_word
# ------------------------------------------------------------------------------
# Giving a slot, finds all other slots that cross it
#
#   crossword: matrix representation of the crossword
#   slots : slot list for the entire crossword
#   slot: slot for which we want to find crossing words
#
#   returns a slot_list with every slot crossing our inital slot
#
def crossing_word(slot, crossword, slots):
    i = slot[1]
    j = slot[2]
    n = slot[3]
    slot_list = []
    if slot[0] == "V":
        while i < slot[1]+n:
            for s in slots:
                if s[0]=='H' and s[1]==i and s[2]<=j and j<=s[2]+s[3]:  # means that both words cross
                    slot_list.append(s)
            i += 1
    else:
        while j < slot[2]+n:
            for s in slots:
                if s[0]=='V' and s[1]<=i and i<=s[1]+s[3] and s[2]==j: # means that both words cross
                    slot_list.append(s)
            j += 1
    return slot_list    


# Function: crossword_forward_checking
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
def crossword_forward_checking(slots, m, n, dictionary, crossword):

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

    for slot1 in slots:
        for word1 in dictionary[slot1[3]-2]:
            if satisfies_constraint(word1, slot1[4::]):
                crossword2 = write_word(crossword, word1, slot1)
                print("\n5 - slot:",slot1, "word:", word1, "slots:")
                for sloti in slots:
                    print(sloti)
                slots = calculate_constraints(crossword2, word1, slots, slot1)
                print("\n 6 - slot:",slot1, "word:", word1, "slots:")
                for sloti in slots:
                    print(sloti)

                # taking this couple <slot1,word1>, does it still exist words for the slots that will be constrained ?
                slot_list = crossing_word(slot1,crossword,slots)
                for slot2 in slot_list:
                    for word2 in dictionary[slot2[3]-2]:
                        if satisfies_constraint(word2,slot2[4::]):
                            

                            sol = crossword_forward_checking(slots[1::],m,n,dictionary,crossword2)
                            if sol != []:
                                return sol
    return []




# Function: main
# ------------------------------------------------------------------------------
#
def main():

    #while()
    print("Reading crossword...")
    crossword, n, m = readCrossword()

    print("Calculating slots...")
    slots, lenghts = calculateSlots(crossword, n, m)

    print("Reading dictionary")
    dictionary = readDictionary(lenghts)

    print("Calculating solution...")
    solution = crossword_forward_checking(slots, m, n, dictionary, crossword)

    print("Solution:")
    print(solution)

if __name__ == "__main__":
    main()    


    

