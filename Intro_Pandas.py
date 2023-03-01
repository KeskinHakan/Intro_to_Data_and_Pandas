import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Set page title
st.set_page_config(page_title='Pandas Tutorial')

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
