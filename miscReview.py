def main():
    # problem1()
    problem2()





def problem1():
    userInput = ""
    while userInput !="quit":
        print(userInput)
        userInput= input("Name some of you favorite role models. When No one else seems to impress you enter 'quit'")
        if userInput.lower() == "quit":
            break






# Create a function that has a loop that quits with ```q```. If the user doesn't enter ```q```, ask them to input another string.
#
# BONUS: Make sure the code can handle whatever case the User enters the ```q``` as (uppercase or lowercase).
#

def problem2():

    def Problem2Helper(num1,num2,num3,operation):
        if operation == "ADD":
            result = (num1 + num2 + num3)
        elif operation == "PROD":
            result= (num1 *num2 *num3)
        elif operation == "AVG":
            result= ((num1 + num2 + num3) / 3)

        return result


    print(Problem2Helper(1,2,4,"ADD"))
    print(Problem2Helper(1,2,4,"PROD"))
    print(Problem2Helper(1,2,4,"AVG"))







#     Write 2 functions: ```exercise2()``` and ```exercise2_helper(num1, num2, num3. operation)```
#
# The function ```exercise2_helper(num1, num2, num3)``` should expect 3 numbers, and an operation to perform as a String as parameters.
#
# The function should support 3 operations:
# * ```SUM``` - Return the sum of the 3 numbers
# * ```PROD``` - Return the product of the 3 numbers
# * ```AVG``` - Return the average of the 3 numbers
#
# The operation and the returned value should then be printed out back in the main ```exercise2()``` function
# . Return ```INVALID OPERATION``` if an operation passed in that isn't supported. HINT: Use ```switch/case```













if __name__ == '__main__':
    main()