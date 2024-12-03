import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
# Import numpy and matplotlib to be used in creating the different graphs.
# We import Line2D from matplotlib for plot 1 to properly create a the legend in the graph.


opened = open('WeatherDataCLL.csv', 'r')
read = opened.read().split('\n')
read = read[1:]
# Open and read the Weather Data file and remove the first line which doesn't include actual data.

############## Plot 1 ##################

def plot1(): # Create a function for Plot 1.
    dailytemp = []
    dailywind = []
    date = [] 
    # Create lists that will be appended to to then be used to plot the lines on the graph.

    iter = 0  
    # Counter for iteration for the x axis as adding the dates on their own causes a weird visual glitch.
    for t in read:
        if t == '':
            continue
        t2 = t.split(',')
        # Split the list to then look through it at specific locations (t2[2] and t2[4]) to calculate the temperature and wind speed.
        try:
            iter += 1
            date.append(iter)
            # Our dates will be linked to the iteration at each iteration.
            dailytemp.append(float(t2[2]))
            dailywind.append(float(t2[4]))
        except (ValueError, IndexError):
            continue
        # We use a try-except statement in order to look through at each iteration of the read file and skip any values that would cause an error such as blank spaces ''.

    min_length = min(len(date), len(dailytemp), len(dailywind))
    date = date[:min_length]
    dailytemp = dailytemp[:min_length]
    dailywind = dailywind[:min_length]
    # Assign each data that is going to be used with the same length to avoid an error from occuring stating that the shapes are different.

    fig, ax1 = plt.subplots()
    # We start creating the graph.

    ax1.plot(date, dailytemp, color="red", linewidth=1.5)
    # Plot and format the data that matches the way done in the instructions.
    ax1.set_xlabel("Date")
    # Assign Date as the X axis label.
    ax1.set_ylabel("Average Temperature (°F)")
    # Create the first plot for the average temperature.

    ax2 = ax1.twinx()
    # Create a second plot using twinx()
    ax2.plot(date, dailywind, color="blue", linewidth=1.5)
    # Format the second data for the plot.
    ax2.set_ylabel("Average Wind Speed (mph)")
    # Assign the proper y axis label.

    redleg = Line2D([0], [0], color="red", linewidth=1.5, label="Avg Temp")
    blueleg = Line2D([0], [0], color="blue", linewidth=1.5, label="Avg Wind")
    ax2.legend(handles=[redleg, blueleg], loc="lower left")
    # Create a legend based on the data we have and position it on the lower left of the graph.

    plt.title('Average Temperature and Average Wind Speed')
    # Finally set the title to be the same as the one from the instruction pdf.
    plt.show()
    # Show the fully formatted plot for the line graph for average temperature and average wind speed.

##########################################

############## Plot 2 ####################

def plot2(): # Create a function for plot 2.
    dailywind = []
    # Create list that will be appended to for the data of the histogram.

    for t in read:
        t2 = t.split(',')
        try:
            wind_speed = float(t2[4])
            dailywind.append(wind_speed)
        except ValueError:
            continue
    # Iterate through the read file and append to the empty list the Average Wind Speed.

    plt.hist(dailywind, bins=30, range=(0, 20), color='green', edgecolor='black')
    # This line will plot the histogram with 30 bins (which I determined by counting the bins in the shown output of the instructions) and format the rest of the histogram.

    plt.xlabel("Average Wind Speed, mph")
    plt.ylabel("Number of Days")
    plt.title("Histogram of Average Wind Speed")
    # Create and name the appropriate labels and title for the histogram.

    plt.show()
    # Show the fully formatted plot 2 of the histogram.

###########################################

############### Plot 3 ####################

def plot3(): # Create a function for plot 3.
    humidity = []
    dew_point = []
    # Create two empty lists to be appended to for humidity and dew point.

    for t in read:
        t2 = t.split(',')
    # Split the list at t to append the humidity and dew point to the empty lists.
        try:
            humidity_value = float(t2[3])
            dew_point_value = float(t2[1])
            humidity.append(humidity_value)
            dew_point.append(dew_point_value)
        except ValueError:
            continue
        # Again we use the try-except statement to append only valid values (which in this case is numbers and avoid any blank spaces '').

    x = np.array(dew_point)
    y = np.array(humidity)
    # We create two arrays for x and y using the lists created for dew point and humidity.

    plt.scatter(x, y, s=10, color='black')
    # With x and y we plot the points into the scatter plot and format them accordingly (similar to how its seen in the instructions)

    plt.xlabel("Average Dew Point (F)")
    plt.ylabel("Average Relative Humidity (%)")
    plt.title("Average Relative Humidity vs Average Dew Point")
    # We then format and label the title and x and y labels for the histogram according to how its seen in the instructions.

    padding_factor = 0.05 # Wanted to add some padding to make the graph match more with the original one given in the instructions. 5% padding on the margins.
    plt.xlim(min(x) - (max(x) - min(x)) * padding_factor, max(x) + (max(x) - min(x)) * padding_factor)
    plt.ylim(min(y) - (max(y) - min(y)) * padding_factor, max(y) + (max(y) - min(y)) * padding_factor)
    # These two lines will create the limits of the x and y axis with the added padding on the margins by identifying the lowest number and highest number for each axis.

    plt.show()
    # Show the fully formatted plot 3 of the scatterplot.

############################################

################## Plot 4 ##################

def plot4(): # Create a function for plot 4.
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    mean_temp = []
    high_temp = []
    low_temp = []
    precip = []
    # Create a list for the months in the weather data file as well as proper empty lists for each data point that we're looking for in the bar graph.

    monthly_data = {month: {'high': [], 'low': [], 'precip': []} for month in months}
    # We create a dictionary to facilitate iteration through the file.

    for t in read:
        t2 = t.split(',')
        t3 = t2[0].split('-')
        month = t3[1]
        try:
            high_temp_val = int(t2[5])
            low_temp_val = int(t2[6])
            precip_val = float(t2[7])
        except ValueError:
            continue
        if month in months:
            monthly_data[month]['high'].append(high_temp_val)
            monthly_data[month]['low'].append(low_temp_val)
            monthly_data[month]['precip'].append(precip_val)
    # We iterate through the file and only append valid values for the points needed (in other words no blank spaces ''.).

    for month in months:
        if monthly_data[month]['high']:
            high_temp.append(max(monthly_data[month]['high']))
            low_temp.append(min(monthly_data[month]['low']))

            total_precip = sum(monthly_data[month]['precip'])
            mean_precip = total_precip / 10 
            precip.append(mean_precip)
            # We calculate the total precipitation for each month and divide by 10 years as suggested by the announcement Professor Mckenzie made.

            mean_temp.append(sum(monthly_data[month]['high']) / len(monthly_data[month]['high']))
        # We calculate the averages and values needed for the graph to then begin creating our bar graph and three lines.

    fig, ax1 = plt.subplots()
    # We begin creating the plot.
    ax1.bar(months, mean_temp, color='yellow')
    # We format the bar graph accordingly
    ax1.plot(months, high_temp, color='red', label="High T")
    ax1.plot(months, low_temp, color='blue', label="Low T")
    ax1.plot(months, precip, color='skyblue', label="Precip")
    # We plot the three lines for high temperature, low temperature, and precipitation.

    ax1.legend(loc="upper left")
    # We create a legend with the labels given to each plot.

    ax1.set_xlabel("Month")
    ax1.set_ylabel("Average Temperature, F\nMonthly Precipitation, in")
    plt.title("Temperature and Precipitation by Month")
    # We title the bar graph and label the x and y axis accordingly.

    plt.show()
    # Show the fully formatted plot 4 of the bar graph.

###################################################

plot1()
plot2()
plot3()
plot4()
# Recall all the defined functions to show all 4 created plots.

opened.close()
# Close the opened weather data file so that it may be closed properly.