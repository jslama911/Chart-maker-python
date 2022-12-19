import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.ttk import Combobox
# Create the tkinter window
root = tk.Tk()
root.title("Charts")


chart_type_label = tk.Label(root, text="Select chart type:")
chart_type_label.pack()
chart_type = tk.StringVar()
chart_type_selection = tk.ttk.Combobox(root, textvariable=chart_type)
chart_type_selection["values"] = ("Bar", "Pie")
chart_type_selection.current(0)
chart_type_selection.pack()

# Allow for user input
a_label = tk.Label(root, text="First item:")
a_label.pack()
a_entry = tk.Entry(root)
a_entry.pack()

b_label = tk.Label(root, text="Second item:")
b_label.pack()
b_entry = tk.Entry(root)
b_entry.pack()

c_label = tk.Label(root, text="Third item:")
c_label.pack()
c_entry = tk.Entry(root)
c_entry.pack()

d_label = tk.Label(root, text="Fourth item:")
d_label.pack()
d_entry = tk.Entry(root)
d_entry.pack()

e_label = tk.Label(root, text="Fifth item:")
e_label.pack()
e_entry = tk.Entry(root)
e_entry.pack()

f_label = tk.Label(root, text="Enter a number for the first item:")
f_label.pack()
f_entry = tk.Entry(root)
f_entry.insert(0, "0")
f_entry.pack()

g_label = tk.Label(root, text="Enter a number for the second item:")
g_label.pack()
g_entry = tk.Entry(root)
g_entry.insert(0, "0")
g_entry.pack()

h_label = tk.Label(root, text="Enter a number for the third item:")
h_label.pack()
h_entry = tk.Entry(root)
h_entry.insert(0, "0")
h_entry.pack()

i_label = tk.Label(root, text="Enter a number for the fourth item:")
i_label.pack()
i_entry = tk.Entry(root)
i_entry.insert(0, "0")
i_entry.pack()

j_label = tk.Label(root, text="Enter a number for the fifth item:")
j_label.pack()
j_entry = tk.Entry(root)
j_entry.insert(0, "0")
j_entry.pack()

# Create a button to plot the pie chart
button = tk.Button(root, text="Plot")
button.pack()

def on_button_click():
    # Get the text from the Entry widgets
    a = (a_entry.get())
    b = (b_entry.get())
    c = (c_entry.get())
    d = (d_entry.get())
    e = (e_entry.get())
    f = float(f_entry.get())
    g = float(g_entry.get())
    h = float(h_entry.get())
    i = float(i_entry.get())
    j = float(j_entry.get())
    x = chart_type.get()
    root.destroy()

    if x == "Pie":
    # pie chart
        slices = [f, g, h, i ,j]
        items = [a, b, c, d, e]
        colors = ['#778899', '#DB7093', '#FFA500', '#FFD700', '#FF6347']
        

        plt.subplot(1,2,1)
        plt.pie(slices, labels = items, colors=colors, startangle=90)
        plt.title('Pie Chart')

        plt.show()

    elif x == "Bar":
    # bar chart
        items = [a, b, c, d, e]
        values = [f, g, h, i, j]
        colors = ['#778899', '#DB7093', '#FFA500', '#FFD700', '#FF6347']
       
        

        plt.subplot(1,2,2)
        plt.bar(items, values, color=colors)
        plt.title('Bar Chart')
        

        plt.show()

# Make the button work when clicked
button.configure(command=on_button_click)

root.mainloop()