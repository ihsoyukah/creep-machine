from tkinter import *

root = Tk() #makes the boxy window thing
root.title('Creep Machine Acquisition Program')
root.iconbitmap(r"C:\Users\ihsoy\OneDrive\Documents\school\uc davis\zhang lab\GUI\creeper.ico")


#making buttons and setting up program outline
selectPlotButton=Button(root, text='Select Plot',padx=35,pady=10) #command=m1.selectPlot
selectPlotButton.grid(row=1)

#lead this one into 3 more buttons for strain/strain rate/stress vs time

newDataRateButton=Button(root, text='New Data Rate',padx=35,pady=10)
newDataRateButton.grid(row=2)

newSpansButton=Button(root, text='New Spans',padx=35,pady=10)
newSpansButton.grid(row=3)

dataTransferButton=Button(root, text='Data Transfer',padx=35,pady=10)
dataTransferButton.grid(row=4)

startTestButton=Button(root, text='Start Test',padx=35,pady=10)
startTestButton.grid(row=5)

endTestButton=Button(root, text='End Test',padx=35,pady=10)
endTestButton.grid(row=6)

endAllTestsButton=Button(root, text='End All Tests',padx=35,pady=10)
endAllTestsButton.grid(row=7)

exitButton=Button(root, text='Exit Program',padx=35,pady=10,command=root.quit)
exitButton.grid(row=8)

#put figures in from Ravela 
#make buttons that switch between gifures





def myClick():
    myLabel = Label(root, text='Hello' + e.get())
   
    
myButton = Button(root, text='Enter your name',command=myClick)


root.mainloop()





