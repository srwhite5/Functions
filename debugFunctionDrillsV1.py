'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with FUNCTIONS.
Focus on the functions and find the problems with the FUNCTIONS.

For this debug, there could be problems with executing the functions. For example,
calling the function may have been done wrong, or put in the wrong spot. So don't
just look at the function itself but also the line calling the function.

Additionally, if converting becomes difficult, ask the instructor about how to
use a conversion table or other tricks to help make sure the conversion is right.

The number of errors are as follows:
ouncesToGallons: 4
gallonsToOunces: 6
gramsToPounds: 4
poundsToGrams: 4
'''

#The problems are between the two --- lines
#-------------------------------------------------
ouncesToGallons(24)

'''
This function converts ounces to gallons using three steps.
'''
def ounces_To_Gallons(ounces, cups, quarts, gallons):
    #There are eight ounces in a cup
    cups = ounces / 8
    
    #There are four cups in a quart
    quarts = cups / 4
    
    #There are four quarts in a gallon
    gallons = quarts / 4
    
    return gallons

#------------------------------------------------


#The problems are between the two --- lines
#-------------------------------------------------
'''
This function converts gallons to ounces using three steps.
'''
def gallons_To_Ounces(gallons, ounces, quarts, cups):
    #There are four quarts in a gallon
    quarts = gallons + 4
    
    #There are four cups in a quart
    cups = quarts - 4
    
    #There are 8 ounces in a cup
    ounces = cups + 8
    
    return 

x = gallons_To_Ounces(24)
x = gallons_To_Ounces(4)
#------------------------------------------------



#The problems are between the two --- lines
#-------------------------------------------------
'''
This function converts grams to pounds using two steps.
'''
def grams_To_Pounds(grams,ounces,pounds):
    #There are 16 ounces in one pound
    pounds = ounces / 16
    
    #There are .035 ounces in a gram
    ounces = grams * .035
    
    return pounds

grams_To_Pounds(60)
grams_To_Pounds(360)

#------------------------------------------------


#The problems are between the two --- lines
#-------------------------------------------------
'''
This function converts pounds to grams using two steps.
'''
def pounds_To_Grams(pounds):
    #There are 16 ounces in one pound
    ounces = pounds * 16
    
    #There are .035 ounces in a gram
    grams = ounces / .035
    
    return grams

x = pounds_To_Grams(60)
x = pounds_To_Grams (360)

#------------------------------------------------