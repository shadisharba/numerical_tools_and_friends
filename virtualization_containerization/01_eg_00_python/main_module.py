import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    name = "tester"
    print()
    print(f"Hello, {name}!")

    x = [1, 2, 3, 4, 5]
    plt.plot(x)
    plt.grid()
    plt.savefig("plot.png")
