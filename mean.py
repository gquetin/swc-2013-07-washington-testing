#!/usr/bin/env python

def mean(numlist):
    """Calculate the mean of the values in numlist

    Input
    =====
    `numlist` (`list` or `tuple`) - List of values whose mean will be calculated
	'numlist' should only contain integers or floats
	
    Output
    ======
    (`float`) - Mean of the values in numlist
    
    """
    if type(numlist) != tuple and type(numlist) != list:
    	raise TypeError("Error in input type")
	
	if numlist == None:
		print('Error, trying to pass in empty variable')
		return None
		
	if len(numlist) == 0:
		print('List length 0')
		return None
    
    for i in range(len(numlist)):
    	if type(i) != int and type(i) != float:
    		print('List has none numbers')
    		return None
    
    numlist2 = []	
    for i in range(len(numlist)):
    	numlist2.append(float(numlist[i]))		
    
    try :
        total = sum(numlist2)
        length = len(numlist2)
    except TypeError :
        raise TypeError("The list was not numbers.")
    except :
        print "Something unknown happened with the list."
    return total/length
    
if __name__ == '__main__':
	A = (1,2,3,4)
	print mean(A)