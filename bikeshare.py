import time
import pandas as pd
import numpy as np

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
    # Get user input for city (chicago, new york city, washington).
    while True:
        city = input('\nWould you like to see data from Chicago, New York City or Washington?\n').lower()
        if city in ['chicago','new york city','washington']:
            break
        else:
            print('\n Please input a valid city.\n')

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWould you like to filter the data by month(From January to June)?If not just type "all"\n').title()
        if month in ['January','February','March','April','May','June','All']:
            break
        else:
            print('\nPlease input a valid month from January to June. Type "all" if you do not have any preference.\n')



    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWould you like to filter by day? You can choose from Monday to Sunday or just type "all" if you have no preference\n').title()
        if day in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']:
            break
        else:
            print('\n Pleas input a valid day of the week or type "all" if you have no preference.\n')
    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    print('\n The most common month is: ',popular_month)

    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\n The most common day of the week is: ',popular_day)

    # Display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\n The most common start hour is: ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('\nThe most commont start station is: ',popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('\nThe most common end station is: ',popular_end_station)

    # Display most frequent combination of start station and end station trip
    popular_station_combinations = df.groupby(['Start Station','End Station']).size().idxmax()

    print('\n The most common station combination is:\n ',popular_station_combinations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time: ',total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser Types: ',user_types)

    # Display counts of gender (Only available for Chicago and New York City files)
    try:
        user_genders = df['Gender'].value_counts()
        print('\nUser genders: ',user_genders)
    except KeyError:
        print('\nNo gender information in this city')

    #Display earliest, most recent, and most common year of birth (Only available for Chicago and New York City files)
    try:
        earliest_birth_year = df['Birth Year'].min()
        latest_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('\nEarliest birth year: ',earliest_birth_year)
        print('\nLatest birth year: ',latest_birth_year)
        print('\nMost common birth year: ', common_birth_year)
    except KeyError:
        print('\nNo birth year information in this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Shows trip data in rows of five if user chooses to do so."""
    start_loc = 0
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input('Do you wish to continue?: ').lower()
        view_data=view_display

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
