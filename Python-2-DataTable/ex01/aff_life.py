from load_csv import load
import matplotlib.pyplot as plt


def aff_life(df):
    """
    Display a line plot of France's life expectancy from a given DataFrame.

    The function filters the DataFrame for France, extracts the life
    expectancy values, and plots them over the years.
    The x-axis shows the years, and the y-axis shows life expectancy. Only
    every 40th year is shown on the x-axis.
    """
    france_data = df[df["country"] == "France"].drop(columns=["country"])
    france_data = france_data.iloc[0]
    plt.plot(france_data.index, france_data.values)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(france_data.index[::40])
    plt.show()


def main():
    """
    Main function to load the life expectancy dataset and display France's
    life expectancy plot.

    The function calls load() to read the CSV file and then aff_life() to
    display the plot.

    Any exceptions encountered during loading or plotting are caught and
    printed.
    """
    try:
        df = load("life_expectancy_years.csv")
        aff_life(df)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
