d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 40, 'e': 50, 'f': 60}

print(d1.items()) #Returns a list of all the items in the dictionary with each key-value pair inside a tuple.
print(d1.get('a')) #Retrieve value using the key name a.
d1['Math'] = 89 #Update dictionary by adding a new key
d1.pop('b')	#SRemove the key b from the dictionary.
d3= {**d1, **d2}	#Join two dictionaries.
d2 = d1.copy()	#Copy dictionary d1 into d2.
d1.clear()	#Removes all items from the dictionary.
print(d1)