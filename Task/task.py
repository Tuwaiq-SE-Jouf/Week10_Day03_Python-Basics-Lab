
#Task..1
num1=7
num2=9
print(num1+num2)

#Task..2
num = 5

factorial = 1

if num < 0:
  print("factorial does not exist for negative numbers")
elif num == 0:
  print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#Task..3

start = 50
end = 100

print("Prime numbers between 50 and 100 are:")

for num in range(start, end + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#Task..4
def show_student(name, GPA=0):
    print (name , GPA)

show_student("NAFLA :" , 90)

#Bonus..
def solve(students):
   min_mark = min(x[1] for x in students)
   students = [x for x in students if x[1] > min_mark]
   min2_mark = min(x[1] for x in students)
   students = sorted([x[0] for x in students if x[1] == min2_mark])
   for x in students:
      print(x)

students = [['Amal',37],['Noor',44],['Maram',36],['Reem',41],['Nafla',33]]
solve(students)