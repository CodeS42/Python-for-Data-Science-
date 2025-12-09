from load_csv import load
import matplotlib.pyplot as plt


def filter_data(df):
    """
    Extract and clean numerical data for the year 1900 from a given DataFrame.

    The function selects the column corresponding to the year 1900, replaces
    shorthand notation using 'k' with scientific notation, and
    converts the resulting values into floats to ensure consistency for
    numerical processing and plotting.

    Returns a pandas Series containing cleaned float values for the year 1900.
    """
    data = df["1900"]
    data = data.replace({"k": "e3"}, regex=True).astype(float)
    return data


def projection_life(df1, df2):
    """
    Display a scatter plot comparing GDP per capita and life expectancy for
    1900.

    The function loads GDP data and life expectancy data for each country,
    cleans both datasets, and plots life expectancy (y-axis) against GDP per
    capita (x-axis) specifically for the year 1900. The x-axis is displayed on
    a logarithmic scale, with fixed tick marks at 300, 1k, and 10k GDP.
    """
    income_per_person = filter_data(df1)
    life_expectancy = filter_data(df2)

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xlim(300, 11000)
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.scatter(income_per_person, life_expectancy)
    plt.show()


def main():
    """
    Main function to load datasets and display the 1900 GDP vs. life
    expectancy plot.

    The function calls load() to read both the GDP and life expectancy CSV
    files, then calls projection_life() to generate the scatter plot. Any
    exceptions occurring during loading, processing, or plotting are caught
    and printed.
    """
    try:
        df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df2 = load("life_expectancy_years.csv")
        projection_life(df1, df2)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
