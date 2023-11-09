#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:00:27 2023

@author: Muhammad Kazim 
"""

# Importing the important libraries 
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset using pandas in df as a dataframe 
data=pd.read_csv('gapminder.csv')
df=data.copy()

# Renaming the columns for ease of use 
df.columns = ['country', 'year', 'fertility', 'life_exp', 'pop', 'child_mortality','gdp', 'region']

# Defining a function to plot a line chart for five coutries to compare their GDP
def gdp_graph(selected_countries, df):
    # Filter data for the selected countries
    countries_data = df[df['country'].isin(selected_countries)]

    # Plotting
    plt.figure(figsize=(12, 8))

    # Loop through selected countries and plot the data
    for country in selected_countries:
        country_data = countries_data[countries_data['country'] == country]
        plt.plot(country_data['year'], country_data['gdp'], marker='o', linestyle='-', label=country)

    # Adding labels and title
    plt.title('GDP Trends Over Time for Selected Countries')
    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

# Defining a function plot a Bar chart for Fertility with respect to Region
def fertility_graph_regions(df):
    # Group by region and calculate the average fertility rate
    region_fertility = df.groupby('region')['fertility'].mean()

    # Plotting the bar chart
    plt.figure(figsize=(12, 8))
    region_fertility.plot(kind='bar', color='mediumseagreen')

    # Adding labels and title
    plt.title('Average Fertility Rate by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Fertility Rate')

    # Show the plot
    plt.grid(axis='y')
    plt.show()

# Defining a funtion to plot a Pie chart with respect to region to showcase Population percentage
def pie_chart(df, column_name):
    # Group by the specified column and calculate the total
    data_grouped = df.groupby(column_name)['pop'].sum()

    # Plotting the pie chart
    plt.figure(figsize=(10, 10))
    plt.pie(data_grouped, labels=data_grouped.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

    # Adding title
    plt.title(f'Population Distribution by {column_name}')

    # Show the plot
    plt.show()

# Calling line plot funtion and also mentioning the five coutries we want to compare the gdp of
s_countries = ['Australia', 'Canada', 'Indonesia', 'Sweden', 'United Kingdom']
gdp_graph(s_countries, df)

# Calling Pie chart function and also mentioning the specific region 
pie_chart(df, 'region')

# Calling bar chart function 
fertility_graph_regions(df)