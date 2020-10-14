
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