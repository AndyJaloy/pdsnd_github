import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("\n Welcome! Let's see some of the bikeshare data")



    while True:
      city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n").lower().title()
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower().title()
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nAre you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n").lower().title()
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Sorry, I didn't catch that. Try again.")
        continue
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month =='None':
        pop_month= df['month'].mode()[0]
        months= ['January','February','March','April','May','June']
        pop_month= months[pop_month-1]
        print("The most Popular month is",pop_month)


    # display the most common day of week
    if day =='None':
        pop_day= df['day_of_week'].mode()[0]
        print("The most Popular day is",pop_day)


    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    pop_hour=df['Start Hour'].mode()[0]
    print("The popular Start Hour is {}:00 hrs".format(pop_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start_station= df['Start Station'].mode()[0]
    print("The most commonly used Start Station is {}".format(pop_start_station))


    # display most commonly used end station
    pop_end_station= df['End Station'].mode()[0]
    print("The most commonly used End Station is {}".format(pop_end_station))

    # display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    pop_com= df['combination'].mode()[0]
    print("The most frequent combination of Start and End Station is {} ".format(pop_com))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration=df['Trip Duration'].sum()
    minute,second=divmod(total_duration,60)
    hour,minute=divmod(minute,60)
    print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(hour,minute,second))

    # display mean travel time
    average_duration=round(df['Trip Duration'].mean())
    m,sec=divmod(average_duration,60)
    if m>60:
        h,m=divmod(m,60)
        print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(h,m,sec))
    else:
        print("The total trip duration: {} minute(s) {} second(s)".format(m,sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts= df['User Type'].value_counts()
    print("The user types are:\n",user_counts)


    # Display counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        gender_counts= df['Gender'].value_counts()
        print("\nThe counts of each gender are:\n",gender_counts)

    # Display earliest, most recent, and most common year of birth
        earliest= int(df['Birth Year'].min())
        print("\nThe oldest user is born of the year",earliest)
        most_recent= int(df['Birth Year'].max())
        print("The youngest user is born of the year",most_recent)
        common= int(df['Birth Year'].mode()[0])
        print("Most users are born of the year",common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    a = 1
    while True:
        more_data = input('\nWould you like to see some more data? Enter yes or no.\n')
        if more_data.lower() == 'yes':
            print(df[a:a+5])
            a = a+5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
