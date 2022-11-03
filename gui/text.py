from display import Display


class Text(Display):
    def __init__(self):
        Display.__init__(self)
        self.canvas1.create_text(420, 22, text="Enter a title:", font=("Helvetica", 13))
        self.canvas1.create_text(405, 70, text="Check for quantity >:", font=("Helvetica", 12))
        self.canvas1.create_text(100, 40, text="Enter number of books:", font=("Helvetica", 14))
        self.canvas1.create_text(440, 120, text="Filter by price:", font=("Helvetica", 12))
        self.canvas1.create_text(370, 150, text="from", font=("Helvetica", 12))
        self.canvas1.create_text(440, 150, text="to", font=("Helvetica", 12))
        self.canvas1.create_text(510, 150, text="GBP", font=("Helvetica", 12))
        self.canvas1.create_text(440, 190, text="Sort by price:", font=("Helvetica", 12))
        self.canvas1.create_text(100, 100, text="Select a category:", font=("Helvetica", 12))
        self.canvas1.create_text(100, 200, text="Filter by rating:", font=("Helvetica", 12))
        self.canvas1.create_text(140, 230, text="Sort by rating:", font=("Helvetica", 12))
