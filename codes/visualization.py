# FUNCTION TO GENERATE HORIZONTAL BAR PLOTS
#
# Input Arguments
#   -   Values for Y-axis(two lists)
#   -   Name of groups
#   -   X-axis Labels
#   -   Y-axis Labels
#   -   X-axis Tick Labels
#   -   Name of the plot
# Output Arguments
#   -   Grouped Horizontal Bar plot
def plot_bar_grouped(y1_values, y2_values, group_plt, label_x, label_y, xticklabels_plt, filename_plt):
    ofst = 0.35  # offset
    xpos = np.arange(len(y1_values))  # x-positions

    fig, ax = plt.subplots()

    grp1 = ax.bar(xpos - ofst / 2, y1_values, ofst, label=group_plt[0])
    grp2 = ax.bar(xpos + ofst / 2, y2_values, ofst, label=group_plt[1])

    # x-axis operations
    plt.xticks(fontsize=7)  # controlling the foent size of x-tick labells
    ax.set_xticks(xpos)  # setting the position of x-tick labells
    ax.set_xticklabels(xticklabels_plt, rotation=20, ha='center')  # setting up x-tick labells
    ax.set_xlabel(label_x, fontsize=10)  # setting up x-axis labell

    # y-axis operations
    plt.yticks(fontsize=7)  # controlling the foent size of x-tick labells
    ax.set_ylabel(label_y, fontsize=10)  # setting up y-tick labells

    # Eliminating the spine
    ax.spines['right'].set_visible(False)  # eliminating right border
    ax.spines['top'].set_visible(False)  # eliminating top border

    # Setting up annotations
    lmt_l, lmt_u = ax.get_ylim()  # y-axis limits
    for i in range(0, len(xpos)):
        plt.text(x=xpos[i] - ofst / 1.5, y=y1_values[i] + (0.01 * lmt_u), s=y1_values[i], fontsize=7, rotation=90)
        plt.text(x=xpos[i] + ofst / 2.75, y=y2_values[i] + (0.01 * lmt_u), s=y2_values[i], fontsize=7, rotation=90)

    ax.legend(fontsize=7, ncol=2, loc='center', bbox_to_anchor=(0.5, 1.15), labelspacing=1)  # setting Legend

    # For plot zooming
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    
    plt.savefig(filename_plt, bbox_inches='tight')  # saving the plot
    plt.close(fig)


# FUNCTION TO PLOT LINE GRAPHS
#
# Input Arguments:
#   -   Values for x-axis
#   -   Values for y-axis
#   -   Labels for Lines
#   -   Labels for x-axis
#   -   Labels for y-axis
#   -   Plot for title
#
# Output Arguments:
#   -   Line Plot
def lineplotter(x_values, y_values, legend_plt, x_label, y_label, filename_plt):
    fig, ax = plt.subplots()

    l = len(x_values)

    # loop to plot all the lines
    for i in range(0, l):
        ax.plot(x_values[i], y_values[i], linewidth=0.9, label=legend_plt[i])

    # Dealing with dates
    date_format = mpl_dates.DateFormatter('%b, %d %y')
    plt.gcf().autofmt_xdate()

    # X-axis Operations
    plt.xticks(fontsize=7)
    ax.set_xlabel(x_label, fontsize=10)
    ax.xaxis.set_major_formatter(date_format)

    # Y-Axis Operations
    plt.yticks(fontsize=7)
    ax.set_ylabel(y_label, fontsize=10)

    # Eliminating the spine
    ax.spines['right'].set_visible(False)  # eliminating right border
    ax.spines['top'].set_visible(False)  # eliminating top border

    plt.legend(fontsize=7, ncol=5, loc='center', bbox_to_anchor=(0.5, 1.1))

    # maximising the graph
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.savefig(filename_plt, bbox_inches='tight')
    plt.close(fig)


# FUNCTION TO PLOT LINE GRAPHS (SUBPLOTS)
#
# Input Arguments:
#   -   Number of Rows
#   -   Number of Columns
#   -   Values for x-axis
#   -   Values for y-axis
#   -   Labels for Lines
#   -   Filename to save the Graph
#
# Output Arguments:
#   -   Line Plot
def lineplotter_subplot(r_plt, c_plt, x_values, y_values, legend_plt, filename_plt):
    fig, ax = plt.subplots(r_plt, c_plt, sharex=True, sharey=True)  # axis for subplots

    l = len(x_values)  # length of the concerned lists

    r = 0  # rows
    c = 0  # columns

    c_pallete = ['red', 'green', 'blue', 'cyan', 'orange']
    l_style = ['solid', 'dashed']

    for j in range(0, l):

        ax[r, c].plot(x_values[j], y_values[j], linestyle=l_style[c], marker='None', linewidth=0.9, color=c_pallete[r], label=legend_plt[j])
        ax[r, c].legend(fontsize=7)  # legend

        # Eliminating the spine
        ax[r, c].spines['right'].set_visible(False)  # eliminating right border
        ax[r, c].spines['top'].set_visible(False)  # eliminating top border

        plt.xscale('log')
        plt.yscale('log')

        # Axis distribution
        r += 1
        if r == r_plt:
            r = 0
            c += 1

    # Zooming the Plots
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    plt.subplots_adjust(left=0.03, right=0.97, top=0.98, bottom=0.08, hspace=0.16, wspace=0.1)  # adjusting spaces
    plt.savefig(filename_plt, bbox_inches='tight')  # saving plots
    plt.close(fig)


# FUNCTION TO PLOT LINE GRAPHS
#
# Input Arguments:
#   -   Values for x-axis
#   -   Values for y-axis
#   -   Labels for Lines
#   -   Labels for x-axis
#   -   Labels for y-axis
#   -   Plot for title
#
# Output Arguments:
#   -   Line Plot
def lineplotter_number(x_values, y_values, legend_plt, x_label, y_label, filename_plt):
    fig, ax = plt.subplots()

    l = len(x_values)

    # loop to plot all the lines
    for i in range(0, l):
        ax.plot(x_values[i], y_values[i], linewidth=0.9, label=legend_plt[i])

    # X-axis Operations
    plt.xticks(fontsize=7)
    ax.set_xlabel(x_label, fontsize=10)

    # Y-Axis Operations
    plt.yticks(fontsize=7)
    ax.set_ylabel(y_label, fontsize=10)

    # Eliminating the spine
    ax.spines['right'].set_visible(False)  # eliminating right border
    ax.spines['top'].set_visible(False)  # eliminating top border

    plt.legend(fontsize=7, ncol=2, loc='center', bbox_to_anchor=(0.5, 1.05))  # Legend

    # maximising the graph
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.savefig(filename_plt, bbox_inches='tight')
    plt.close(fig)


# FUNCTION TO PLOT LINE GRAPHS
#
# Input Arguments:
#   -   Values for x-axis
#   -   Values for y-axis
#   -   Labels for Lines
#   -   Labels for x-axis
#   -   Labels for y-axis
#   -   Plot for title
#
# Output Arguments:
#   -   Line Plot
def lineplotter_number_log(x_values, y_values, legend_plt, x_label, y_label, filename_plt):
    fig, ax = plt.subplots()

    l = len(x_values)

    plt.xscale('log')
    plt.yscale('log')

    # loop to plot all the lines
    for i in range(0, l):
        ax.plot(x_values[i], y_values[i], linewidth=0.9, label=legend_plt[i])

    # X-axis Operations
    plt.xticks(fontsize=7)
    ax.set_xlabel(x_label, fontsize=10)

    # Y-Axis Operations
    plt.yticks(fontsize=7)
    ax.set_ylabel(y_label, fontsize=10)

    # Eliminating the spine
    ax.spines['right'].set_visible(False)  # eliminating right border
    ax.spines['top'].set_visible(False)  # eliminating top border

    plt.legend(fontsize=7, ncol=3, loc='center', bbox_to_anchor=(0.5, 1.05))  # Legend

    # maximising the graph
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.savefig(filename_plt, bbox_inches='tight')
    plt.close(fig)


# FUNCTION TO PLOT LINE GRAPHS (SUBPLOTS)
#
# Input Arguments:
#   -   Number of Rows
#   -   Number of Columns
#   -   Values for x-axis
#   -   Values for y-axis
#   -   Labels for Lines
#   -   Filename to save the Graph
#
# Output Arguments:
#   -   Line Plot (subplots with each plot represeneting multiple values
def lineplotter_subplot_multivalues(r_plt, c_plt, x_values_1, x_values_2, y_values_1, y_values_2, legend_plt,
                                    filename_plt):
    fig, ax = plt.subplots(r_plt, c_plt, sharex=True, sharey=True)  # axis for subplots

    l = len(x_values_1)  # length of the concerned lists

    r = 0  # rows
    c = 0  # columns

    c_pallete = ['red', 'green', 'blue', 'cyan', 'orange']
    l_style = ['solid', 'dashed']

    for j in range(0, l):

        ymax1 = max(y_values_1[j])
        ymax2 = max(y_values_1[j])
        ymax = max([ymax1, ymax2])

        ax[r, c].set_ylim(0, 1.05 * ymax)

        ax[r, c].plot_date(x_values_1[j], y_values_1[j], linestyle=l_style[c], marker='None', linewidth=0.9, color=c_pallete[r], label=legend_plt[j] + ' Absolute')
        ax[r, c].plot_date(x_values_2[j], y_values_2[j], linestyle='dotted', marker='None', linewidth=0.9, color=c_pallete[r], label=legend_plt[j] + ' Moving Average')

        ax[r, c].legend(fontsize=6, ncol=2, loc='center', bbox_to_anchor=(0.5, 1.15), labelspacing=1)  # legend

        # Dealing with Dates
        date_format = mpl_dates.DateFormatter('%b, %d %y')
        plt.gcf().autofmt_xdate()
        ax[r, c].xaxis.set_major_formatter(date_format)

        # Eliminating the spine
        ax[r, c].spines['right'].set_visible(False)  # eliminating right border
        ax[r, c].spines['top'].set_visible(False)  # eliminating top border

        # Axis distribution
        r += 1
        if r == r_plt:
            r = 0
            c += 1

    # Zooming the Plots
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    plt.subplots_adjust(left=0.04, right=0.98, top=0.99, bottom=0.1, hspace=0.4, wspace=0.04)  # adjusting spaces
    plt.savefig(filename_plt, bbox_inches='tight')  # saving plots
    plt.close(fig)


# FUNCTION TO PLOT LINE GRAPHS (SUBPLOTS)
#
# Input Arguments:
#   -   Number of Rows
#   -   Number of Columns
#   -   Values for x-axis
#   -   Values for y-axis
#   -   Labels for Lines
#   -   Filename to save the Graph
#
# Output Arguments:
#   -   Line Plot
def lineplotter_subplot_multivalues_limit1(r_plt, c_plt, x_values_1, x_values_2, y_values_1, y_values_2, legend_plt,
                                           filename_plt):
    fig, ax = plt.subplots(r_plt, c_plt, sharex=True, sharey=True)  # axis for subplots

    l = len(x_values_1)  # length of the concerned lists

    r = 0  # rows
    c = 0  # columns

    c_pallete = ['red', 'green', 'blue', 'cyan', 'orange']
    l_style = ['solid', 'dashed']

    for j in range(0, l):

        ax[r, c].set_ylim(0, 2)  # setting limits of y-axis

        ax[r, c].plot_date(x_values_1[j], y_values_1[j], linestyle=l_style[c], marker='None', linewidth=0.9, color=c_pallete[r], label=legend_plt[j] + ' Absolute')
        ax[r, c].plot_date(x_values_2[j], y_values_2[j], linestyle='dotted', marker='None', linewidth=0.9, color=c_pallete[r], label=legend_plt[j] + ' Moving Average')
        ax[r, c].axhline(1, color='k', linewidth=0.3, linestyle='dashed')

        ax[r, c].legend(fontsize=7, ncol=2, loc='center', bbox_to_anchor=(0.5, 1.15), labelspacing=1)  # legend

        # Dealing with Dates
        date_format = mpl_dates.DateFormatter('%b, %d %y')
        plt.gcf().autofmt_xdate()
        ax[r, c].xaxis.set_major_formatter(date_format)

        # Eliminating the spine
        ax[r, c].spines['right'].set_visible(False)  # eliminating right border
        ax[r, c].spines['top'].set_visible(False)  # eliminating top border

        # Axis distribution
        r += 1
        if r == r_plt:
            r = 0
            c += 1

    # Zooming the Plots
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    plt.subplots_adjust(left=0.04, right=0.98, top=0.99, bottom=0.1, hspace=0.4, wspace=0.04)  # adjusting spaces
    plt.savefig(filename_plt, bbox_inches='tight')  # saving plots
    plt.close(fig)


# FUNCTION TO STRIP OFF ZEROS
#
# Input Arguments
#   -   Database from which 0 needs to be stripped before first non-zero values
#   -   List of countries for which above mentioned operation needs to be performed
# Output Arguments
#   -   List of Numbers after stripping the zeros (list of lists)
#   -   List of Dates(the dates for which zeros are removed are droped) (list of lists)
def zerostrip(df, filtervalues):
    dates = df.drop(['Country'], axis=1).columns.values.tolist()  # extracting dates
    df = df[df.Country.isin(filtervalues)]  # filtering required values of the worst hit countries

    x_values = []  # List to hold final values after stripping
    y_values = []  # List to hold final dates after stripping zeros

    for i in filtervalues:
        df_temp = df[df['Country'] == i].values.tolist()
        for k in df_temp:
            l = len(k)
            firstzero = True
            lst1 = []
            lst2 = []
            for p in range(1, l):
                if (firstzero == False) or (k[p] > 0):
                    lst1.append(round(k[p], 3))
                    lst2.append(dates[p - 1])
                    firstzero = False
            x_values.append(lst2)
            y_values.append(lst1)
            
    return x_values, y_values


# FUNCTION TO STRIP OFF ZEROS
#
# Input Arguments
#   -   Database from which negitive values needs to stripped from the begining and from the end
#   -   List of countries for which above mentioned operation needs to be performed
# Output Arguments
#   -   List of Numbers after stripping the zeros (list of lists)
#   -   List of Dates(the dates for which zeros are removed are droped) (list of lists)
def negstrip(df, filtervalues):
    dates = df.drop(['Country'], axis=1).columns.values.tolist()  # extracting dates
    df = df[df.Country.isin(filtervalues)]  # filtering required values of the worst hit countries

    x_values = []  # List to hold final values after stripping
    y_values = []  # List to hold final dates after stripping zeros
    str_index = []  # starting point of the list
    end_index = []  # ending point of list

    for i in filtervalues:
        df_temp = df[df['Country'] == i].values.tolist()
        for k in df_temp:
            l = len(k)
            firstpositive = False
            for p in range(1, l - 1):
                if (k[p] > 0) & (firstpositive == False):
                    str_index.append(p)
                    s = p
                    firstpositive = True
                if (k[p] > 0) & (k[p + 1] < 0):
                    end_index.append(p)
                    e = p
            x_values.append(dates[s - 1:e - 1])
            y_values.append(k[s:e])
    return x_values, y_values


# FUNCTION TO CONVERT DATES(STRING VALUES FROM DATABASE) TO DATES(DATES TYPE)
#
# Input Arguments:
#   -   List of Lists with dates as strings
# Output Arguments:
#   -   List of Lists with dates as date/time
def datesorter(listoflist_dates):
    # Correcting for year
    length_listoflist_dates = len(listoflist_dates)
    for i in range(0, length_listoflist_dates):  # loop to enter list inside list
        list_dates = listoflist_dates[i]
        length_list_dates = len(list_dates)
        for j in range(0, length_list_dates):  # loop to enter individual element inside the list
            element_date = str(list_dates[j])
            if ('/' in element_date):
                temp_date = element_date.split('/')
            if ('-' in element_date):
                temp_date = element_date.split('-')

            length_temp_date = len(temp_date)
            v = ''
            for k in range(0, length_temp_date):
                if k == length_temp_date - 1:
                    temp_date[k] = '20' + temp_date[k]
                else:
                    temp_date[k] = temp_date[k] + '/'
                v = v + temp_date[k]
            element_date = v
            list_dates[j] = element_date

    # # Converting to dates from string
    length_listoflist_dates = len(listoflist_dates)
    for i in range(0, length_listoflist_dates):  # loop to enter list inside list
        list_dates = listoflist_dates[i]
        length_list_dates = len(list_dates)
        for j in range(0, length_list_dates):  # loop to enter individual element inside the list
            element_date = list_dates[j]
            dt = datetime.strptime(element_date, '%m/%d/%Y')
            list_dates[j] = dt

    return listoflist_dates


# FUNCTION TO RECIVE TWO STRINGS OF UNEQUAL LENGTH AND SLICE THEM TO EQUAL LENGTH
#
# Input Parameters
#   -   Two lists of unequal length
# Output Parameters
#   -   Two lists of equal length
def listequalizer(x_values, y_values):
    length_x_values = len(x_values)

    x_values_final = []
    y_values_final = []

    for i in range(0, length_x_values):
        x = x_values[i]
        y = y_values[i]
        if (len(x) == len(y)):
            x_values_final.append(x)
            y_values_final.append(y)
        else:
            if (len(x) > len(y)):
                index_adjustment = len(x) - len(y)
                x_values_final.append(x[index_adjustment:len(x)])
                y_values_final.append(y)
            if (len(y) > len(x)):
                index_adjustment = len(x) - len(y)
                x_values_final.append(x)
                y_values_final.append(y[index_adjustment:len(y)])
    return x_values_final, y_values_final


# MAIN BODY OF THE PROGRAM
# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np
from datetime import datetime

####_______________________________________________________ Reading the Database______________________________________________________###

df_coronaC = pd.read_csv('confirmedcases.csv')  # Confirmed Cases of Coronavirus
df_coronaD = pd.read_csv('deaths.csv')  # Deaths due to Cornavirus
df_coronaR = pd.read_csv('recovered.csv')  # Recovered from Coronavirus
df_deaths_average = pd.read_csv('deaths_average.csv')  # Average Deaths due to coronavirus
df_recovered_average = pd.read_csv('recovered_average.csv')  # Average Recovered from Coronavirus
df_recoveryratio = pd.read_csv('recoveryratio.csv')  # Recovery Ratio
df_recoveryratio_movingaverage = pd.read_csv('recoveryratio_movingaverage.csv')  # Moving Average of Recovery Ratio
df_mortalityfactor = pd.read_csv('mortalityfactor.csv')  # Mortality Factor
df_mortalityfactor_movingaverage = pd.read_csv(
    'mortalityfactor_movingaverage.csv')  # Moving Average of Mortality Factor
df_newcases = pd.read_csv('newcases.csv')  # New Cases of coronavirus
df_growthrate = pd.read_csv('growthrate.csv')  # Growth Rate
df_growthrate_movingaverage = pd.read_csv('growthrate_movingaverage.csv')  # Mooving Average of Growth Rate

# For simulated outbreak
df_simulted = pd.read_csv('simulation_values.csv')  # values for simulated outbreak

# _______________________________________________________________________________________________________________________________________#


###_________________________________________________Creating New Database_and lists__________________________________________________________###

# Extracting Countries Worst Affected by Coronavirus (in terms of confirmed cases)
countries = df_coronaC['Country'].values.tolist()  # list of countries from original data
dates = df_coronaC.columns.values.tolist()  # indexes from original data
lastday = dates[len(dates) - 1]  # selecting last day entry
lastdaycases = df_coronaC[lastday].values.tolist()  # list of cases on last day
data = {'Country': countries, lastday: lastdaycases}  # creating dictionary to create DataFrame
df_coronaC_lastday = pd.DataFrame(data)  # DataFrame with number of confirmed cases
df_coronaC_worstaffected = df_coronaC_lastday.sort_values(lastday, ascending=False).head(
    10)  # Dataframe of 10 worst affected countries
countries_P1 = df_coronaC_worstaffected['Country'].values.tolist()  # list of countries from the the previous DataFrame

countries_P1.sort()

# For Plot 1 - [GROUPED BAR GRAPH]
df_temp = df_coronaD[df_coronaD.Country.isin(countries_P1)]  # filtering required values of the worst hit countries (Deaths)
df_coronaD_worstaffected = df_temp[lastday]  # Dataframe of 10 worst affected countries
y1_values_P1 = df_coronaD_worstaffected.values.tolist()  # Creating list of last day values
df_temp = df_coronaR[df_coronaR.Country.isin(countries_P1)]  # filtering required values of the worst hit countries(Recovered)
df_coronaR_worstaffected = df_temp[lastday]  # Dataframe of 10 worst affected countries
y2_values_P1 = df_coronaR_worstaffected.values.tolist()  # Creating list of last day values

# For Plot-2 [GROUPED BAR GRAPH]
df_temp = df_deaths_average[df_deaths_average.Country.isin(countries_P1)]  # filtering required values of the worst hit countries (Deaths)
y1_values_P2 = df_temp['avrg'].values.tolist()  # Creating list of average values
df_temp = df_recovered_average[df_recovered_average.Country.isin(countries_P1)]  # filtering required values of the worst hit countries (Recovered)
y2_values_P2 = df_temp['avrg'].values.tolist()  # Creating list of average values

# For Plot -3 [LINE GRAPH] - Deaths due to Coronavirus
x_values_P3_temp, y_values_P3 = zerostrip(df_coronaD, countries_P1)
x_values_P3 = datesorter(x_values_P3_temp)

# For Plot 4 - [LINE GRAPH] - Number of deaths
x_values_P4_temp, y_values_P4 = zerostrip(df_coronaR, countries_P1)
x_values_P4 = datesorter(x_values_P4_temp)

# For Plot 5, 6 - [LINE GRAPH - SUBPLOT OF MULTIPLE VALUES] - Recovery Ratio-Comparitive, Recovery Ratio-Moving Average
x_values_P5_1_temp, y_values_P5_1 = zerostrip(df_recoveryratio, countries_P1)
x_values_P5_1 = datesorter(x_values_P5_1_temp)
x_values_P5_2_temp, y_values_P5_2 = negstrip(df_recoveryratio_movingaverage, countries_P1)
x_values_P5_2 = datesorter(x_values_P5_2_temp)

# For Plot 7,8 - [LINE GRAPH - SUBPLOT OF MULTIPLE VALUES] - Mortality Factor
x_values_P6_1_temp, y_values_P6_1 = zerostrip(df_mortalityfactor, countries_P1)
x_values_P6_1 = datesorter(x_values_P6_1_temp)
x_values_P6_2_temp, y_values_P6_2 = negstrip(df_mortalityfactor_movingaverage, countries_P1)
x_values_P6_2 = datesorter(x_values_P6_2_temp)

# For Plot 9 - [LINE GRAPH](log log curve) - New Cases vs Confirmed Cases on log log axis
placeholder_values, y_values_P9_temp = zerostrip(df_newcases, countries_P1)  # creating y-values for Plot 8
placeholder_values, x_values_P9_temp = zerostrip(df_coronaC, countries_P1)  # creating x-values for Plot 8
x_values_P9, y_values_P9 = listequalizer(x_values_P9_temp, y_values_P9_temp)  # Equalizing the Values

# For Plot 10 - [LINE GRAPH - SUBPLOT OF MULTIPLE VALUES] - Growth Rate
x_values_P10_1_temp, y_values_P10_1 = zerostrip(df_growthrate, countries_P1)
x_values_P10_1 = datesorter(x_values_P10_1_temp)
x_values_P10_2_temp, y_values_P10_2 = negstrip(df_growthrate_movingaverage, countries_P1)
x_values_P10_2 = datesorter(x_values_P10_2_temp)

##################################################### For Simulated Outbreak ###########################################################

# For Plot 11 - [LINE GRAPH] - Case Distribution over time
y1_sustained = df_simulted['sustained_confirmed'].values.tolist()
y2_sustained = df_simulted['sustained_new'].values.tolist()
days = df_simulted['days'].values.tolist()
y_values_sustained = [y1_sustained, y2_sustained]
x_values_sustained = [days, days]

# For Plot 12 - [LINE GRAPH] - Case Distribution for Confirmed Cases
y1_confirmed = df_simulted['linear_confirmed'].values.tolist()
y2_confirmed = df_simulted['sudden_confirmed'].values.tolist()
y_values_confirmed = [y1_confirmed, y2_confirmed]
x_values_confirmed = [days, days]
plt_cases = ['Linear Decay', 'Sudden Change']

# For Plot 13 - [LINE GRAPH] - Case Distribution for New Cases
y1_new = df_simulted['linear_new'].values.tolist()
y2_new = df_simulted['sudden_new'].values.tolist()
y_new = [y1_new, y2_new]
x_new = [days, days]
plt_new = ['Linear Decay', 'Sudden Change']

# For Plot 14 - [LINE GRAPH](logarithmic Axis) - Confirmed Cases vs New Cases
x_values_simulated = [y1_sustained, y1_confirmed, y2_confirmed]
y_values_simulated = [y2_sustained, y1_new, y2_new]
plt_simulated = ['Sustained', 'Linearly Decaying', 'Sudden Chnage']

###______________________________________________________________________________________Plotting the dataset____________________________________________________________________________________________________###

# Plot - 1 - [STACKED BAR GRAPH] - Deaths and Recovered
plot_bar_grouped(y1_values_P1, y2_values_P1, ['Deaths', 'Recovered'], 'Dates', 'Deaths/Recovered', countries_P1, 'plot_1.pdf')

# Plot - 2 - [STACKED BAR GRAPH] - Average deaths and recovories
plot_bar_grouped(y1_values_P2, y2_values_P2, ['Average Deaths', 'Average Recovered'], 'Dates', 'Average Deaths/Average Recoveries', countries_P1, 'plot_2.pdf')

# Plot - 3 - [LINE GRPAH] - Deaths due to Coronavirus
lineplotter(x_values_P3, y_values_P3, countries_P1, 'Dates', 'Deaths', 'plot_3.pdf')

# Plot 4 - [LINE GRAPH] - Recovered from coronavirus
lineplotter(x_values_P4, y_values_P4, countries_P1, 'Dates', 'Recovered', 'plot_4.pdf')

# For Plot 5 - [LINE GRAPH - SUBPLOT OF MULTIPLE VALUES] - Recovery Ratio-Comaprative
lineplotter_subplot_multivalues(5, 2, x_values_P5_1, x_values_P5_2, y_values_P5_1, y_values_P5_2, countries_P1, 'plot_5.pdf')

# For Plot 6 -[LINE GRAPH] - Recovery Ratio - Moving Average
lineplotter(x_values_P5_1, y_values_P5_1, countries_P1, 'Dates', 'Recovery Ratio', 'plot_6.pdf')

# For Plot 7 - [LINE GRAPH - SUBPLOT OF MULTIPLE VALUES] - Mortality Factor-Comparative
lineplotter_subplot_multivalues(5, 2, x_values_P6_1, x_values_P6_2, y_values_P6_1, y_values_P6_2, countries_P1, 'plot_7.pdf')

# For Plot 8 - [LINE GRAPH] - Mortality Factor - Moving Average
lineplotter(x_values_P6_1, y_values_P6_1, countries_P1, 'Dates', 'Mortality Factor', 'plot_8.pdf')

# For Plot 9 - [LINE GRAPH - SUBPLOT](log log curve) - New Cases vs Confirmed Cases on log log axis
lineplotter_subplot(5, 2, x_values_P9, y_values_P9, countries_P1, 'plot_9.pdf')

# For Plot 10- [LINE GRAPH - SUBPLOT](log log curve) - New Cases vs Confirmed Cases on log log axis
lineplotter_subplot_multivalues_limit1(5, 2, x_values_P10_1, x_values_P10_2, y_values_P10_1, y_values_P10_2, countries_P1, 'plot_10.pdf')

##################################################### For Simulated Outbreak ###########################################################

# For plot 11 - [LINE GRAPH] - New Cases vs Days
lineplotter_number(x_values_sustained, y_values_sustained, ['Confirmed Cases', 'New Cases'], 'Days', 'Confirmed Cases', 'plot_11.pdf')

# For Plot 12 - [LINE GRAPH] - Case Distribution for Various Growth Patterns
lineplotter_number(x_values_confirmed, y_values_confirmed, plt_cases, 'Days', 'Confirmed Cases', 'plot_12.pdf')

# For Plot 13 - [LINE GRAPH] - Confirmed Cases vs New Cases
lineplotter_number_log(x_values_simulated, y_values_simulated, plt_simulated, 'Confirmed Cases', 'New Cases', 'plot_13.pdf')