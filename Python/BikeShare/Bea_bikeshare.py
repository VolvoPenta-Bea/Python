import pandas as pd
import numpy as np
import time as t
import calendar as c
from pathlib import Path

csv_files = {'C', 'chicago.csv', 'N', 'new_york_city.csv', 'W', 'washington.csv'}

def users_input()

    print('Hello! Let\'s explore some US bikeshare data!', 'yellow', 'on_grey')

    while True:
        try:
            city = input(bcolors.HEADER + 'What city? C for Chicago, N for New York City or W for Washington \n')
            if city.upper() == 'C' or city.upper() == 'N' or city.upper() == 'W':
                break
            elif city.isdigit():
                cprint(f'Enter the letter C, N or W not a number', 'magenta')
            else:
                print(bcolors.FAIL + 'Only the first letter')
        except ValueError:
            print(bcolors.FAIL + 'Somethings gone wrong here')

    while True:
        try:
            month = input(
                bcolors.HEADER + 'What month? enter the number for the month, eg 1 for January, 6 for June. Or \'all\' for no filter. \n')
            if month == '1' or month == '2' or month == '3' or month == '4' or month == '5' or month == '6':
                break
            elif city.lower() == 'all':
                break
            else:
                print(
                    bcolors.FAIL + 'You can only type numbers 1-6 or all. This statistic can not show data for July to December')
        except ValueError:
            print(bcolors.FAIL + 'This input only accept 1-6 or the word all')

    while True:
        try:
            day = input(
                bcolors.HEADER + 'What day of week? enter the number for the weekday where Monday is 1 and Sunday 7. Or \'all\' for no filter. \n')
            if day == '1' or day == '2' or day == '3' or day == '4' or day == '5' or day == '6' or day == '7':
                break
            elif day.lower() == 'all':
                break
            else:
                print(bcolors.FAIL + 'You can only type numbers 1-7 or all.')
        except ValueError:
            print(bcolors.FAIL + 'This input only accept 1-7 or the word all')

    print('-' * 40)
    return city.upper(), month, day

def load_data (city, month, day):

    filepath = Path(__file__)
    data = {
        "W": Path(f"{filepath.parent}/washington.csv"),
        "C": Path(f"{filepath.parent}/chicago.csv"),
        "N": Path(f"{filepath.parent}/new_york_city.csv"),
    }

    df = pd.read_csv(data[city].as_posix())

    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d')

    if month != "all":
        month_filter = df["Start Time"].dt.month == int(month) # dt.month : The month as January=1, December=12. int to convert str to number
        df = df.loc[month_filter] # Access a group of rows and columns by label(s) or a boolean array.
    if day != "all":
        day_filter = df["Start Time"].dt.weekday + 1 == int(day) # + 1 because default is Monday = 0 not 1
        df = df.loc[day_filter]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = calendar

    print('Most common month was'+ {most_common_month})

    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


if __name__ == "__main__":
	main()
