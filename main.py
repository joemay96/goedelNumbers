# This is the Main File of the geodelproject

separator = "11"
one = "01"
zero = "00"

#This Method calculates the goedelnumber of a given TM --> as Array
#TM has the following Structure:
#{
#   1. Zustandsmenge: [z0,z1,...,zn],
#   2. Eingabealphabet: [a1,a2,...,an],
#   3. Arbeitsalphabet: [0,1,blank],
#   4. Überführungsfunktion: Like (z0,1)=(z1,0,R),
#   5. Startzustand: z0 element Z
#   6. Blank-Symbol: blank,
#   7. E <= Z die Menge der Endzustände
#}

def calculateTransferFunction(zPresent, numberPresent, zForward, numberForward, direction):
    number = 5
    print("Geodelnumber is: " + str(number))

def calculateTM(tm):
    print("a")