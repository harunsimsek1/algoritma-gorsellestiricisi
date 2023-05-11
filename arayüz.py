import random
import time
import winsound
from tkinter import *
from tkinter import ttk
from sorting import Sortings

sortings = Sortings()

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry('900x600')
root.config(bg='lightgray')

# Variables
selected_alg = StringVar()
data = []

# Function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # Top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # Bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="white")
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), fill='white', font='Arial 8')

    root.update_idletasks()


def generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal + 1, maxVal + 1))

    drawData(data, ['#c0c0c0' for x in range(len(data))])


def startAlgorithm():
    global data
    if not data:
        return

    if algMenu.get() == 'Quick Sort':
        sortings.quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())

    elif algMenu.get() == 'Bubble Sort':
        sortings.bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Selection Sort':
        sortings.selection_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        sortings.merge_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        sortings.insertion_sort(data, drawData, speedScale.get())

    drawData(data, ['green' for x in range(len(data))])


# Frame / Base Layout
UI_frame = Frame(root, width=900, height=300, bg='lightgray')
UI_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=900, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=10)

# User Interface Area
# Row[0]
Label(UI_frame, text="Algorithm: ", bg='lightgray', fg='black', font='Arial 12').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Selection Sort', 'Quick Sort',
                                                                   'Merge Sort', 'Insertion Sort'], font='Arial 12')
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, bg='white',
                   label="Select Speed [s]", font='Arial 12')
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=startAlgorithm, bg='green', fg='white', font='Arial 12', relief=RAISED).grid(row=0, column=3, padx=10, pady=10)

# Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, bg='white', label="Data Size", font='Arial 12')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value", bg='white', font='Arial 12')
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value", bg='white', font='Arial 12')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=generate, bg='gray', fg='white', font='Arial 12', relief=RAISED).grid(row=1, column=3, padx=10, pady=10)



root.mainloop()