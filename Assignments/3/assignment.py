print('1) Create a list with hetrogenous values')
print('Ans:')
r = ['python',12,range(-100,-50)]
print(r)
print('*'*20)
print()

print('2) mylst=[10,7,3.14,\"python\",range(5),[2,33,\'z\']]')
mylst=[10,7,3.14,"python",range(5),[2,33,'z']]
print('print the above list with help of for loop ')
print('Ans:')
for item in mylst:
    print(item)
print()
print('2.1) Print the last item in the forward and backward directions')
print('Ans:')
print(f'Last item in the forward direction:{mylst[-1]}; Last item in backward direction:{mylst[-len(mylst)]}')
print('*'*20)
print()

print('3) -23,-1,21,43; ')
print('create a range function for the above values')
print('Ans:')
rng = range(-23, 44, 22)
for i in rng:
    print(i)
print('*'*20)
print()

print('4) a=356')
print('Is it iterable? if yes why? if no  why?')
print('Ans:')
print("""\'a\' being an integer type, is not iterable by nature. Iterable variable contain multiple values.
The best test to check if a variable is iterable is by using len(\'variableName\'); if it returns 0 or positive values its iterable.
In this case it throws an error; hence its not iterable.""")
#print(len(a))
print('*'*20)
print()

print('5) Find the value of this expression : 3 * True + True + 4 * (3*True) - 20')
print('Ans: -4')
print(f'Expression evaluation result : {3 * True + True + 4 * (3*True) - 20}')
print('*'*20)
print()

print('6) Define the iterable and mutable?')
print('Ans:')
print("""
Iterable is any variable that can contain more than one values. Simple test of such a variable is to check lenght of it; len(\'variableName\'). If the function returns value without throwing any error, the variable is iterable
\t Iterable exhibits one or more of following characteristics : indexing, slicing, change of values (replacement, addtion, deletion or change of values using underlying type methods),
\t mutable/immutable, print using for loop/range, ordered element.\n
Mutable is any variable that allows change of value without changing its address (id).
list, set, dict, bytearray are mutable.
tupple, str, range, frozeset are immutable
""")
print('*'*20)
print()

print('7) Proof that list is mutable')
print('Ans:')
lst = [1,2,3]
print(f'list defined as {lst} at address \'{id(lst)}\'')
lst[0]=10
print(f'First element of the list is changed {lst} still at same address \'{id(lst)}\'')
print("""
This proves that list is mutable. Other methods of item assignment like adding using append, deleting using del, pop, remove, clear suuport the argument that list data type is mutable.
""")
print('*'*20)
print()

print('8) What is the mean of ordered items/elements?')
print('Ans:')
print("""
This is a property of an iterable datatype. Iterable datatype can contain multiple values. An iterable variable can be initialised with some values.
The order in which the values are given being same as the order when we print the values in the variable proves that the datatype supports ordered items.
list, range, dict, tupple, string, bytes, bytearray are examples of such datatypes.
If the order is not maintained then datatype does not support ordered items. set and frozeset are examples of such datatype.
""")
print('*'*20)
print()


print('9) What is meaning of duplicate and unique?')
print('Ans:')
print("""
The iterable datatype may support adding same value multiple times, hence support duplicate values. list, tupple, dict, str, bytes, bytearray support duplicate values.
set, frozeset support only unique values.
""")
print('*'*20)
print()

print('10) How will you findout a variable is iterable or not?')
print('Ans:')
print("""
Iterable is any variable that can contain more than one values. Simple test of such a variable is to check lenght of it; len(\'variableName\'). If the function returns value without throwing any error, the variable is iterable.
""")
print('*'*20)
print()
