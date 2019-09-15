<<<<<<< HEAD
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

# Modified print-statements
def print_pause_a(message_to_print):
    print(message_to_print)
    time.sleep(1.0)
def print_pause_b(message_to_print):
    print(message_to_print)
    time.sleep(0.5)

# Providing input for main-function
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print_pause_a('Hello! Let\'s explore some US bikeshare data!')
    print_pause_a('')

# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please choose a business location to analyze:\nType (1)Chicago, (2)New York City, (3)Washington\n')
        city = city.lower()
# Improve usability through multiple options for the same city
        if city == 'chicago' or city == '1':
            city = 'Chicago'
            break
        if city == 'new york' or city == 'new york city' or city == '2':
            city = 'New York City'
            break
        elif city == 'washington' or city == 'washington dc' or city == '3':
            city = 'Washington'
            break
# 'Safety net' if no valid input is given to the function
        else:
            print_pause_a('Please select one of the given possibilities.')
            get_filters()
    print_pause_a('You have chosen ' + city + ' as a filter . Please continue..')
    print_pause_a('')

# TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('Would you like to filter the data by month? If not please choose all.\nType (1) January, (2) February, (3) March, (4) April, (5) May, (6) June (7) all\n')
        month = month.lower()
# Improve usability through multiple options for the same month
        if month == '1' or month == 'january' or month == 'jan':
            month = 'January'
            break
        elif month == '2' or month == 'february' or month == 'feb':
            month = 'February'
            break
        elif month == '3' or month == 'march' or month == 'mar':
            month = 'March'
            break
        elif month == '4' or month == 'april' or month == 'apr':
            month = 'April'
            break
        elif month == '5' or month == 'may':
            month = 'May'
            break
        elif month == '6' or month == 'june'or month == 'jun':
            month = 'June'
            break
        elif month == '7' or month == 'all'or month == 'jul':
            month = 'all'
            break
# 'Safety net' if no valid input is given to the function
        else:
            print_pause_a('Please select one of the given possibilities.')
            get_filters()
    print_pause_a('You have chosen ' + month + ' as a filter . Please continue..')
    print_pause_a('')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Would you like to filter the data by day? If not please choose all.\nType (1) Monday, (2)Tuesday, (3)Wednesday, (4)Thursday, (5)Friday, (6)Saturday, (7)Sunday, (8) all\n')
        day = day.lower()
# Improve usability through multiple options for the same day
        if day == '1' or day == 'monday' or day == 'mon':
            day = 'Monday'
            break
        elif day == '2' or day == 'tuesday' or day == 'tue':
            day = 'Tuesday'
            break
        elif day == '3' or day == 'wednesday' or day == 'wed':
            day = 'Wednesday'
            break
        elif day == '4' or day == 'thursday' or day == 'thu':
            day = 'Thursday'
            break
        elif day == '5' or day == 'friday' or day == 'fri':
            day = 'Friday'
            break
        elif day == '6' or day == 'saturday' or day == 'sat':
            day = 'Saturday'
            break
        elif day == '7' or day == 'sunday' or day == 'sun':
            return day
        elif day == '8' or day == 'all':
            day = 'all'
            break
# 'Safety net' if no valid input is given to the function
        else:
            print_pause('Please select one of the given possibilities.')
            get_filters()
    print_pause_a('You have chosen ' + day + ' as a filter.')
    print_pause_a('')
    print_pause_a('You\'re dataset is being processed')
    print_pause_b('-'*40)
# Returning user input for further processing
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
# Choose data from provided csv according to user input provided by respective function and create a dataset (city)
    df = pd.read_csv(CITY_DATA[city])
# Preparing for .dt.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# Creating additional columns for month & day to prepare for respective requests
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
# Choose data according to user input provided by respective function (month)
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
# create a adjusted dataset
        df = df[df['month'] == month]
# Choose data according to user input provided by respective function (day)
    if day != 'all':
# create a adjusted dataset
        df = df[df['day'] == day.title()]
# return dataset as requested by user
    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print_pause_b('Calculating the most frequent times of travel...\n')
# Needed later on to determine how long it took to make the calculation
    start_time = time.time()
# TO DO: display the most common month
    most_popular_month = df['month'].mode()[0]
    print_pause_b(('Most popular month:', most_popular_month))
# TO DO: display the most common day of week
    most_popular_day = df['day'].mode()[0]
    print_pause_b(('Most popular day:', most_popular_day))
# TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_popular_hour = df['hour'].mode()[0]
    print_pause_b(('Most popular hour:', most_popular_hour))
# How long did the calculation take
    print_pause_b('This took %s seconds.' % (time.time() - start_time))
    print_pause_b('-'*40)

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print_pause_b('Calculating the most popular stations and trip...\n')
# Needed later on to determine how long it took to make the calculation
    start_time = time.time()
# TO DO: display most commonly used start station with Pandas .idxmax()
    most_popular_start_station = df['Start Station'].value_counts().idxmax()
    print_pause_b(('Most commonly used start station:', most_popular_start_station))
# TO DO: display most commonly used end station with Pandas .idxmax()
    most_popular_end_station = df['End Station'].value_counts().idxmax()
    print_pause_b(('Most commonly used end station:', most_popular_end_station))
# TO DO: display most frequent combination of start station and end station trip
    most_popular_combination_station = df.groupby(['Start Station', 'End Station']).count()
    print_pause_b(('Most frequent combination of start station and end station trip:', most_popular_start_station, " & ", most_popular_end_station))
# How long did the calculation take
    print_pause_b('This took %s seconds.' % (time.time() - start_time))
    print_pause_b('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print_pause_b('Calculating trip duration...\n')
# Needed later on to determine how long it took to make the calculation
    start_time = time.time()
# TO DO: display total travel time (sec to day /(24*60*60))
    total_travel_time = sum(df['Trip Duration'])
    print_pause_b(('Total travel time:', total_travel_time/86400, ' days'))
# TO DO: display mean travel time (sec to min /60)
    mean_travel_time = df['Trip Duration'].mean()
    print_pause_b(('Mean travel time:', mean_travel_time/60, ' minutes'))
# How long did the calculation take
    print_pause_b(('This took %s seconds.' % (time.time() - start_time)))
    print_pause_b('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""

    print_pause_b('Calculating user stats...\n')
# Needed later on to determine how long it took to make the calculation
    start_time = time.time()
# TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print_pause_b(('Counts of user Types:\n', count_user_types))
# TO DO: Display counts of gender
    try:
      count_gender = df['Gender'].value_counts()
      print_pause_b(('Counts of gender:\n', count_gender))
    except KeyError:
      print_pause_b('Counts of gender:\nData not available.')
# TO DO: Display earliest year of birth
    try:
      earliest_year_birth = df['Birth Year'].min()
      print_pause_b(('Earliest year of birth:', earliest_year_birth))
    except KeyError:
      print_pause_b('Earliest year of birth:\nData not available.')
# TO DO: Display most recent year of birth
    try:
      most_recent_year_birth = df['Birth Year'].max()
      print_pause_b(('Most recent year of birth:', most_recent_year_birth))
    except KeyError:
      print_pause_b('Most recent year of birth:\nData not available.')
# TO DO: Display  most common year of birth
    try:
      most_common_year_birth = df['Birth Year'].value_counts().idxmax()
      print_pause_b(('Most common year of birth:', most_common_year_birth))
    except KeyError:
      print_pause_b('Most common year of birth:\nData not available.')
# How long did the calculation take
    print_pause_b(('This took %s seconds.' % (time.time() - start_time)))
    print_pause_b('-'*40)

# Improve usability by providing the option of creating further surveys
def restart_survey():
    print_pause_a('Do you want to create another survey?')
    restart = input('y/n\n')
    if restart == 'y':
        main()
# Ending the program if no futher surveys are needed
    elif restart == 'n':
        print_pause_a('Thank you for using this data analysis tool!')
        exit()
# 'Safety net' if no valid input is given to the function
    else:
        print_pause_a('Sorry I don\'t understand-please try again')
        restart_survey()


# main function that combines the predefined functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart_survey()

# checking if this is the main program
if __name__ == "__main__":
	main()
||||||| merged common ancestors
=======
# Submitted 
import time
import pandas as pd
import numpy as np


CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

# Modified print-statements
def print_pause_a(message_to_print):
    print(message_to_print)
    time.sleep(1.0)

def print_pause_b(message_to_print):
    print(message_to_print)
    time.sleep(0.5)

# TO DO: display the most common month
def popular_month(df):
    most_popular_month = df['month'].mode()[0]
    print('Most popular month:', most_popular_month)

# TO DO: display the most common day of week
def popular_day(df):
    most_popular_day = df['day'].mode()[0]
    print('Most popular day:', most_popular_day)

# TO DO: display the most common start hour
def popular_hour(df):
    df['hour'] = df['Start Time'].dt.hour
    most_popular_hour = df['hour'].mode()[0]
    print('Most popular start hour:', most_popular_hour)

# TO DO: display most commonly used start station with Pandas .idxmax()
def popular_start_station(df):
    most_popular_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', most_popular_start_station)

# TO DO: display most commonly used end station with Pandas .idxmax()
def popular_end_station(df):
    most_popular_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station:', most_popular_end_station)

# TO DO: display most frequent combination of start station and end station trip
def popular_combination_station(df):
    most_popular_start_station = df['Start Station'].value_counts().idxmax()
    most_popular_end_station = df['End Station'].value_counts().idxmax()
    most_popular_combination_station = df.groupby(['Start Station', 'End Station']).count()
    print('Most frequent combination of start station and end station trip:', most_popular_start_station, " & ", most_popular_end_station)

# TO DO: display mean travel time (sec to min /60)
def mean_travel(df):
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/60, ' minutes')

# TO DO: display total travel time (sec to day /(24*60*60))
def total_travel(df):
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time/86400, ' days')

# TO DO: Display counts of user types
def count_user(df):
    count_user_types = df['User Type'].value_counts()
    print('Counts of user Types:', count_user_types)

# TO DO: Display counts of gender
def count_gender(df):
    try:
      count_gender = df['Gender'].value_counts()
      print('Counts of gender:\n', count_gender)
    except KeyError:
      print_pause_b('Counts of gender:\nData not available.')

# TO DO: Display earliest year of birth
def earliest_birth(df):
    try:
      earliest_year_birth = df['Birth Year'].min()
      print('Earliest year of birth:', earliest_year_birth)
    except KeyError:
      print('Earliest year of birth:\nData not available.')

# TO DO: Display most recent year of birth
def recent_birth(df):
    try:
      most_recent_year_birth = df['Birth Year'].max()
      print('Most recent year of birth:', most_recent_year_birth)
    except KeyError:
      print('Most recent year of birth:\nData not available.')

# TO DO: Display  most common year of birth
def common_birth(df):
    try:
      most_common_year_birth = df['Birth Year'].value_counts().idxmax()
      print('Most common year of birth:', most_common_year_birth)
    except KeyError:
      print('Most common year of birth:\nData not available.')

# Providing input for main-function
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print_pause_a('Hello! Let\'s explore some US bikeshare data!')
    print_pause_a('')

# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please choose a business location to analyze:\nType (1)Chicago, (2)New York City, (3)Washington\n')
        city = city.lower()
# Improve usability through multiple options for the same city
        if city == 'chicago' or city == '1':
            city = 'Chicago'
            break
        if city == 'new york' or city == 'new york city' or city == '2':
            city = 'New York City'
            break
        elif city == 'washington' or city == 'washington dc' or city == '3':
            city = 'Washington'
            break
# 'Safety net' if no valid input is given to the function
        else:
            print_pause_a('Please select one of the given possibilities.')
            get_filters()
    print_pause_a('You have chosen ' + city + ' as a filter . Please continue..')
    print_pause_a('')

# TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to filter the data by month? If not please choose all.\nType (1) January, (2) February, (3) March, (4) April, (5) May, (6) June (7) all\n')
        month = month.lower()
# Improve usability through multiple options for the same month
        if month == '1' or month == 'january' or month == 'jan':
            month = 'January'
            break
        elif month == '2' or month == 'february' or month == 'feb':
            month = 'February'
            break
        elif month == '3' or month == 'march' or month == 'mar':
            month = 'March'
            break
        elif month == '4' or month == 'april' or month == 'apr':
            month = 'April'
            break
        elif month == '5' or month == 'may':
            month = 'May'
            break
        elif month == '6' or month == 'june'or month == 'jun':
            month = 'June'
            break
        elif month == '7' or month == 'all'or month == 'jul':
            month = 'all'
            break
# 'Safety net' if no valid input is given to the function
        else:
            print_pause_a('Please select one of the given possibilities.')
            get_filters()
    print_pause_a('You have chosen ' + month + ' as a filter . Please continue..')
    print_pause_a('')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Would you like to filter the data by day? If not please choose all.\nType (1) Monday, (2)Tuesday, (3)Wednesday, (4)Thursday, (5)Friday, (6)Saturday, (7)Sunday, (8) all\n')
        day = day.lower()
# Improve usability through multiple options for the same day
        if day == '1' or day == 'monday' or day == 'mon':
            day = 'Monday'
            break
        elif day == '2' or day == 'tuesday' or day == 'tue':
            day = 'Tuesday'
            break
        elif day == '3' or day == 'wednesday' or day == 'wed':
            day = 'Wednesday'
            break
        elif day == '4' or day == 'thursday' or day == 'thu':
            day = 'Thursday'
            break
        elif day == '5' or day == 'friday' or day == 'fri':
            day = 'Friday'
            break
        elif day == '6' or day == 'saturday' or day == 'sat':
            day = 'Saturday'
            break
        elif day == '7' or day == 'sunday' or day == 'sun':
            day = 'Sunday'
            break
        elif day == '8' or day == 'all':
            day = 'all'
            break
# 'Safety net' if no valid input is given to the function
        else:
            print_pause_a('Please select one of the given possibilities.')
            get_filters()
    print_pause_a('You have chosen ' + day + ' as a filter.')
    print_pause_a('')
    print_pause_a('You\'re dataset is being processed')
    print_pause_b('-'*40)
# Returning user input for further processing
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
# Choose data from provided csv according to user input provided by respective function and create a dataset (city)
    df = pd.read_csv(CITY_DATA[city])
# Preparing for .dt.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# Creating additional columns for month & day to prepare for respective requests
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
# Choose data according to user input provided by respective function (month)
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
# create a adjusted dataset
        df = df[df['month'] == month]
# Choose data according to user input provided by respective function (day)
    if day != 'all':
# create a adjusted dataset
        df = df[df['day'] == day.title()]
# return dataset as requested by user
    return df
# Give the user the opportunity to see the raw data
def raw_data(df):
    display_data = input('Do you want to see the first 5 rows which are going to be used for the calculation?\ny/n\n')
    display_data = display_data.lower()
    index = 0
    while True:
        if display_data == 'n':
            print_pause_a('The programm will now go on with the calculation')
            break
        elif display_data == 'y':
            print(df[index: index + 5])
            index = index + 5
            display_data = input('Do you want to see the the next 5 rows which are going to be used for the calculation?\ny/n\n')
            display_data = display_data.lower()
# 'Safety net' if no valid input is given to the function
        else:
            print_pause_a('Sorry I don\'t understand-please try again')
            raw_data(df)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print_pause_b('Calculating the most frequent times of travel...\n')
# Needed later on to determine how long it took to make the calculation
    start_time = time.time()
    popular_month(df)
    popular_day(df)
    popular_hour(df)
# How long did the calculation take
    print_pause_b('This took %s seconds.' % (time.time() - start_time))
    print_pause_b('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print_pause_b('Calculating the most popular stations and trip...\n')
# Needed later on to determine how long it took to make the calculation
    start_time = time.time()
    popular_start_station(df)
    popular_end_station(df)
    popular_combination_station(df)
# How long did the calculation take
    print_pause_b('This took %s seconds.' % (time.time() - start_time))
    print_pause_b('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print_pause_b('Calculating trip duration...\n')
# Needed later on to determine how long it took to make the calculation
    start_time = time.time()
    total_travel(df)
    mean_travel(df)
# How long did the calculation take
    print_pause_b(('This took %s seconds.' % (time.time() - start_time)))
    print_pause_b('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print_pause_b('Calculating user stats...\n')
# Needed later on to determine how long it took to make the calculation
    start_time = time.time()
    count_user(df)
    count_gender(df)
    earliest_birth(df)
    recent_birth(df)
    common_birth(df)
# How long did the calculation take
    print_pause_b(('This took %s seconds.' % (time.time() - start_time)))
    print_pause_b('-'*40)

# Improve usability by providing the option of creating further surveys
def restart_survey():
    print_pause_a('Do you want to create another survey?')
    restart = input('y/n\n')
    if restart == 'y':
        main()
# Ending the program if no futher surveys are needed
    elif restart == 'n':
        print_pause_a('Thank you for using this data analysis tool!')
        quit()
# 'Safety net' if no valid input is given to the function
    else:
        print_pause_a('Sorry I don\'t understand-please try again')
        restart_survey()

# main function that combines the predefined functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart_survey()

# checking if this is the main program
if __name__ == "__main__":
	main()
>>>>>>> d8810a24bad372c6e32c57ceceea743863ec428e
