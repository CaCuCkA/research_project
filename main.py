from parse_file import parse_file
from plots.crimes.crimes import plot_crimes
from plots.arrests.arrests import plot_arrests
from plots.crimes.crimes_by_time_2 import plot_crimes_by_time_2
from plots.arrests.arrest_frequency import plot_arrests_frequency
from plots.theft_battery_compare import theft_battery_arrest_comparison
from plots.arrests.arrest_probability import plot_probability_of_arrest_by_crime_type
from plots.amount_of_theft_by_time import plot_amount_of_theft_by_time
from plots.crimes.crimes_by_time import plot_crimes_by_time
from plots.crimes.crimes_by_season import plot_crimes_by_season
from plots.arrests.arrest_by_month import plot_arrests_by_month
from plots.burglary_by_month import plot_burglary_by_month
from map import map_crimes




def main():
    df = parse_file()
    plot_crimes(df)
    plot_arrests(df)
    plot_crimes_by_time_2(df)
    plot_arrests_frequency(df)
    theft_battery_arrest_comparison(df)
    plot_probability_of_arrest_by_crime_type(df)
    plot_amount_of_theft_by_time(df)
    plot_crimes_by_time(df)
    plot_crimes_by_season(df)
    plot_arrests_by_month(df)
    plot_burglary_by_month(df)
    map_crimes(df)


if __name__ == '__main__':
    main()