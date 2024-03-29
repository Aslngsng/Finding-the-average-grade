#ask the user to input their grades in Math, Science, and English
math = float(input("Please inpur your grade in Math: "))
science = float(input("Please input your grade in Science: "))
english = float(input("Please input your grade in English: "))

#get the average grade of three subjects
average = ((math + science + english) / 3)
print(int(average))

#identify if they passed or not
if average > 100 or average <= 50:
    print("Invalid grade")
elif average >=98 and 99:
    print("With Highest Honor")
elif average >= 95 and 97:
    print ("With High Honor")
elif average >= 90 and 94:
    print ("With Honor")
elif average >= 75 and 89:
    print ("You passed")
elif average >= 60 and 73:
    print ("You failed")