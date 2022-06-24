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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Please Choose a city: "Chicago, Washington or New York City": ').lower()
       if city not in CITY_DATA:
            city
       else:
        break
                
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please choose a month or select all to filter by from January to June: ').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        if month != 'all' and month not in months:
            month
        
        else:
            break
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please choose a day from the week or all: ').lower()
        days = ['monday', 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday']
        
        if day != 'all' and day not in days:
            day
            
        else:
            break


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) #To convert start time into datetime
    
    df['month'] = df['Start Time'].dt.month # to access months
    df['day_of_week'] = df['Start Time'].dt.day #to access days
    
    #To filter by months
    if month != 'all' :
        months = [ 'january', 'february', 'march', 'april', 'may', 'june']
        
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
    
    #To filter by days 
    if day != 'all' :
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        
        day = days_of_week.index(day) + 1
        
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('most common month:', most_common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('most common day of week:', most_common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    
    print('most common hour:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('most commonly used end station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_start_end = ('From ' + df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('most frequent combination of start and end station trip:', most_frequent_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time:', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_time)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Counts of user types:', user_type_count)

    # TO DO: Display counts of gender
    
    if 'Gender' in df:
        print('Counts of gender', df['Gender'].value_counts())
    else:
        print('Count of gender: Sorry, There is not data available ')


    # TO DO: Display earliest, most recent, and most common year of birth
      
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        print('Earliest year of Birth:', earliest_year)
        
        most_recent_year = int(df['Birth Year'].max())
        print('Most recent year of birth:', most_recent_year)
        
        most_common_year = int(df['Birth Year'].mean())
        print('Most common year of Birth:', most_common_year)

    else:
        print('Sorry, there is not data available for earliest, most recent and most common year of birth')
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def question(df):
    """Asks user whether they want to see the nnext 5 rows of data or not."""
    
    view_data = input('Do you want to see the next 5 rows of data? Please enter yes or no.\n')
    start_loc = 0
    
    while True:
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        print('-'*40)
            
        if view_display != 'yes':
            break
    
    print('-'*40)
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        question(df)
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
