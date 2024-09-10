# using lambda functions
'''
This function can have any number of arguments but only one expression, which is evaluated and returned.
One is free to use lambda functions wherever function objects are required.
You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
'''
#used to reduce code

longstring  = "hi This code defines a lambda function named upper that takes a string as its argument and converts it to uppercase using the upper() method."

upper = lambda s: s.upper()
print(upper(longstring))

format_no = lambda number: f"{number:e}" if  isinstance(number, int) else f"{number:,.2f}"

print(f"number: {format_no(10000000)}")
print(f"number: {format_no(999999)}")

def cube_add_one(num):
    return (num**3)+1

num = 5
print(f"cube of {num} plus 1 is {cube_add_one(num)}")    
cube1 = lambda num: num**3 + 2
print(f"cube of {num} plus 2 is {cube1(num)}")    

even_list = [lambda num = x: num**x for x in range(1,6)]

for i in ([lambda num = x: num**x for x in range(1,6)]):
    print(i())

n = (lambda num: num**2)(15)        #225 will be return value
print(n)

# print(len([lambda num = x: num**x for x in range(1,6)]))

List = [[9,8,7],[6,5,4],[1,2,3],[10,9,5]]
print(List[0:2])

sort = lambda li: (sorted(i) for i in li)
sort(List)
print(List)

times2 = lambda li: [li[i]*2 for i in range(len(li))]
li1 = [1,2,3,4,5]
print(times2(li1))

    
