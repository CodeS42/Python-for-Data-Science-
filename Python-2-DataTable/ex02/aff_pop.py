from load_csv import load
import matplotlib.pyplot as plt


def aff_pop(df):
    """

    """
    
    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.show()


def main():
    """

    """
    try:
        df = load("population_total.csv")
        aff_pop(df)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
