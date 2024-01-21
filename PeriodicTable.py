import tkinter as tk

class PeriodicTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Periodic Table")

        # Element data (name, symbol, atomic number, category)
        elements = [
            ("Hydrogen", "H", 1, "Nonmetal"),
            ("Helium", "He", 2, "Noble Gas"),
            ("Lithium", "Li", 3, "Alkali Metal"),
            ("Beryllium", "Be", 4, "Alkaline Earth Metal"),
            ("Boron", "B", 5, "Metalloid"),
            ("Carbon", "C", 6, "Nonmetal"),
            ("Nitrogen", "N", 7, "Nonmetal"),
            ("Oxygen", "O", 8, "Nonmetal"),
            ("Fluorine", "F", 9, "Halogens"),
            ("Neon", "Ne", 10, "Noble Gas"),
            # More element will be added
        ]

        # Define colors for different element categories
        category_colors = {
            "Nonmetal": "lightblue",
            "Noble Gas": "lightgreen",
            "Alkali Metal": "lightcoral",
            "Alkaline Earth Metal": "lightsalmon",
            "Metalloid": "lightcyan",
            "Halogens": "lightpink",
            # More categories and colors will be added
        }

        # Create labels for each element and place them on the grid
        for row in range(7):
            for col in range(18):
                element_index = row * 18 + col
                if element_index < len(elements):
                    element = elements[element_index]
                    category = element[3]
                    label_text = f"{element[1]}\n{element[0]}\n{element[2]}"
                    label = tk.Label(
                        root,
                        text=label_text,
                        relief="solid",
                        borderwidth=1,
                        padx=10,
                        pady=10,
                        bg=category_colors.get(category, "white"),
                    )
                    label.grid(row=row, column=col, sticky="nsew")

        # Configure grid weights to make labels expand with window resizing
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        for i in range(18):
            root.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableApp(root)
    root.mainloop()
