'''

PR.4 Functional Treat

Create a Data Analyzer and Transformer program in Python that utilizes various
functions to manipulate and analyze data in one-dimensional (1D) and
two-dimensional (2D) arrays (using lists). The project must demonstrate
proficiency in:
    -Utilizing built-in functions.
    -Creating user-defined functions(UDF)
    -Using *args, **kwargs, and ___doc___
    -Implementing function recursion
    -Applying lambda (anonymous) functions
    -Using the global keyword
    -Returning multiple values
    -Sorting and transforming list-based data collections

    
'''



dataset_summary = {}


def display_menu():
    '''

        This function just displays the menu of the whole program to keep the
        flow of the program smooth for the user-friendly experience.

        Parameters:
                        This function doesn't take any parameters.

        Returns:
                    This function doesn't returns any value.
                    
    '''
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")


def input_data():
        '''

        This function takes the data as input from the user to perform various
        operations on the data and give different results to the user.

        Parameters:
                        This function doesn't take any parameters.

        Returns:
                    This function doesn't returns any value.
                    
    '''

    global data
    print("\nStep 1: Input Data")
    choice = input("Enter '1' for 1D array or '2' for 2D array: ")
    if choice == '1':
        data = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
    elif choice == '2':
        rows = int(input("Enter number of rows: "))
        data = []
        for i in range(rows):
            row = list(map(int, input(f"Enter row {i+1} (separated by spaces): ").split()))
            data.append(row)
    else:
        print("Invalid choice. Returning to main menu.")
        return
    print("Data has been stored successfully!")


def display_summary():
        '''

        This function displays the summary of the data entered by the user like
        total elements, minimum value, maximum value, sum of all elements and
        average of all the elements.

        Parameters:
                        This function doesn't take any parameters.

        Returns:
                    This function doesn't returns any value.
                    
    '''

    global data
    print("\nStep 2: Display Data Summary (Built-in Functions)")
    if isinstance(data[0], list):  
        total_elements = sum(len(row) for row in data)
        flat_data = [item for row in data for item in row]
        min_value = min(flat_data)
        max_value = max(flat_data)
        total_sum = sum(flat_data)
        avg_value = total_sum / total_elements
    else:  
        total_elements = len(data)
        min_value = min(data)
        max_value = max(data)
        total_sum = sum(data)
        avg_value = total_sum / total_elements
    print("Data Summary:")
    print(f"- Total elements: {total_elements}")
    print(f"- Minimum value: {min_value}")
    print(f"- Maximum value: {max_value}")
    print(f"- Sum of all values: {total_sum}")
    print(f"- Average value: {avg_value:.2f}")


def calculate_factorial():
        '''

        This function has one more function in it which calls it self repeatetively
        until a condition is true and gives the factorial of the number entered by
        the user.

        Parameters:
                        This function doesn't take any parameters.

        Returns:
                    This function doesn't returns any value.
                    
    '''

    print("\nStep 3: Calculate Factorial (Recursion)")
    def factorial(n):
            '''

        This function is the main function where the logic of finding the factorial
        of a number entered using recursion method is mentioned.

        Parameters:
                        This function takes an int valueas a parameters from the
                        user to find it's factorial.

        Returns:
                    This function doesn't returns any value.
                    
    '''

        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {num} is: {factorial(num)}")


def filter_data():
        '''

        This function contains several small lambda functions to fillter out
        the data inputed by the user and prints all the values less than
        threshold entered by the user.
        

        Parameters:
                        This function doesn't take any parameters.

        Returns:
                    This function doesn't returns any value.
                    
    '''

    global data
    print("\nStep 4: Filter Data by Threshold (Lambda Function)")
    threshold = int(input("Enter a threshold value to filter out data above this value: "))
    if isinstance(data[0], list):  
        flat_data = [item for row in data for item in row]
        filtered_data = list(filter(lambda x: x >= threshold, flat_data))
    else:
        filtered_data = list(filter(lambda x: x >= threshold, data))
    print(f"Filtered Data (values >= {threshold}):")
    print(", ".join(map(str, filtered_data)))


def sort_data():
        '''

        This function sorts the data into ascending order or descending order
        by using sort() method or sortted() function.

        Parameters:
                        This function doesn't take any parameters.

        Returns:
                    This function doesn't returns any value.
                    
    '''

    global data
    print("\nStep 5: Sort Data")
    if isinstance(data[0], list):  
        print("Sorting rows in 2D array:")
        for row in data:
            row.sort()
        print("Sorted 2D Array:")
        for row in data:
            print(row)
    else:  
        choice = input("Choose sorting option:\n1. Ascending\n2. Descending\nEnter your choice: ")
        if choice == '1':
            data.sort()
            print("Sorted Data in Ascending Order:")
        elif choice == '2':
            data.sort(reverse=True)
            print("Sorted Data in Descending Order:")
        else:
            print("Invalid choice. Returning to main menu.")
            return
        print(", ".join(map(str, data)))


def dataset_statistics():
        '''

        This function prints the statics values that have been gained by
        doing several operations on the data entered by the user like
        minimum value, maximum value, sum of all elements and average of all
        the values of the data.

        Parameters:
                        This function doesn't take any parameters.

        Returns:
                    This function doesn't returns any value.
                    
    '''

    global data
    print("\nStep 6: Display Dataset Statistics (Return Multiple Values)")
    if isinstance(data[0], list): 
        flat_data = [item for row in data for item in row]
        min_value = min(flat_data)
        max_value = max(flat_data)
        total_sum = sum(flat_data)
        avg_value = total_sum / len(flat_data)
    else:  
        min_value = min(data)
        max_value = max(data)
        total_sum = sum(data)
        avg_value = total_sum / len(data)
    print("Dataset Statistics:")
    print(f"- Minimum value: {min_value}")
    print(f"- Maximum value: {max_value}")
    print(f"- Sum of all values: {total_sum}")
    print(f"- Average value: {avg_value:.2f}")


def main():
        '''

        This function acts as a main function of the whole program like this
        function calls the other functions which is called bythe user.
        
        Parameters:
                        This function doesn't take any parameters.

        Returns:
                    This function doesn't returns any value.
                    
    '''

    global data
    data = []  
    while True:
        display_menu()
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            input_data()
        elif choice == 2:
            display_summary()
        elif choice == 3:
            calculate_factorial()
        elif choice == 4:
            filter_data()
        elif choice == 5:
            sort_data()
        elif choice == 6:
            dataset_statistics()
        elif choice == 7:
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
