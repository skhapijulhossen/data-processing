import matplotlib.pyplot as plt

# Initializing The Graph
def plot_initializer(xli: int):
    # Setting Figure size
    plt.figure(figsize=(10, 4))
    # Annotating x and y axis
    plt.xlim((0, xli))
    plt.ylim((0,1))
    plt.yticks([0.25, 0.50, 0.75],["-v","0", "+v"])
    plt.xticks([xli//2], [" "])

    # Setting Customize Grid for signals
    for i in range(xli):
        plt.plot([i+1, i+1], [-1, xli], color="lightgrey", linestyle="dashed")
    plt.plot([0, xli], [0.25, 0.25], color="lightgrey", linestyle="dotted")
    plt.plot([0, xli], [0.5, 0.5], color="lightgrey", linestyle="dashed")
    plt.plot([0, xli], [0.75, 0.75], color="lightgrey", linestyle="dotted")


# NRZ-L Signal encoding
def NRZ_L(data: list):
    # passing No of bits to encode into plot initializer
    plot_initializer(len(data))
    plt.title("NRZ-L")
    # Loop will process each bit encoding and plot signal
    for i in range(len(data)):
        if data[i] == 0:
            if data[i-1] == 0:
                plt.plot([i,i+1],[0.25,0.25], color="lightgreen", linewidth=9)
            else:
                plt.plot([i,i,i+1],[0.75,0.25,0.25], color="lightgreen", linewidth=9)
        else:
            if data[i-1]==1:
                plt.plot([i,i+1],[0.75,0.75],color="lightgreen", linewidth=9)
            else:
                plt.plot([i,i,i+1],[0.25,0.75,0.75],color="lightgreen", linewidth=9)
        # Annotating bits
        plt.text(round((i+(i+1))/2, 2),0.15, s=str(data[i]), color="lightgreen")
    # Saving as PNG and Showing the Graph
    plt.savefig("NRZ-L.png")
    plt.show()


def NRZ_I(data: list):
    # passing No of bits to encode into plot initializer
    plot_initializer(len(data))
    plt.title("NRZ-I")
    # Set from where to start
    if data[0] == 0:
        j=0.25
    else:
        j=0.75

    # Loop will process each bit encoding and plot signal
    for i in range(len(data)):
        if data[i] == 0:
            plt.plot([i,i+1],[j,j], color="purple", linewidth=9)
        else:
            if j == 0.25:
                plt.plot([i,i,i+1],[j,j+0.50,j+0.50], color="purple", linewidth=9)
                j= j+ 0.50
            else:
                plt.plot([i,i,i+1],[j,j-0.50,j-0.50], color="purple", linewidth=9)
                j= j-0.50
        # Annotating bits
        plt.text(round((i+(i+1))/2, 2),0.15, s=str(data[i]), color="purple")
    # Saving as PNG and Showing the Graph
    plt.savefig("NRZ-I.png")
    plt.show()
        


def Bipolar_AMI(data: list):
    # passing No of bits to encode into plot initializer
    plot_initializer(len(data))
    plt.title("BIPOLAR AMI")
    no_1 = 0
    # Loop will process each bit encoding and plot signal
    for i in range(len(data)):
        if data[i] == 0:
            plt.plot([i, i+1], [0.5,0.5], color="orange", linewidth=9)
            
        else:
            no_1 += 1
            if no_1 %2 == 0:
                plt.plot([i,i, i+1, i+1], [0.5,0.25,0.25,0.5], color="orange", linewidth=9)
            else:
                plt.plot([i,i, i+1, i+1], [0.5,0.75,0.75,0.5], color="orange", linewidth=9)
        # Annotating bits
        plt.text(round((i+(i+1))/2, 2),0.15, s=str(data[i]), color="orange")
    # Saving as PNG and Showing the Graph
    plt.savefig("Bipolar_AMI.png")
    plt.show()


def Manchester(data: list):
    # passing No of bits to encode into plot initializer
    plot_initializer(len(data))
    plt.title("Manchester")
    # Loop will process each bit encoding and plot signal
    for i in range(len(data)):
        if data[i] == 0:
            mid_x = round((i+(i+1))/2, 2)
            plt.plot([i,mid_x, mid_x, i+1], [0.75, 0.75, 0.25, 0.25], color="brown", linewidth=9)
        else:
            mid_x = round((i+(i+1))/2, 2)
            plt.plot([i,mid_x, mid_x, i+1], [0.25, 0.25,0.75, 0.75], color="brown", linewidth=9)
        if data[i] == data[i-1] and i>0:
                plt.plot([i,i], [0.75,0.25], color="brown", linewidth=9)
        # Annotating bits
        plt.text(round((i+(i+1))/2, 2),0.15, s=str(data[i]), color="brown")
    # Saving as PNG and Showing the Graph
    plt.savefig("Manchester.png")
    plt.show()


def Diff_Manchester(data: list):
    # passing No of bits to encode into plot initializer
    plot_initializer(len(data))
    plt.title("Differential Manchester Encoding")
    # Set to 0.75 to start from positive side
    stop = 0.75
    # Loop will process each bit encoding and plot signal
    for i in range(len(data)):
        if data[i] == 0:
            if stop == 0.75:
                mid_x = round((i+(i+1))/2, 2)
                plt.plot([i,i,mid_x,mid_x, i+1], [stop, stop-0.50,stop-0.50,stop,stop], color="magenta", linewidth=9)
            else:
                mid_x = round((i+(i+1))/2, 2)
                plt.plot([i,i,mid_x,mid_x, i+1], [stop, stop+0.50,stop+0.50,stop,stop], color="magenta", linewidth=9)
        else:
            if stop == 0.75:
                mid_x = round((i+(i+1))/2, 2)
                plt.plot([i,mid_x,mid_x, i+1], [stop, stop, stop-0.50,stop-0.50], color="magenta",linewidth=9 )
                stop -= 0.50
            else:
                mid_x = round((i+(i+1))/2, 2)
                plt.plot([i,mid_x,mid_x, i+1], [stop,stop, stop+0.50,stop+0.50], color="magenta", linewidth=9)
                stop += 0.50
        # Annotating bits
        plt.text(round((i+(i+1))/2, 2),0.15, s=str(data[i]), color="magenta")
    # Saving as PNG and Showing the Graph
    plt.savefig("differential-Manchester.png")
    plt.show()




if __name__ == '__main__':
    
    bit_data = [0, 1, 1,0, 0, 1, 1,0,1, 1 ,1, 1,0, 0, 1, 1,0, 1, 0, 1]

    NRZ_I(bit_data)
    NRZ_L(bit_data)
    Bipolar_AMI(bit_data)
    Manchester(bit_data)
    Diff_Manchester(bit_data)
