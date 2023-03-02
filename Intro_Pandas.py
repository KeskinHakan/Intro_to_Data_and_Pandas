import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

main_topic = ["Introduction to Python", "Introduction to Pandas"]
selected_main_topic = st.sidebar.selectbox('Select a Main Topic', main_topic)

if selected_main_topic == "Introduction to Python":

    options = ['Introduction', 'Loops', 'If-else statements', 'While loops', 'List comprehension', 'Dictionaries']
    selected_option = st.sidebar.radio('Select a topic', options)

    # Show the appropriate content based on the user's selection
    if selected_option == 'Introduction':
        st.title('Inspired by Miuul.')

        "This open-source web applications is prepared by Hakan Keskin. Miuul and 11. Term Data Science and Machine Learning Bootcamp inspired me" \
        "to prepare the this content develop with the other Data Science Enthusiast."

        "Source code can be seen in my GitHub Account: https://github.com/KeskinHakan"

        st.title("Python Introduction")
        "In this part you can find the Python Basics below"

        explanations = [
            'Loops',
            'If-else Statements',
            'While Loops',
            'List Comprehension',
            'Dictionaries'
        ]

        for i, explanation in enumerate(explanations):
            st.write(f"{i + 1}. {explanation}")

    elif selected_option == 'Loops':
        st.title("Loops")
        "A for loop is used to iterate over a sequence of elements, such as a list, tuple, or string. The basic syntax of a for loop in Python is:"

        "In this syntax, variable is a new variable that takes on the value of each element in the sequence as the loop iterates. You can use variable to perform some action or calculation for each element in the sequence. For example, here's a for loop that iterates over a list of numbers and prints each one to the console:"

        st.subheader('Example 1')
        "Using a for loop to iterate over a list of numbers and print each number"
        numbers = [1, 2, 3, 4, 5]
        code = """
        numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num)

        """
        st.code(code, language='python')

        for num in numbers:
            st.write(f"The result is {num}")

        # Example 2: Using a for loop to iterate over a string and print each character
        st.subheader('Example 2')
        "Using a for loop to iterate over a string and print each character"
        code = """
        word = 'Python'
for char in word:
    print(f"{char}")

        """
        st.code(code, language='python')
        word = 'Python'
        for char in word:
            st.write(f"{char}")

        # Example 3: Using a for loop to iterate over a dictionary and print each key-value pair
        st.subheader('Example 3')
        "Using a for loop to iterate over a dictionary and print each key-value pair"
        code = """
        fruits = {'apple': 1, 'banana': 2, 'orange': 3}
for fruit, count in fruits.items():
    print(f"You have total {count} {fruit}")

        """
        st.code(code, language='python')
        fruits = {'apple': 1, 'banana': 2, 'orange': 3}
        for fruit, count in fruits.items():
            st.write(f"You have total {count} {fruit}")

        st.subheader('Example 4')
        "Loop Control Statements:"
        """
        Python provides several special statements that allow you to control the flow of a loop. These statements include
        break, continue, and pass.
        
            1- 'break' is used to immediately exit a loop, even if the loop 
            condition has not been fully satisfied.
            2- 'continue' is used to skip over the current iteration of a loop 
            and move on to the next iteration.
            3- 'pass' is used as a placeholder statement when you need to include a statement 
            that does nothing, such as in a loop that hasn't been fully implemented yet.
        """
        code = """
    numbers = [1, 2, 3, 4, 5]

    for num in numbers:
        if num == 3:
            break  # exit the loop when num is 3
        elif num == 2:
            continue  # skip num 2 and move on to the next iteration
        else:
            pass  # do nothing for all other values of num
        print(num)

                    """
        st.code(code, language='python')
        numbers = [1, 2, 3, 4, 5]

        for num in numbers:
            if num == 3:
                break  # exit the loop when num is 3
            elif num == 2:
                continue  # skip num 2 and move on to the next iteration
            else:
                pass  # do nothing for all other values of num
            st.write(f"Result is: {num}")

    elif selected_option == 'If-else statements':
        st.header('If-else statements')
        st.subheader('Example 1')
        "Using an if-else statement to check if a number is even or odd"
        code = """
        num = 4
if num % 2 == 0:
    print('Result: Even')
else:
    print('Result: Odd')

        """
        st.code(code, language='python')
        num = 4
        if num % 2 == 0:
            st.write('Result: Even')
        else:
            st.write('Result: Odd')

        # Example 2: Using an if-else statement to check if a string is uppercase or lowercase
        st.subheader('Example 2')
        "Using an if-else statement to check if a string is uppercase or lowercase"
        code = """
        word = 'Python'
if word.isupper():
    print('Result: Uppercase')
else:
    print('Result: Lowercase')

        """
        st.code(code, language='python')
        word = 'Python'
        if word.isupper():
            st.write('Result: Uppercase')
        else:
            st.write('Result: Lowercase')

        # Example 3: Using an if-else statement to check if a variable is of a certain type
        st.subheader('Example 3')
        "Using an if-else statement to check if a variable is of a certain type"
        code = """
        value = 5
if isinstance(value, int):
    print('Result: Integer')
else:
    print('Result: Not an integer')

        """
        st.code(code, language='python')
        value = 5
        if isinstance(value, int):
            st.write('Result: Integer')
        else:
            st.write('Result: Not an integer')

    elif selected_option == 'While loops':
        st.header('While loops')
        "A while loop is used to repeat a block of code as long as a certain condition is true. The basic syntax of a while loop in Python is:"

        "In this syntax, condition is a Boolean expression that is checked at the beginning of each iteration of the loop. If condition is True, the loop will continue to execute. If condition is False, the loop will terminate."

        st.subheader('Example 1')
        "Using a while loop to print the first five numbers"
        code = """
        i = 1
while i <= 5:
    print(i)
    i += 1

        """
        st.code(code, language='python')
        i = 1
        while i <= 5:
            st.write(f"i is {i}")
            i += 1

        # Example 2: Using a while loop to count down from 10 to 1
        st.subheader('Example 2')
        "Using a while loop to count down from 10 to 1"
        code = """
        i = 10
while i >= 1:
    print(f"i is {i}")
    i -= 1

                """
        st.code(code, language='python')
        i = 10
        while i >= 1:
            st.write(f"i is {i}")
            i -= 1

        # Example 3: Using a while loop to print the first five even numbers
        st.subheader('Example 3')
        "Using a while loop to print the first five even numbers"
        code = """
        i = 0
        count = 0
while count < 5:
    if i % 2 == 0:
        print(i)
        count += 1
    i += 1

        """
        st.code(code, language='python')
        i = 0
        count = 0
        while count < 5:
            if i % 2 == 0:
                st.write(f"{i} is even ")
                count += 1
            i += 1

    elif selected_option == 'List comprehension':
        st.header('List comprehension')

        # Example 1: Using a list comprehension to create a list of even numbers from 1 to 10
        st.subheader('Example 1')
        "Using a list comprehension to create a list of even numbers from 1 to 10"
        code = """
        even_numbers = [num for num in range(1, 11) if num % 2 == 0]
        """
        st.code(code, language='python')
        even_numbers = [num for num in range(1, 11) if num % 2 == 0]
        st.write(even_numbers)
        # Example 2: Using a list comprehension to create a list of squared numbers from 1 to 5
        st.subheader('Example 2')
        "Using a list comprehension to create a list of squared numbers from 1 to 5"
        code = """
        squared_numbers = [num ** 2 for num in range(1, 6)]
        """
        st.code(code, language='python')
        squared_numbers = [num ** 2 for num in range(1, 6)]
        st.write(squared_numbers)

        # Example 3: Using a list comprehension to create a list of words that start with a vowel
        st.subheader('Example 3')
        "Using a list comprehension to create a list of words that start with a vowel"
        code = """
        words = ['apple', 'banana', 'orange', 'pear', 'kiwi']
vowel_words = [word for word in words if word[0] in 'aeiou']
        """
        st.code(code, language='python')
        words = ['apple', 'banana', 'orange', 'pear', 'kiwi']
        vowel_words = [word for word in words if word[0] in 'aeiou']
        st.write(vowel_words)

    elif selected_option == 'Dictionaries':
        st.header('Dictionaries')

        # Example 1: Creating a dictionary of names and ages
        st.subheader('Example 1')
        "Creating a dictionary of names and ages"
        code = """
        names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
age_dict = {name: age for name, age in zip(names, ages)}
        """
        st.code(code, language='python')
        names = ['Alice', 'Bob', 'Charlie']
        ages = [25, 30, 35]
        age_dict = {name: age for name, age in zip(names, ages)}
        st.write(age_dict)

        # Example 2: Modifying values in a dictionary
        st.subheader('Example 2')
        "Modifying values in a dictionary"
        code = """
        fruit_counts = {'apple': 2, 'banana': 3, 'orange': 1}
print(fruit_counts)
fruit_counts['banana'] = 5
        """
        st.code(code, language='python')
        fruit_counts = {'apple': 2, 'banana': 3, 'orange': 1}
        st.write(fruit_counts)
        fruit_counts['banana'] = 5
        st.write(fruit_counts)

        # Example 3: Using a dictionary to count the frequency of words in a string
        st.subheader('Example 3')
        "Using a dictionary to count the frequency of words in a string"
        code = """
        word_freq = {}
for word in sentence.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
                """
        st.code(code, language='python')
        sentence = 'the quick brown fox jumps over the lazy dog'
        word_freq = {}
        for word in sentence.split():
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        st.write(word_freq)

elif selected_main_topic == "Introduction to Pandas":

    # Define the sidebar options
    options = ['Introduction', 'DataFrames', 'Data Selection', 'Data Cleaning', 'Data Aggregation', 'Data Visualization']
    option = st.sidebar.radio("Select an Topic:", options)

    # Define the function to render the selected option

    if option == 'Introduction':
        st.title('Inspired by Miuul.')

        "This open-source web applications is prepared by Hakan Keskin. Miuul and 11. Term Data Science and Machine Learning Bootcamp inspired me" \
        "to prepare the this content develop with the other Data Science Enthusiast."


        "Source code can be seen in my GitHub Account: https://github.com/KeskinHakan"

        st.title('Introduction to Pandas')
        st.write('Pandas is a powerful open-source data analysis and manipulation library for Python.')
        st.write(
            'It provides data structures for efficiently storing and manipulating large datasets, as well as tools for reading and writing data from and to various file formats.')
        st.write('In this tutorial, we will cover some of the basic concepts and operations of Pandas.')
        "Lets start the import related libraries."

        code = """
    import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
    
                """
        st.code(code, language='python')

    elif option == 'DataFrames':
        st.title('DataFrames in Pandas')
        st.write(
            'A DataFrame is a two-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects.')
        st.write('Here are some examples of how to create and manipulate DataFrames:')

        # Example 1: Creating a DataFrame from a dictionary
        data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40],
                'salary': [50000, 60000, 70000, 80000]}
        df = pd.DataFrame(data)
        st.subheader('Example 1: Creating a DataFrame from a dictionary')
        code = """
            data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40], 
                'salary': [50000, 60000, 70000, 80000]}
    df = pd.DataFrame(data)
    
            """
        st.code(code, language='python')
        st.write(df)

        # Example 2: Reading a CSV file into a DataFrame
        file_path = 'data.csv'
        df2 = pd.read_csv(file_path)
        st.subheader('Example 2: Reading a CSV file into a DataFrame')
        code = """
            file_path = 'data.csv'
    df2 = pd.read_csv(file_path)
    
                """
        st.code(code, language='python')
        st.write(df2.head())


        # Example 3: Adding a new column to a DataFrame

        df['city'] = ['New York', 'Los Angeles', 'Chicago', 'Houston']
        st.subheader('Example 3: Adding a new column to a DataFrame')
        code = """
        df['city'] = ['New York', 'Los Angeles', 'Chicago', 'Houston']
                """
        st.code(code, language='python')
        st.write(df)

        # Example 4: Filtering rows in a DataFrame
        df_filtered = df[df['age'] > 30]
        st.subheader('Example 4: Filtering rows in a DataFrame')
        code = """
        df_filtered = df[df['age'] > 30]
                        """
        st.code(code, language='python')
        st.write(df_filtered)

        # Example 5: Grouping data in a DataFrame
        grouped_df = df.groupby('city').sum()
        st.subheader('Example 5: Grouping data in a DataFrame')
        code = """
    grouped_df = df.groupby('city').sum()
                    """
        st.code(code, language='python')
        st.write(grouped_df)

    elif option == 'Data Selection':
        st.title('Data Selection in Pandas')
        st.write('Pandas provides various methods for selecting subsets of data from a DataFrame.')
        st.write('Here are some examples of how to select data:')

        # Example 1: Selecting columns by name
        data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40],
                'salary': [50000, 60000, 70000, 80000]}
        df = pd.DataFrame(data)
        selected_cols = df[['name', 'salary']]
        st.subheader('Example 1: Selecting columns by name')
        code = """
        data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40],
                'salary': [50000, 60000, 70000, 80000]}
    df = pd.DataFrame(data)
    selected_cols = df[['name', 'salary']]
        """
        st.code(code, language='python')
        st.write(selected_cols)

        # Example 2: Filtering rows by a condition
        filtered_rows = df[df['age'] > 30]
        st.subheader('Example 2: Filtering rows by a condition')
        code = """
        filtered_rows = df[df['age'] > 30]
            """
        st.code(code, language='python')
        st.write(filtered_rows)

        # Example 3: Selecting rows and columns by labels
        selected_rows_and_cols = df.loc[df['age'] > 30, ['name', 'salary']]
        st.subheader('Example 3: Selecting rows and columns by labels')
        code = """
        selected_rows_and_cols = df.loc[df['age'] > 30, ['name', 'salary']]
            """
        st.code(code, language='python')
        st.write(selected_rows_and_cols)

        # Example 4:

        # Selecting rows and columns by index
        selected_rows_and_cols = df.iloc[[1, 3], [0, 2]]
        st.subheader('Example 4: Selecting rows and columns by index')
        code = """
        selected_rows_and_cols = df.iloc[[1, 3], [0, 2]]
            """
        st.code(code, language='python')
        st.write(selected_rows_and_cols)

        # Example 5: Applying a function to a DataFrame
        def convert_salary_to_hourly_rate(salary):
            hourly_rate = salary / 2080
            return hourly_rate

        df['hourly_rate'] = df['salary'].apply(convert_salary_to_hourly_rate)
        st.subheader('Example 5: Applying a function to a DataFrame')
        code = """
        def convert_salary_to_hourly_rate(salary):
            hourly_rate = salary / 2080
            return hourly_rate
    
    df['hourly_rate'] = df['salary'].apply(convert_salary_to_hourly_rate)
            """
        st.code(code, language='python')
        st.write(df)

    elif option == 'Data Cleaning':
        st.title('Data Cleaning in Pandas')
        st.write(
            'Data cleaning is the process of identifying and correcting errors, inconsistencies, and discrepancies in data.')
        st.write('Here are some examples of how to clean data in Pandas:')

        # Example 1: Handling missing values
        data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, None, 35, 40],
                'salary': [50000, 60000, 70000, None]}
        df = pd.DataFrame(data)
        st.subheader('Example 1: Handling missing values')
        code = """
        data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, None, 35, 40],
                'salary': [50000, 60000, 70000, None]}
    df = pd.DataFrame(data)
            """
        st.code(code, language='python')
        st.write(df)
        st.write('Number of missing values:')
        code =  """
        df.isna().sum()
        """
        st.code(code, language='python')
        st.write(df.isna().sum())
        df = df.dropna()
        st.write('After dropping missing values:')
        code =  """
        df = df.dropna()
        """
        st.code(code, language='python')
        st.write(df)

        # Example 2: Renaming columns
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df = df.rename(columns={'A': 'X', 'B': 'Y'})
        st.subheader('Example 2: Renaming columns')
        code =  """
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df = df.rename(columns={'A': 'X', 'B': 'Y'})
        """
        st.code(code, language='python')
        st.write(df)

        # Example 3: Removing duplicates
        df = pd.DataFrame({'A': [1, 1, 2, 3], 'B': [4, 4, 5, 6]})
        df = df.drop_duplicates()
        st.subheader('Example 3: Removing duplicates')
        code = """
        df = pd.DataFrame({'A': [1, 1, 2, 3], 'B': [4, 4, 5, 6]})
    df = df.drop_duplicates()
        """
        st.code(code, language='python')
        st.write(df)

        # Example 4: Changing data types
        df = pd.DataFrame({'A': ['1', '2', '3'], 'B': ['4', '5', '6']})
        df = df.astype({'A': int, 'B': int})
        st.subheader('Example 4: Changing data types')
        code = """
        df = pd.DataFrame({'A': ['1', '2', '3'], 'B': ['4', '5', '6']})
    df = df.astype({'A': int, 'B': int})
        """
        st.code(code, language='python')

        # Example 5: Handling outliers
        df = pd.DataFrame({'A': [1, 2, 3, 100], 'B': [4, 5, 6, 200]})
        q1 = df.quantile(0.25)
        q3 = df.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df = df[(df > lower_bound) & (df < upper_bound)].dropna()
        st.subheader('Example 5: Handling outliers')
        code = """
        df = pd.DataFrame({'A': [1, 2, 3, 100], 'B': [4, 5, 6, 200]})
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df = df[(df > lower_bound) & (df < upper_bound)].dropna()
        """
        st.code(code, language='python')
        st.write(df)

    elif option == 'Data Aggregation':
        st.title('Data Aggregation in Pandas')
        st.write('Aggregation is the process of combining multiple data points into a single summary value.')
        st.write('Here are some examples of how to aggregate data in Pandas:')

        # Example 1: Grouping and aggregating data
        data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40], 'salary': [50000, 60000, 70000, 80000]}
        df = pd.DataFrame(data)
        df_grouped = df.groupby('age').agg({'salary': 'mean'}).reset_index()
        st.subheader('Example 1: Grouping and aggregating data')
        code = """
        data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40], 'salary': [50000, 60000, 70000, 80000]}
    df = pd.DataFrame(data)
    df_grouped = df.groupby('age').agg({'salary': 'mean'}).reset_index()
        """
        st.code(code, language='python')
        st.write(df_grouped)

        # Example 2: Applying multiple aggregation functions
        df_grouped = df.groupby('age').agg({'salary': ['mean', 'min', 'max']}).reset_index()
        df_grouped.columns = ['age', 'mean_salary', 'min_salary', 'max_salary']
        st.subheader('Example 2: Applying multiple aggregation functions')
        code = """
        df_grouped = df.groupby('age').agg({'salary': ['mean', 'min', 'max']}).reset_index()
    df_grouped.columns = ['age', 'mean_salary', 'min_salary', 'max_salary']
        """
        st.code(code, language='python')
        st.write(df_grouped)

        # Example 3: Aggregating with a custom function
        def count_high_salaries(series):
            return len(series[series > 55000])

        df_grouped = df.groupby('age').agg({'salary': count_high_salaries}).reset_index()
        st.subheader('Example 3: Aggregating with a custom function')
        code = """
        def count_high_salaries(series):
            return len(series[series > 55000])
    
    df_grouped = df.groupby('age').agg({'salary': count_high_salaries}).reset_index()
        """
        st.code(code, language='python')
        st.write(df_grouped)

        # Example 4: Grouping by multiple columns
        df_grouped = df.groupby(['age', 'name']).agg({'salary': 'mean'}).reset_index()
        st.subheader('Example 4: Grouping by multiple columns')
        code = """
        df_grouped = df.groupby(['age', 'name']).agg({'salary': 'mean'}).reset_index()
        """
        st.code(code, language='python')
        st.write(df_grouped)

        # Example 5: Pivoting data
        df_pivot = pd.pivot_table(df, values='salary', index='name', columns='age', fill_value=0)
        st.subheader('Example 5: Pivoting data')
        code = """
        df_pivot = pd.pivot_table(df, values='salary', index='name', columns='age', fill_value=0)
        """
        st.code(code, language='python')
        st.write(df_pivot)

    elif option == 'Data Visualization':
        st.title('Data Visualization in Pandas')
        st.write(
            'Data visualization is the process of creating visual representations of data to help communicate insights and findings.')
        st.write('Here are some examples of how to visualize data in Pandas:')

        # Example 1: Line plot
        data = {'year': [2010, 2011, 2012, 2013, 2014], 'sales': [100, 120, 150, 200, 250]}
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax.plot(df['year'], df['sales'])
        ax.set_xlabel('Year')
        ax.set_ylabel('Sales')
        st.subheader('Example 1: Line plot')
        code = """
        data = {'year': [2010, 2011, 2012, 2013, 2014], 'sales': [100, 120, 150, 200, 250]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.plot(df['year'], df['sales'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Sales')
        """
        st.code(code, language='python')
        st.pyplot(fig)

        # Example 2: Bar chart
        data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'salary': [50000, 60000, 70000, 80000]}
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax.bar(df['name'], df['salary'])
        ax.set_xlabel('Name')
        ax.set_ylabel('Salary')
        st.subheader('Example 2: Bar chart')
        code = """
        data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'salary': [50000, 60000, 70000, 80000]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.bar(df['name'], df['salary'])
    ax.set_xlabel('Name')
    ax.set_ylabel('Salary')
            """
        st.code(code, language='python')
        st.pyplot(fig)

        # Example 3: Histogram
        data = {'age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
                'salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]}
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax.hist(df['age'], bins=5)
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        st.subheader('Example 3: Histogram')
        code = """
        data = {'age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
                'salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.hist(df['age'], bins=5)
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
                """
        st.code(code, language='python')
        st.pyplot(fig)

        # Example 4: Scatter plot
        data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax.scatter(df['x'], df['y'])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        st.subheader('Example 4: Scatter plot')
        code = """
        data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.scatter(df['x'], df['y'])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
                    """
        st.code(code, language='python')
        st.pyplot(fig)

        # Example 5: Box plot
        data = {'group': ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C'], 'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax.boxplot([df[df['group'] == 'A']['value'], df[df['group'] == 'B']['value'], df[df['group'] == 'C']['value']])
        ax.set_xticklabels(['Group A', 'Group B', 'Group C'])
        ax.set_ylabel('Value')
        st.subheader('Example 5: Box plot')
        code = """
        data = {'group': ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C'], 'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.boxplot([df[df['group'] == 'A']['value'], df[df['group'] == 'B']['value'], df[df['group'] == 'C']['value']])
    ax.set_xticklabels(['Group A', 'Group B', 'Group C'])
    ax.set_ylabel('Value')
                        """
        st.code(code, language='python')
        st.pyplot(fig)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

