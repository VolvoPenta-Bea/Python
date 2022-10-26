import time
import pandas as pd
import numpy as np
import datetime
import calendar

# instead of import citydata I use pathlib, tip from friend
import pathlib
import calendar

# With some color I find it easier to read the output
import sys
from termcolor import colored, cprint


class bcolors:
    HEADER = '\033[94m'
    FAIL = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_filters():
    '''
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 'all' to apply no month filter
        (str) day - name of the day of week to filter by, or 'all' to apply no day filter
    '''
    # I use f strings as from this source: https: // realpython.com / python - f - strings /
    cprint('Hello! Let\'s explore some US bikeshare data!','yellow', 'on_grey')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            input_city = input(bcolors.HEADER + 'What city? C for Chicago, N for New York City or W for Washington \n')
            if input_city.upper() == 'C' or input_city.upper() == 'N' or input_city.upper() == 'W':
                break
            elif input_city.isdigit():
                cprint(f'Enter the letter C, N or W not a number', 'magenta')
            else:
                print(bcolors.FAIL + 'Only the first letter')
        except ValueError:
            print(bcolors.FAIL + 'Somethings gone wrong here')

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            input_month = input(bcolors.HEADER + 'What month? enter the number for the month, eg 1 for January, 6 for June. Or all for no filter. \n')
            if type(input_month) == int and input_month >= 6:
                break
            elif input_city.lower() == 'all':
                break
            else:
                print(bcolors.FAIL + 'You can only type numbers 1-6 or all. This statistic can not show data for July to December')
        except ValueError:
            print(bcolors.FAIL + 'This input only accept 1-6 or the word all')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            input_day = input(bcolors.HEADER + 'What day of week? enter the number for the weekday where Monday is 1 and Sunday 7. Or all for no filter. \n')
            if type(input_day) == int and input_day >= 7:
                break
            elif input_day.lower() == 'all':
                break
            else:
                print(bcolors.FAIL + 'You can only type numbers 1-7 or all.')
        except ValueError:
            print(bcolors.FAIL + 'This input only accept 1-7 or the word all')

    print('-' * 40)
    return input_city, input_month, input_day


def load_data(city, month, day):
    '''
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 'all' to apply no month filter
        (str) day - name of the day of week to filter by, or 'all' to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day

        Comment: pathlib not part of course. Got this tip from friend
    '''
    # load data with path
    filepath = pathlib.Path(__file__)
    data = {
        'W': pathlib.Path(f'{filepath.parent}/washington.csv'),
        'C': pathlib.Path(f'{filepath.parent}/chicago.csv'),
        'N': pathlib.Path(f'{filepath.parent}/new_york_city.csv'),
    }
    # convert to posix parameter
    df = pd.read_csv(data[city].as_posix())

    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d')

    if month != 'all':
        month_filter = df['Start Time'].dt.month == int(month)
        df = df.loc[month_filter]
    if day != 'all':
        day_filter = df['Start Time'].dt.weekday + 1 == int(day)
        df = df.loc[day_filter]

    return df


def time_stats(df: pd.DataFrame):
    '''Displays statistics on the most frequent times of travel.'''

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = calendar.month_name[int(df['Start Time'].dt.month.mode().to_string(index=False))]
    print('The most common month was : {most_common_month}')

    # display the most common day of week
    most_common_day = calendar.day_name[int(df['Start Time'].dt.day_of_week.mode().to_string(index=False))]
    print('The most common day of the week was : {most_common_day}')

    # display the most common start hour
    most_common_hour = '{df['Start Time'].dt.hour.mode().to_string(index=False)}:00'
    print(f'The most common start hour was : {most_common_hour}')

    print(f'\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def station_stats(df: pd.DataFrame):
    '''Displays statistics on the most popular stations and trip.'''

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode().to_string(index=False)
    print(f'Most common start station was : {most_common_start}')

    # display most commonly used end station
    most_common_end = df['End Station'].mode().to_string(index=False)
    print(f'Most common end station was : {most_common_end}')

    # display most frequent combination of start station and end station trip
    start, end = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'Most frequent combination of start and end station was : {start} - {end}')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df: pd.DataFrame):
    '''Displays statistics on the total and average trip duration.'''

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    df['End Time'] = pd.to_datetime(df['End Time'], format='%Y-%m-%d %H:%M:%S')

    total = (df['End Time'] - df['Start Time']).sum()
    print(f'Total travel time was : {total}')

    # display mean travel time
    mean = (df['End Time'] - df['Start Time']).mean()
    print(f'Mean travel time was : {mean}')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def user_stats(df: pd.DataFrame):
    '''Displays statistics on bikeshare users.'''

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        # Display counts of user types
        print(df['User Type'].value_counts().rename_axis('User Types').reset_index(name='count'))
    except KeyError:
        print('No user type data to display.')

    print('\n')

    # Display counts of gender
    try:
        print(df['Gender'].value_counts().rename_axis('Gender').reset_index(name='count'))
    except KeyError:
        print('No gender data to display.')

    print('\n')

    try:
        # Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode().to_string(index=False)[0:-2])
        print(
            f'Earliest Birth Year : {earliest_year}\nMost recent Birth Year : {most_recent_year}\nMost common birth year : {most_common_year}')
    except KeyError:
        print('No Birt Year Data to display.')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-' * 40)


def main() -> object:
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == '__main__':
    main()
