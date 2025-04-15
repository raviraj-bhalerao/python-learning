print('1) Create the range function for this pattern - -1,-6,-13,-20')
print('Ans:')
r = range(1,-21,-7)
for i in r:
    print(i)
print('*'*20)
print()

print('2) create a range function to print the odd numbers from 21 to 35')
print('Ans:')
odd = range(21,36,2)
for i in odd:
    print(i)
print('*'*20)
print()

print('3) write a for loop and range function to print 100 to 3')
print('Ans1:')
nums = range(100,2,-1)
for i in nums:
    print(i)
print('#'*20)
print('Ans2:')
nums = range(3,101)
for i in nums[::-1]:
    print(i)
print('#'*20)
print()
print('*'*20)
print()

print('4) k =range(-26,-923,-34)')
k =range(-26,-923,-34)
print('Ans:')
print(f'4.1) findout total items/values? = {len(k)}')
print(f'4.2) print last element in the forward direction? = {k[len(k) - 1]}')
print(f'4.3) print last element(left to right) by using backward direction? = {k[-1]}')
print(f'4.4) Print first value of "k" variable(without using index 0) = {k[-len(k)]}')
print('*'*20)
print()

print('5) Write a program to print even ragne values with help of the for loop;')
print('take two inputs, ex: var1, ask the input in the form of integer and similary take the var2 input as int.')
print('Print all the numbers from var1 to var2(include var2 also')
print('Ans:')
var1str = input('Enter var1 as number :')
if var1str.isdigit():
    var1 = int(var1str) 
    var2str = input(f'Enter var2 (>={var1str}) :')
    if var2str.isdigit():
        var2 = int(var2str)
        if var2 >= var1:
            myRange = range(var1,var2+1,2)
            for i in myRange:
                print(i)
print('*'*20)
print()

