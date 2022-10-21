import time
import pandas as pd
import numpy as np
from pathlib import Path
import datetime
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    input_city = input('What city? C for Chicago, N for New York City or W for Washington \n')

    # get user input for month (all, january, february, ... , june)
    input_month = input('What month? enter the number for the month, eg 1 for January, 12 for December. Or "all" for no filter. \n')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    input_day = input('What day of week? 1 enter the number for the weekday where Monday is 1 and Sunday 7. Or "all" for no filter. \n')


    print('-'*40)
    return input_city, input_month, input_day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filepath = Path(__file__)
    data = {
        "W":Path(f"{filepath.parent}/washington.csv"),
        "C":Path(f"{filepath.parent}/chicago.csv"),
        "N":Path(f"{filepath.parent}/new_york_city.csv"),
    }

    df = pd.read_csv(data[city].as_posix())

    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d')
    
    if month != "all":
        month_filter = df["Start Time"].dt.month == int(month)
        df = df.loc[month_filter]
    if day != "all":
        day_filter = df["Start Time"].dt.weekday+1 == int(day)
        df = df.loc[day_filter]

    return df


def time_stats(df:pd.DataFrame):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = calendar.month_name[int(df["Start Time"].dt.month.mode().to_string(index=False))]
    print(f"The most common month was : {most_common_month}")

    # display the most common day of week
    most_common_day = calendar.day_name[int(df["Start Time"].dt.day_of_week.mode().to_string(index=False))]
    print(f"The most common day of the week was : {most_common_day}")

    # display the most common start hour
    most_common_hour = f'{df["Start Time"].dt.hour.mode().to_string(index=False)}:00'
    print(f"The most common start hour was : {most_common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df:pd.DataFrame):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start =df["Start Station"].mode().to_string(index=False)
    print(f"Most common start station was : {most_common_start}")

    # display most commonly used end station
    most_common_end = df["End Station"].mode().to_string(index=False)
    print(f"Most common end station was : {most_common_end}")


    # display most frequent combination of start station and end station trip
    start, end = df.groupby(["Start Station", "End Station"]).size().idxmax()
    print(f"Most frequent combination of start and end station was : {start} - {end}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df:pd.DataFrame):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    df['End Time'] = pd.to_datetime(df['End Time'], format='%Y-%m-%d %H:%M:%S')

    total = (df['End Time'] - df['Start Time']).sum()
    print(f"Total travel time was : {total}")


    # display mean travel time
    mean = (df['End Time'] - df['Start Time']).mean()
    print(f"Mean travel time was : {mean}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df:pd.DataFrame):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df["User Type"].value_counts().rename_axis('User Types').reset_index(name='count'))

    print("\n")

    # Display counts of gender
    print(df["Gender"].value_counts().rename_axis('Gender').reset_index(name='count'))

    print("\n")

    # Display earliest, most recent, and most common year of birth
    earliest_year = int(df["Birth Year"].min())
    most_recent_year = int(df["Birth Year"].max())
    most_common_year = int(df["Birth Year"].mode().to_string(index=False)[0:-2])
    print(f"Earliest Birth Year : {earliest_year}\nMost recent Birth Year : {most_recent_year}\nMost common birth year : {most_common_year}")

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
