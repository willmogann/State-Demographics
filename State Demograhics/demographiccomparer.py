import state_demographics
import school_scores
import state_crime
import matplotlib.pyplot as plt

state_income = state_demographics.get('Income.Median Houseold Income','(None)','')
state_names = state_demographics.get('State','(None)','')
math_scores = school_scores.get('Total.Math','Year','2015')
crime_rate = state_crime.get('Data.Rates.Violent.All','Year','2015')
nc_math_scores = school_scores.get('Total.Math','State.Name','North Carolina')
nc_crime_rate = state_crime.get('Data.Rates.Violent.All','State','North Carolina')

#This code takes the income of the states and sorts the data alphabetically by the state name using parallel lists
zipped_lists = zip(state_names, state_income)
sorted_zipped_lists = sorted(zipped_lists)
sorted_state_income = []
for i in sorted_zipped_lists:
    sorted_state_income.append(i[1])

print('Please type "Math Scores" or "Crime Rates"')
#This variable stores what dataset the user wants to use
user_dataset = input('What dataset do you want to use?')

#This function defines the scatterplot, so code is not repeated
def scatterplot(input_x, input_y, name_x, name_y):
    plt.scatter(input_x, input_y)
    plt.title((name_x + ' vs. ') + name_y)
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.show()
    print(name_x, ': ', input_x)
    print(name_y, ': ', input_y)

#Line plot function
def line_plot(input_x, name_x, name_y):
    plt.plot(input_x)
    plt.title((name_x + ' vs. ') + name_y)
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.show()

#This calculates the mean of one dataset
def mean(variable):
    return (sum(variable) / len(variable))

#This scatterplot is used if the user desires to look at school scores vs income
if user_dataset == 'Math Scores':
    (scatterplot(sorted_state_income, math_scores, 'Median Income', 'Math Scores'))
    print('There is no solution to this problem, because there is not an apparent relationship between median income and math scores.')
    print('Here is a line plot of the math scores of all 50 states, followed by the mean.')
    line_plot(nc_math_scores, 'Years past 2005', 'Math Scores in NC')
    print('Average math score over time in NC:', mean(nc_math_scores))

#This scatterplot is used if the user wants to compare state crime and income
if user_dataset == 'Crime Rates':
    (scatterplot(sorted_state_income, crime_rate, 'Median Income', 'Violent Crime Rate'))
    print('There is a slight downward relationship, meaning higher income leads to slightly lower crime, in general.')
    print('Possible solutions are: increasing spending in lower income areas to reduce crime rates.')
    line_plot(nc_crime_rate, 'Years past 1960', 'Crime rate in NC')
    print('Average crime rate over time in NC:', mean(nc_crime_rate))
