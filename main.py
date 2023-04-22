import customtkinter as ctk
import RNGPlot
import TextWriter as tw

#Sets the CTK theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Sets the CTK window dimensions and background color
window = ctk.CTk()
window.geometry("430x90")
window.configure(fg_color='black')

#Initializes global vairables
totalTrials = 0
totalRNGRupees = 0

#RNG table for various bush cutting
RNGValues = [0.0359396, 0.0623236, 0.0971629, 0.1397928]

#Selection buttons current value
defaultBushSelection = ctk.StringVar(value="8")

#Called from the no rupee button
def NoRupeeButton():
    global totalTrials
    totalTrials+=1
    RNGPlot.plot(totalTrials, totalRNGRupees, RNGValues[int(defaultBushSelection.get())-5])
    tw.write(totalTrials, totalRNGRupees, int(defaultBushSelection.get()))

#Called from the RNG rupee button
def RNGButton():
    global totalTrials
    global totalRNGRupees

    totalTrials+=1
    totalRNGRupees+=1
    RNGPlot.plot(totalTrials, totalRNGRupees, RNGValues[int(defaultBushSelection.get())-5])
    tw.write(totalTrials, totalRNGRupees, int(defaultBushSelection.get()))

#Configures the window's grid layout
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure((0,1), weight=1)

#Segmented Button and label
BushSelectionButtons = ctk.CTkSegmentedButton(master=window, values=["5","6","7","8"], variable=defaultBushSelection)
BushSelectionButtons.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
BushSelectionLabel = ctk.CTkLabel(master=window, text="How many bushes do you plan on cutting?:")
BushSelectionLabel.grid(row=0, column=0, padx=10, pady=10)

#No Rupees Button
NoRupees = ctk.CTkButton(master=window, text="No RNG Rupees", command=NoRupeeButton)
NoRupees.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

#RNG Rupees Button
RNGRupees = ctk.CTkButton(master=window, text="RNG Rupees", command=RNGButton)
RNGRupees.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

window.mainloop()