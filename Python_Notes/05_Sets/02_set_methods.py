# CREATING AN EMPTY SET 
a = set()

# 1. ADDING VALUES TO AN EMPTY SET 
a.add(1)
a.add(5)
a.add(6)
a.add(1)
a.add(1)
a.add(5)

print(a)  # {1, 5, 6}

#  We cannot add a list or dictionary in the set Eg : a.add([2, 3, 4]) - it wll show error
# But we can add a tuple in set Eg : (1, 2, 3)

# ADDING A TUPLE IN SET 
a.add((1, 2, 3, 4))
print(a)  # {(1, 2, 3, 4), 1, 5, 6}
print("Type of a: ",type(a))  # Type of a:  <class 'set'>
# EVEN IF WE CAN PRINT A TUPLE IN SET BUT WE CANNOT CHANGE THE VALUES IN SET AS TUPLE ITSELF CANNOT BE CHANGED

# 2. LEN()
# PRINTS THE LENGTH OF THE SET 
print(len(a))  # 4

# 3. REMOVE()
# REMOVES THE SPECIFIED ELEMENT FROM THE SET 
a.remove(1)
print(a)  # {(1, 2, 3, 4), 5, 6}
# if we try to remove an element which is not present in the set then it will show error Eg. a.remove(10)

# 4. POP()
# REMOVES ANY RANDOM ELEMENT FROM THE SET AND RETURNS THE VALUE OF ELEMENT WHICH IS REMOVED 
print("REMOVED AN ELEMENT FROM THE SET ",a.pop())
print("REMANINIG SET",a)

# 5. CLEAR()
# EMPTIES THE ENTIRE SET 
# EG : a.clear() ; output : None

mySet = {4,68,34,5,2}

# 6. UNION()
# COMBINES TWO SETS. RETURNS A NEW SET WITH ALL ITEMS FROM BOTH SET
set1 = {4,98,76,2,3}
newSet = mySet.union(set1)
print("\nUnion of set is : ",newSet)  # Union of set is : {34, 2, 4, 5, 68, 98, 3, 76}

# 7. INTERSECTION()  
# Returns the elements that are common to both the sets.
newSet2 = mySet.intersection(set1)
print("\nIntersection of set is : ",newSet2)  # Intersection of set is :  {2, 4}

# 8. INTERSECTION UPDATE FUNCTION
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)  # {'Madrid', 'Tokyo'}

# 9. UPDATE FUNCTION
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1 ,s2)  # {1, 2, 5, 6} {3, 6, 7}
s1.update(s2)
print("Updated set : ",s1,s2)  Updated set :  {1, 2, 3, 5, 6, 7} {3, 6, 7}

# 10. SYMMETRIC DIFFERENCE FUNCTION
# (AUB)-(A intersection B)
# This means the values which are not common in A and B
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)  # {'Kabul', 'Seoul', 'Berlin', 'Delhi'}

# 11. DIFFERNCE FUNCTION
# Difference function means A-B
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)  # {'Madrid', 'Berlin', 'Tokyo'}

# 12. DISJOINT SET
# Disjoint set means when elements in both the sets are different. Eg:-
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Kanpur", "Jalandhar"}
cities3 = cities.isdisjoint(cities2)
print(cities3)  # True

# 13. ISSUPERSET FUNCTION
# A superset is a set of elements containing all of the elements of another set.
'''A is a superset of B if it contains all of the elements of B. Eg :- Set A elements are {1,2,3,4,5,6,7,8,9,10} 
Set B elements are {1,3,5,7,9}. Here B contains all the elements of A.'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))  # False
cities3 = {"Tokyo", "Madrid", "Delhi"}
print(cities.issuperset(cities3))  # True

# 14. ISSUBSET FUNCTION
print(cities3.issubset(cities))  # True

# 15. DEL AND CLEAR
''' The difference between del and clear is that del deletes the entire set whereas clear deletes all the elements
of the set.'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)  # set()

