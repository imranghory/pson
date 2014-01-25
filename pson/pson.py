import json
from pprint import pprint

def pathparser(path, separator="."):
        return path.split(separator)

def pathquery(pson, path, separator=".", missing=None, iterate=True):

        if isinstance(path,str) or isinstance(path, unicode):
                path = pathparser(path, separator=separator)

	counter = 0
        for token in path:
                if type(pson) == dict and pson.has_key(token): # step one level deeper into the pson with our token
                        pson = pson[token]
                elif type(pson) == list: 
			# if we hit an array see if the token is a number else assume we 
			# want the rest of the path applied to every element in the array
                        try:
                                if int(token)<len(pson):
                                        pson = pson[int(token)]
                                else: #handle a number longer than list len
                                        return missing
                        except ValueError: 
				if iterate:
	                                return [pathquery(x, path[counter:]) for x in pson]
				return missing
                else:
                        return missing
		counter += 1

        return pson

