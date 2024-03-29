#ask the user to input their grades in Math, Science, and English

#identify if they passed or not

math = float(input("Please inpur your grade in Math: "))
science = float(input("Please input your grade in Science: "))
english = float(input("Please input your grade in English: "))

#get the average grade of three subjects
average = ((math + science + english) / 3)
print(int(average))
