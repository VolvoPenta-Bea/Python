import pandas as pd
import numpy as np


df = pd.read_csv('chicago.csv')

# converting column data to list - .must be a better way - eg access directly
start_time = df['Start Time'].tolist()
start_time = pd.to_datetime(start_time)
end_time = df['End Time'].tolist()
start_station = df['Start Station'].tolist()
end_station = df['End Station'].tolist()
user_type = df['User Type'].tolist()
gender = df['Gender'].tolist()
birth_year = df['Birth Year'].tolist()

def function_input_test():
    while True:
        try:
            input_city = input('What city? C for Chicago, N for New York City or W for Washington')
        except:
            print('thats not right')
        finally:
            print('wow')
        return input_city

# printing list data
function_input_test()
