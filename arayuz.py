from tkinter import *
from tkinter import ttk
import random
from siralamalar import Sortings

sortings = Sortings()

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.attributes('-fullscreen', True)
root.config(bg='#303030')

selected_alg = StringVar()
data = []
graph_type = StringVar(value='scatter')

def exitFullscreen(event):
    root.attributes('-fullscreen', False)

root.bind('<Escape>', exitFullscreen)


def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 800
    c_width = 800
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]

    if graph_type.get() == 'scatter':
        for i, height in enumerate(normalizedData):
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * (c_height - offset - spacing)
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="")
            canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), fill='white', font='Arial 8')
            canvas.create_text(x0 + 2, y0 + 15, anchor=NW, text="Comparison: " + str(sortings.comparison_count), fill='white', font='Arial 8')
    elif graph_type.get() == 'bar':
        bar_width = x_width / 2
        for i, height in enumerate(normalizedData):
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * (c_height - offset - spacing)
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="")
            canvas.create_text(x0 + bar_width, y0 - 15, anchor=N, text=str(data[i]), fill='white', font='Arial 8')
            canvas.create_text(x0 + bar_width, y0, anchor=NW, text="Comparison: " + str(sortings.comparison_count), fill='white', font='Arial 8')

    elif graph_type.get() == 'stem':
        for i, height in enumerate(normalizedData):
            x = i * x_width + offset + spacing
            y = c_height - height * (c_height - offset - spacing)

            canvas.create_line(x, c_height, x, y, fill=colorArray[i], width=2)
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=colorArray[i], outline="")

    root.update_idletasks()


def generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal + 1, maxVal + 1))

    drawData(data, ['#004080' for x in range(len(data))])


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

    drawData(data, ['#4CAF50' for x in range(len(data))])
    sortings.complete_sorting()
    showComplexityAnalysis()


def stopAnimation():
    global animation_running
    animation_running = False


def resetAlgorithm():
    global data
    sortings.comparison_count = 0  # comparison_count değişkenini sıfırla
    data = []
    drawData(data, ['#004080' for x in range(len(data))])

def showComplexityAnalysis():
    algorithm = algMenu.get()
    complexity_label_text = get_complexity_analysis(algorithm)
    complexityLabel.config(text=complexity_label_text)


def get_complexity_analysis(algorithm):
    if algorithm == 'Bubble Sort':
        return "Best: O(n), Average: O(n^2), Worst: O(n^2)"
    elif algorithm == 'Selection Sort':
        return "Best: O(n^2), Average: O(n^2), Worst: O(n^2)"
    elif algorithm == 'Quick Sort':
        return "Best: O(n log n), Average: O(n log n), Worst: O(n^2)"
    elif algorithm == 'Merge Sort':
        return "Best: O(n log n), Average: O(n log n), Worst: O(n log n)"
    elif algorithm == 'Insertion Sort':
        return "Best: O(n), Average: O(n^2), Worst: O(n^2)"
    else:
        return ""


UI_frame = Frame(root, width=1200, height=800, bg='#303030')
UI_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

canvas = Canvas(root, width=1200, height=800, bg='#303030')
canvas.grid(row=0, column=1, padx=10, pady=10)

algorithm_frame = LabelFrame(UI_frame, text="Algorithm", bg='#303030', fg='white', font='Arial 12')
algorithm_frame.pack(fill=BOTH, padx=10, pady=10)

algMenu = ttk.Combobox(algorithm_frame, textvariable=selected_alg, values=['Bubble Sort', 'Selection Sort', 'Quick Sort',
                                                                           'Merge Sort', 'Insertion Sort'], font='Arial 12', state='readonly')
algMenu.pack(padx=10, pady=5)
algMenu.current(0)

speed_frame = LabelFrame(UI_frame, text="Speed", bg='#303030', fg='white', font='Arial 12')
speed_frame.pack(fill=BOTH, padx=10, pady=10)

speedScale = Scale(speed_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, bg='#ff8080',
                   label="Select Speed [s]", font='Arial 12')
speedScale.pack(padx=10, pady=5)

data_frame = LabelFrame(UI_frame, text="Data Generation", bg='#303030', fg='white', font='Arial 12')
data_frame.pack(fill=BOTH, padx=10, pady=10)

sizeEntry = Scale(data_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, bg='#ffff80', label="Data Size", font='Arial 12')
sizeEntry.pack(padx=10, pady=5)

minEntry = Scale(data_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value", bg='#ff80ff', font='Arial 12')
minEntry.pack(padx=10, pady=5)

maxEntry = Scale(data_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value", bg='#80ff80', font='Arial 12')
maxEntry.pack(padx=10, pady=5)

generateButton = Button(data_frame, text="Generate", command=generate, bg='#008080', fg='white', font='Arial 12', relief=RAISED)
generateButton.pack(padx=20, pady=30)

graph_frame = LabelFrame(UI_frame, text="Graph Type", bg='#303030', fg='white', font='Arial 12')
graph_frame.pack(fill=BOTH, padx=10, pady=10)

scatterRadio = Radiobutton(graph_frame, text="Scatter", variable=graph_type, value='scatter', bg='#303030', fg='white', font='Arial 12')
scatterRadio.pack(padx=10, pady=5, anchor=W)

barRadio = Radiobutton(graph_frame, text="Bar", variable=graph_type, value='bar', bg='#303030', fg='white', font='Arial 12')
barRadio.pack(padx=10, pady=5, anchor=W)

stemRadio = Radiobutton(graph_frame, text="Stem", variable=graph_type, value='stem', bg='#303030', fg='white', font='Arial 12')
stemRadio.pack(padx=10, pady=5, anchor=W)

startButton = Button(UI_frame, text="Start", command=startAlgorithm, bg='#008080', fg='white', font='Arial 12', relief=RAISED)
startButton.pack(side=LEFT, padx=10, pady=10)

stopButton = Button(UI_frame, text="Stop", command=stopAnimation, bg='#008080', fg='white', font='Arial 12', relief=RAISED)
stopButton.pack(side=LEFT, padx=10, pady=10)

resetButton = Button(UI_frame, text="Reset", command=resetAlgorithm, bg='#008080', fg='white', font='Arial 12', relief=RAISED)
resetButton.pack(side=LEFT, padx=10, pady=10)

complexityLabel = Label(UI_frame, text="Comparison:", bg='#303030', fg='white', font='Arial 12')
complexityLabel.pack(side=LEFT, padx=10, pady=10)

root.mainloop()