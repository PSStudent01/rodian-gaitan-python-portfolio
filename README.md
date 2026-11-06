# Python Portfolio

## Python Programming Projects & Practical Applications

Welcome to my Python portfolio!

This repository contains nine Python projects completed as part of my Python Essentials training through Per Scholas. The projects demonstrate my understanding of Python fundamentals, object-oriented programming, data structures, functions, exception handling, file operations, data persistence, and application organization.

My goal in building this portfolio was not simply to complete the exercises, but to understand how the code works, what each component does, how different programming concepts interact, and how to troubleshoot issues when something doesn't work as expected.

I'm particularly interested in applying these technical skills to **Business Systems Analyst, Application Support Analyst, ERP Support, Business Analyst, and Data Analytics** opportunities.

---

## About Me

I have an educational background in Management Information Systems (MIS) and professional experience supporting IT environments, proprietary business applications, and ERP systems.

My background includes application support, ERP administration, financial systems, data analysis, SQL, and working with business users to resolve application and data-related issues.

I've also worked with enterprise applications and tools such as Oracle Fusion Financials, Revenue Management, BI Publisher, Excel, Power Query, and SQL.

As I continue developing my technical skills, I'm using Python to complement my existing IT and ERP experience, particularly in areas involving application support, business processes, data handling, troubleshooting, and automation.

I'm interested in opportunities where I can combine technical knowledge with an understanding of business applications, data, and operational requirements.

---

## Technical Skills & Concepts

The following are some of the technologies and concepts represented in my training and project work.

**Programming & Development**
- Python
- Object-Oriented Programming (OOP)
- Functions, modules, and packages
- Data structures and algorithms
- Conditional logic and loops
- Input validation and exception handling

**Data Handling & Processing**
- Lists, tuples, and dictionaries
- CSV file handling
- Data persistence
- Date and time processing
- String manipulation
- Data validation and processing

**Application Support & Troubleshooting**
- Application logic and execution flow
- Error handling and debugging
- File and directory management
- Operating environment and dependencies
- Testing normal and invalid application scenarios

**Additional Technical Background**
- SQL
- Excel and Power Query
- Oracle Fusion Financials
- Oracle Revenue Management
- BI Publisher
- ERP and business application support

---

# Python Projects

## 1. Conditionals, Loops, and Lists

**Project Overview**

A collection of Python exercises demonstrating conditional logic, loops, list operations, and basic problem-solving techniques.

The exercises include:
- Bubble Sort – sorting a list of numbers using nested loops and comparisons.
- Even Number Sum – calculating the sum of even numbers using both `for` and `while` loops.
- Grade Checker – validating numerical scores and assigning letter grades based on defined ranges.

**What I Learned**

- Creating and manipulating lists.
- Using nested loops to compare and sort values.
- Accessing list elements through indexes.
- Swapping values using tuple unpacking.
- Using `range()` to control loop execution.
- Understanding the differences between `for` and `while` loops.
- Using the modulo operator (`%`) to identify even numbers.
- Maintaining running totals using assignment operators.
- Defining functions and returning values.
- Validating user input using `try/except`.
- Handling `ValueError` exceptions.
- Using `continue` and `return` to control program execution.
- Applying conditional logic and chained comparisons.

**Practical Application:** These concepts provide a foundation for processing collections of data, validating information, applying business rules, and understanding application logic.

---

## 2. Functions, Tuples, Dictionaries, and Exceptions

**Project Overview**

A collection of exercises demonstrating reusable functions, structured data, mathematical operations, and exception handling.

The exercises include:
- Exception Handling – demonstrating how to raise and catch exceptions using a safe division function.
- Grade Processing – calculating average grades stored in tuples and organizing course information using dictionaries.
- Calculator – performing arithmetic operations through separate functions and handling invalid inputs and division by zero.

**What I Learned**

- Defining reusable functions with parameters and return values.
- Working with tuples and understanding immutable data.
- Using dictionaries to organize related information as key-value pairs.
- Iterating through dictionaries and tuples.
- Using `sum()` and `len()` to process numerical data.
- Raising exceptions using `raise ValueError()`.
- Handling exceptions using `try/except/finally`.
- Understanding the difference between raising an exception and catching one.
- Handling specific exceptions such as `ValueError` and `ZeroDivisionError`.
- Returning `None` when a calculation cannot be completed.
- Using conditional logic to determine which operation should execute.
- Separating application logic from input and output operations.

**Practical Application:** These concepts are useful when working with structured business data, reusable application functionality, data processing, and troubleshooting errors.

---

## 3. Object-Oriented Programming

**Project Overview**

A two-file project demonstrating object-oriented programming through a basic bank account and savings account implementation.

The project consists of:

- `bank.py` – defines a `BankAccount` class with account information, deposit and withdrawal methods, transaction validation, and balance management.
- `savings.py` – defines a `SavingsAccount` subclass that inherits functionality from `BankAccount` and introduces interest-rate calculations.

**What I Learned**

- Defining classes and creating objects.
- Using `__init__()` to initialize object attributes.
- Understanding `self` and instance attributes.
- Creating and calling instance methods.
- Managing object state as account balances change.
- Applying conditional logic to validate transactions.
- Raising and catching `ValueError` exceptions.
- Returning updated values from methods.
- Using `__str__()` to create readable object representations.
- Understanding class inheritance and code reuse.
- Using `super()` to access parent-class functionality.
- Extending constructors with additional attributes.
- Overriding inherited methods.
- Testing inherited functionality and subclass-specific behavior.

**Testing & Execution**

The project was tested with successful deposits and withdrawals, invalid transaction amounts, and withdrawals exceeding the available balance.

I also compared the savings account output before and after overriding `__str__()` to verify that the interest-rate information was included in the updated object representation.

**Practical Application:** These concepts are relevant to understanding transaction-based applications, maintaining application data, enforcing business rules, and extending existing application functionality.

---

## 4. Generators, Closures, and Utility Modules

**Project Overview**

A collection of Python exercises demonstrating generators, closures, file operations, exception handling, and standard library modules.

The project consists of:

- `multiplier_closure.py` – demonstrates nested functions and closures that retain access to variables from an enclosing function.
- `fibonacci_generator.py` – generates Fibonacci numbers using a generator function and `yield`.
- `diary.py` – demonstrates creating, writing, appending, and reading files.
- `calendar_utility.py` – uses Python's calendar and datetime modules to retrieve and display calendar information.

**What I Learned**

**Closures**
- Defining nested functions.
- Understanding variable scope.
- Returning functions as values.
- Using closures to retain access to variables from an enclosing function.
- Creating reusable functions with customized behavior.

**Generators**
- Defining generator functions.
- Using `yield` to pause and resume function execution.
- Understanding lazy evaluation.
- Generating values one at a time.
- Using iteration and multiple assignment.
- Understanding the memory-efficiency benefits of generators.

**File Handling**
- Creating, opening, writing, appending, and reading files.
- Understanding file modes such as `"a"` and `"r"`.
- Using context managers with `with open()`.
- Handling file-related exceptions.
- Understanding exception inheritance, including `FileNotFoundError` and `PermissionError` as subclasses of `OSError`.
- Working with timestamps using `datetime`.
- Understanding basic file-based data persistence.

**Standard Library Modules**
- Importing and using Python's `calendar` and `datetime` modules.
- Working with dates and calendar information.
- Validating user input.
- Handling invalid month values and other exceptions.
- Using built-in functions to avoid unnecessary custom implementations.

**Testing & Troubleshooting**

I deliberately modified file paths and configurations to reproduce errors, observed how the program responded, and verified that previously saved data remained intact.

**Practical Application:** These concepts are particularly useful when working with file-based processes, troubleshooting file access problems, handling application errors, and developing reusable support utilities.

---

## 5. Python To-Do List Manager

**Project Overview**

A command-line To-Do List Manager that allows users to create, display, complete, and delete tasks.

The application is organized into three Python files:

- `task.py` – defines the Task class, including task titles, optional due dates, completion status, and string representation.
- `todolist.py` – contains the application functionality for managing tasks, validating input, handling dates, and saving or loading task information.
- `main.py` – controls the application's menu and overall execution flow.

The application uses a CSV file to store task information so that tasks can be retrieved when the program runs again.

**What I Learned**

**Object-Oriented Programming**
- Creating classes and objects.
- Initializing objects using `__init__()`.
- Working with `self`, instance attributes, and default argument values.
- Using Boolean attributes.
- Overriding the default object representation with `__str__()`.

**Functions and Modular Programming**
- Defining reusable functions.
- Passing arguments and returning values.
- Importing classes and functionality from other modules.
- Separating application responsibilities across multiple Python files.
- Passing objects and lists between functions.

**Data Structures and Application Logic**
- Creating and managing lists of objects.
- Adding items using `append()`.
- Retrieving and removing items using indexes.
- Iterating through lists using `for` loops.
- Using `enumerate()` to retrieve indexes and values.
- Implementing menu-driven application logic.
- Applying CRUD operations: Create, Read, Update, and Delete.

**Input Validation and Date Processing**
- Capturing and converting user input.
- Validating required and optional information.
- Using `strip()` to identify empty or whitespace-only input.
- Converting date strings using `datetime.strptime()`.
- Working with `datetime.date` objects.
- Using `date.today()` and comparing dates to identify overdue tasks.

**File Handling and Data Persistence**
- Opening files using `open()`.
- Understanding read (`"r"`) and write (`"w"`) modes.
- Using `with open()` to manage file operations.
- Writing CSV records using `csv.writer()` and `writerow()`.
- Reading CSV records using `csv.reader()`.
- Reconstructing Task objects from saved CSV records.
- Converting stored string values back into appropriate data types.
- Understanding how file-based persistence maintains data between application executions.

**Exception Handling and Troubleshooting**
- Handling `ValueError` and `IndexError`.
- Handling file-related exceptions such as `OSError`, `PermissionError`, and `FileNotFoundError`.
- Providing user-friendly error messages.
- Understanding exception inheritance.
- Deliberately triggering errors to test exception-handling behavior.

**Project Organization**
- Understanding relative and absolute file paths.
- Working with the current working directory.
- Using `__file__`, `os.path.abspath()`, and `os.path.dirname()`.
- Building file paths using `os.path.join()`.
- Checking file existence using `os.path.exists()`.
- Using `.gitignore` to exclude generated files and Python cache directories.

**Practical Application:** This project combines several Python concepts into a working application and demonstrates record management, data validation, file-based persistence, application organization, and troubleshooting.

---

## 6. Contact Book Application

**Project Overview**

A menu-driven contact management application that allows users to add, view, search, and delete contacts.

The application uses a Python dictionary to store contact names and phone numbers while the program is running.

**What I Learned**

- Defining reusable functions to organize application operations.
- Creating and managing dictionaries using key-value pairs.
- Adding, retrieving, searching, and deleting dictionary entries.
- Passing a dictionary between functions to maintain shared application data.
- Validating user input using `strip()`, `lower()`, and `isdigit()`.
- Checking for empty values and duplicate contact names.
- Validating phone numbers based on numeric characters and length.
- Using conditional statements and Boolean expressions.
- Building menu-driven applications using `while` loops.
- Using `for` loops to iterate through dictionary entries.
- Implementing partial and case-insensitive searches.
- Using Boolean flags to determine whether a matching contact was found.
- Understanding the differences between `return` and `break`.
- Implementing basic CRUD operations.

**Practical Application:** These concepts are useful when managing records, validating user-entered information, searching structured data, and developing basic application functionality.

**Note:** Contact information is stored in memory only and is not retained after the program terminates.

---

## 7. Simple Calculator

**Project Overview**

A Python script that accepts two numbers and an arithmetic operator from the user, performs the selected calculation, and displays the result.

The calculator supports addition, subtraction, multiplication, and division.

**What I Learned**

- Collecting user input using `input()`.
- Understanding that user input is initially returned as a string.
- Validating numeric input using `isdigit()`.
- Understanding the limitations of `isdigit()` when working with negative and decimal numbers.
- Converting strings into integers using `int()`.
- Applying Boolean logic using `not` and `or`.
- Using `if`, `elif`, and `else` to control program execution.
- Implementing arithmetic operations.
- Using nested conditional statements.
- Checking for division by zero before performing a calculation.
- Storing calculation results in variables.
- Displaying formatted results using f-strings.
- Providing user-friendly messages for invalid input and operations.

**Practical Application:** This exercise reinforces data type conversion, input validation, conditional logic, and error prevention.

---

## 8. List Manager

**Project Overview**

A menu-driven application that manages a list of integers. Users can add numbers, remove numbers by index, display the current list, or quit the application.

The application uses exception handling to manage invalid numeric input and incorrect list indexes.

**What I Learned**

- Creating and managing Python lists.
- Adding values using `append()`.
- Removing values using `pop()`.
- Understanding list indexes and zero-based indexing.
- Defining functions to separate application operations.
- Using `while` loops to maintain a repeating menu.
- Applying conditional logic to process user selections.
- Converting user input into integers using `int()`.
- Handling `ValueError` when invalid numeric input is entered.
- Handling `IndexError` when an invalid list index is used.
- Using `try/except` to prevent unhandled exceptions.
- Normalizing menu selections using `lower()`.
- Organizing program execution using a `main()` function.

**Practical Application:** These concepts are useful when managing collections of data, validating user input, handling application errors, and developing interactive command-line utilities.

---

## 9. Python Modules, Packages, and Libraries

**Project Overview**

A collection of exercises demonstrating how to use Python's standard library, install third-party packages, create custom modules, and organize reusable functionality into packages.

The exercises include:

- Standard Library Modules – using `math`, `random`, and `platform` to perform calculations, generate random numbers, and retrieve operating system and Python version information.
- Third-Party Packages – installing and using `colorama` to display colored terminal output.
- Custom Packages – importing and using functions from a custom `mypackage` package.
- Utility Modules – defining reusable greeting and factorial functions in `utilities.py`.
- Package Initialization – using an `__init__.py` file to organize the package.

**What I Learned**

- Importing and using Python standard library modules.
- Generating random numbers using `random.randint()`.
- Performing mathematical calculations using `math.sqrt()` and `math.floor()`.
- Retrieving operating system information using `platform.system()`.
- Retrieving Python version information using `platform.python_version()`.
- Installing third-party packages using `pip`.
- Importing specific components from external packages.
- Initializing and using the `colorama` package.
- Creating custom Python modules.
- Organizing related modules into package directories.
- Understanding the purpose of `__init__.py`.
- Importing custom functionality using `from ... import`.
- Calling imported functions using dot notation.
- Reusing existing library functionality such as `math.factorial()`.
- Separating the main program from reusable utility functions.
- Using `if __name__ == "__main__":` to test a module independently.

**Practical Application:** Understanding modules, packages, imports, and dependencies is useful when navigating existing Python projects, troubleshooting application functionality, and maintaining reusable support scripts.

---

# Overall Skills Developed

Across these nine projects, I've developed practical experience with several areas of Python programming.

| Skill Area | Concepts Practiced |
|---|---|
| Python Fundamentals | Variables, data types, operators, input, and output |
| Conditional Logic | `if`, `elif`, `else`, Boolean expressions |
| Loops | `for`, `while`, nested loops, iteration |
| Data Structures | Lists, tuples, dictionaries, objects |
| Functions | Parameters, arguments, return values, reusable functions |
| Object-Oriented Programming | Classes, objects, attributes, methods, inheritance |
| Exception Handling | `try`, `except`, `finally`, `raise`, common exceptions |
| Data Validation | Input validation, conditional checks, business rules |
| File Handling | Reading, writing, appending, CSV processing |
| Data Persistence | Saving and retrieving application data |
| Date Processing | `datetime`, date conversion, date comparisons |
| String Manipulation | Slicing, concatenation, formatting, character processing |
| Modules & Packages | Imports, standard libraries, third-party dependencies |
| Troubleshooting | Testing, debugging, exception handling, file paths |
| Development Practices | Project organization, Git, `.gitignore` |

---

# Career Interests & Professional Direction

I'm interested in opportunities where I can combine my existing IT and ERP experience with the technical skills I'm continuing to develop.

My areas of interest include:

- Business Systems Analyst
- Application Support Analyst
- ERP Support Analyst / ERP Administrator
- Business Analyst
- SQL Analyst
- Data Analyst
- Business Systems Support

I'm particularly interested in working with business applications, supporting system functionality, investigating application and data issues, understanding business processes, and identifying opportunities to improve operational efficiency.

I view Python as an additional tool that can complement my experience with ERP systems, SQL, Excel, and business application support.

---

## Final Thoughts

These projects represent my progression through Python Essentials and my effort to develop a stronger understanding of programming concepts through practical exercises.

I believe understanding how code works is just as important as getting it to execute successfully. Throughout these projects, I've focused on understanding the purpose of individual statements, following program execution, handling errors, testing different scenarios, and recognizing how separate components work together.

I'm continuing to build on these skills as I work toward opportunities in Application Support, ERP Support, Business Systems Analysis, Business Analysis, and Data Analytics.

**Thank you for taking the time to review my portfolio!**