import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Простое приложение для рисования")

        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack()

        self.pen_color = "black"
        self.pen_width = 2

        self.create_ui()

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def create_ui(self):
        self.pen_color_label = ttk.Label(root, text="Цвет пера:")
        self.pen_color_label.pack()

        self.color_picker = ttk.Button(root, text="Выбрать цвет", command=self.pick_color)
        self.color_picker.pack()

        self.pen_width_label = ttk.Label(root, text="Толщина пера:")
        self.pen_width_label.pack()

        self.width_scale = ttk.Scale(root, from_=1, to=10, orient="horizontal", command=self.set_pen_width)
        self.width_scale.set(2)
        self.width_scale.pack()

        self.clear_button = ttk.Button(root, text="Очистить", command=self.clear_canvas)
        self.clear_button.pack()

    def pick_color(self):
        color = askcolor()[1]
        if color:
            self.pen_color = color

    def set_pen_width(self, value):
        self.pen_width = int(value)

    def start_drawing(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.pen_color, width=self.pen_width, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.last_x = x
        self.last_y = y

    def stop_drawing(self, event):
        pass

    def clear_canvas(self):
        self.canvas.delete("all")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    app.run()
