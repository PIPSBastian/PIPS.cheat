def cheat(assignment):
    if assignment == "Assignment 1.1":
        print("Here is the correct solution")
        print("")
        print("import numpy as np")
        print("# a)")
        print("another_array = np.zeros((2, 4, 6))")
        print("")
        print("# b)")
        print("# the last element of the first dimension")
        print("print(another_array[-1, 0, 0])")
        print("")
        print("# the first element of the second dimension")
        print("print(another_array[0, 2, 0])")
        print("")
        print("# the third element of the third dimension")
        print("print(another_array[0, 0, 2])")
    elif assignment == "Assignment 2.1":
        print("Here is the correct solution")
        print("")
        print("current_time = datetime.now().hour")
        print("if current_time < 5:")
        print("    print('go to sleep')")
        print("elif current_time > 7 and current_time < 10:")
        print("    print('Eat je Hagelslag!')")
        print("else:")
        print("    print('Gut gemacht!')")
    else:
        print("I am sorry")
        print("The solution to the assignment you are requesting is not part of this function")
        print("or you entered the input incorrectly.")
        print("")
        print("The input should be a string with the following format: Assignment x.x")
