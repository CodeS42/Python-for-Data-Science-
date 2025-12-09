from load_csv import load
import matplotlib.pyplot as plt


def filter_data(country, df, years):
    """
    Extract and clean numerical data for a specific country and given years
    from a DataFrame.

    The function selects the row corresponding to the specified country, drops
    the 'country' column, replaces shorthand notations like 'k' and 'M' with
    scientific notation, converts all values to floats, and selects only the
    specified years.

    Returns a pandas Series containing cleaned float values for the specified
    years.
    """
    country_data = df[df["country"] == country].drop(columns=["country"])
    country_data = country_data.replace({"k": "e3", "M": "e6"}, regex=True)
    country_data = country_data.astype(float)
    country_data = country_data[years]
    country_data = country_data.iloc[0]
    return country_data


def aff_pop(df):
    """
    Display a line plot comparing population projections for France and
    Belgium.

    The function extracts population data for each country over the years
    1800–2050, cleans the data, and plots population (y-axis) against year
    (x-axis).
    """
    years = [year for year in df.columns[1:] if 1800 <= int(year) <= 2050]
    fr_data = filter_data("France", df, years)
    be_data = filter_data("Belgium", df, years)

    plt.plot(be_data.index, be_data.values, label="Belgium")
    plt.plot(fr_data.index, fr_data.values, label="France", color="green")
    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
    plt.xticks(years[::40])
    plt.title("Population Projections")
    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.legend(loc="lower right")
    plt.show()


def main():
    """
    Main function to load the population dataset and display the population
    projection plot.

    The function calls load() to read the population CSV file, then calls
    aff_pop() to generate the line plot. Any exceptions occurring during
    loading, processing, or plotting are caught and printed.
    """
    try:
        df = load("population_total.csv")
        aff_pop(df)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
