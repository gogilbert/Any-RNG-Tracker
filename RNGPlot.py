import matplotlib.pyplot as plt
import numpy as np

#Plots two lines using matplotlib and saves to a file
def plot(totalTrials, totalRNGRupees, RNGFactor):
    plt.clf()
    plt.style.use('dark_background')
    ExpectedX = np.array(range(35))
    ExpectedY = ExpectedX*(RNGFactor)
    RealityX = np.array(range(35))
    RealityY = RealityX*(totalRNGRupees/totalTrials)
    plt.figure(figsize=(5,5))
    plt.plot(ExpectedX,ExpectedY, label="Expected RNG", color='red')
    plt.plot(RealityX,RealityY, label="Current RNG", color='green')
    plt.xlim(0, 30)
    plt.ylim(0, 30*RNGFactor)
    plt.title("RNG Rupees Graph")
    plt.ylabel("Runs with RNG")
    plt.xlabel("Total Runs")
    plt.locator_params(axis="both", integer=True, tight=True)
    plt.legend()
    plt.savefig("GraphOverlay.png", dpi=300, pad_inches=0.1)
    plt.close()
