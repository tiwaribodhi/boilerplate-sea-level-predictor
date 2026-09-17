import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # First line of best fit: all available data
    result = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    slope = result.slope
    intercept = result.intercept

    # Years for prediction
    years = pd.Series(
        range(df["Year"].min(), 2051)
    )

    # Predicted sea level
    predicted_sea_level = slope * years + intercept

    # Plot first regression line
    plt.plot(
        years,
        predicted_sea_level
    )

    # Second line of best fit: data from 2000 onward
    df_recent = df[df["Year"] >= 2000]

    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    slope_recent = result_recent.slope
    intercept_recent = result_recent.intercept

    # Years for second prediction
    years_recent = pd.Series(
        range(2000, 2051)
    )

    predicted_recent = (
        slope_recent * years_recent
        + intercept_recent
    )

    # Plot second regression line
    plt.plot(
        years_recent,
        predicted_recent
    )

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return
    plt.savefig("sea_level_plot.png")
    return plt.gca()