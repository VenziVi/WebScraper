import Tkinter as tk
import tkFileDialog as filedialog
import ScrolledText


class PopUpWindowSuccess:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x100")
        self.root.minsize(500, 100)
        self.root.maxsize(500, 100)
        self.root.title("All done!")
        self.canvas2 = tk.Canvas(self.root, width=880, height=500)
        self.canvas2.pack(fill="both", expand=True)
        self.canvas2.create_text(222, 22, text="Collection JSON saved in output/Book collection.txt",
                                 font=("Helvetica", 14))
        self.viewFileButton = tk.Button(self.root, text="View File", command=self.openFile)
        self.viewFileButtonWindow = self.canvas2.create_window(200, 70, window=self.viewFileButton)

    def openFile(self):
        file_path = filedialog.askopenfilename(initialdir="output")
        print(file_path)
        file = open(file_path, 'r')
        text = file.read()

        popup = tk.Tk()
        popup.geometry("1200x800")
        popup.title("Books collection - all items matching your criteria:")
        txt = ScrolledText.ScrolledText(popup, undo=True)
        txt['font'] = ('Comic Sans', '12')
        txt.insert(tk.END, text)
        self.root.destroy()
        txt.pack(expand=True, fill='both')


class PopUpWindowFailure:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x100")
        self.root.minsize(500, 100)
        self.root.maxsize(500, 100)
        self.root.title("Collection is empty!")
        self.canvas2 = tk.Canvas(self.root, width=880, height=500)
        self.canvas2.pack(fill="both", expand=True)
        self.canvas2.create_text(222, 22, text="There were no items matching your criteria", font=("Helvetica", 14))
        self.OkButton = tk.Button(self.root, text="OK", command=self.closeWindow)
        self.OkButtonWindow = self.canvas2.create_window(250, 70, window=self.OkButton)

    def closeWindow(self):
        self.root.destroy()

