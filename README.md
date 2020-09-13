# Explore US Bikeshare Data
Using Python to explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a determined price. Thanks to the rise in data science we can obtain a great deal of data from each users’ trip, meaning we can explore how these bike-sharing systems are used and how we can improve upon them.
###### 13/09/2020


### Description
Wrote Python code that imports each cities data with CSV files. The script takes raw input from the user to create an interactive experience in the terminal to compute and present descriptive statistics.

### Datasets
All data was provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. The data shown corresponds to the first six months of 2017 for all three cities.

All three cities contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

### Statistics Computed
* Popular times of travel
  * Most common month
  * Most common day of week
  * Most common hour of day

* Popular stations and trip
  * Most common start station
  * Most common end station
  * Most common trip from start to end

* Trip duration
  * Total travel time
  * Average travel time

* User info
  * Counts of each user type
  * Counts of each gender (only available for NYC and Chicago)
  * Earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Software Requirements
To complete this project, the following software requirements apply:

* You should have Python 3, NumPy, and pandas installed using Anaconda
* A text editor, like Sublime or Atom.
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).
