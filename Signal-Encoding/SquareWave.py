import numpy as np
import matplotlib.pyplot as plt

def Sn():
    """
    This Function will Produce graph.
    it will use the global n value no of harmonics. Which should be '<= 11'.
    """
    # taking global n value
    global n

    # Initializing Graph
    plt.figure(figsize=(6,4))
    plt.title("Square wave using sum of Sinusoid's")
    plt.plot([0,1],[0,0], color="grey",linewidth=3)
    plt.ylabel("Volts")
    plt.xlabel(" t ")

    # Creates time interval
    t = np.linspace(0,1,100)
    y = np.zeros(100)

    # Calculate sum of Odd Harmonics
    for n in range(1,n,2):
        sin = np.sin(2*np.pi*n*t)/n
        y += sin
    y = (y*4)/np.pi

    # Plot the Graph
    plt.plot(t,y , color="orange")
    plt.grid(True, color="lightgrey")

    # To Save as .png file
    plt.savefig("squareWave.png")

    # Show The Graph
    plt.show()


if __name__ == "__main__":
    # Validating User input
    n = int(input("Enter Number of Harmonics should be <=11: "))
    if n <= 11:
        Sn()
    else:
        print("Entered Number of Harmonics is Greater than 11!")
