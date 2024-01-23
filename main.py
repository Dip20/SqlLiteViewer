import tkinter as tk
from tkinter import filedialog
import sqlite3


class SQLiteViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite Database Viewer")
        root.geometry("1200x700")

        # Database Connection
        self.conn = None

        # UI Components
        self.upload_button = tk.Button(root, text="Upload Database", command=self.upload_database)
        self.upload_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.show_tables_button = tk.Button(root, text="Show Tables", command=self.show_tables)
        self.show_tables_button.grid(row=0, column=0, padx=(120, 100), pady=10, sticky="w")

        # Dictionary to store buttons for each table
        self.table_buttons = {}

        self.data_text = tk.Text(root, height=20, width=140)
        self.data_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


    def upload_database(self):
        file_path = filedialog.askopenfilename(filetypes=[("SQLite Database Files", "*.db;*.sqlite;*.db3")])
        if file_path:
            # Close existing connection, if any
            if self.conn:
                self.conn.close()

            # Open a new connection to the selected SQLite database
            self.conn = sqlite3.connect(file_path)

    def get_table_list(self):
        # Retrieve the list of tables in the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        return [table[0] for table in tables]

    def show_tables(self):
        # Show the list of tables and create buttons for each table
        if self.conn:
            tables = self.get_table_list()
            self.data_text.delete(1.0, tk.END)  # Clear existing text

            # Create buttons for each table
            for i, table in enumerate(tables):
                button = tk.Button(self.root, text=table, command=lambda t=table: self.show_table_data(t))
                button.grid(row=2, column=0, padx=10 + i * 80, pady=5, sticky="w")
                self.table_buttons[table] = button
        else:
            self.data_text.delete(1.0, tk.END)
            self.data_text.insert(tk.END, "Please upload a database first.")

    def show_table_data(self, table_name):
        # Retrieve and display data from the selected table
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name};")
        data = cursor.fetchall()

        # Display data in the Text widget
        self.data_text.delete(1.0, tk.END)  # Clear existing text
        for row in data:
            self.data_text.insert(tk.END, str(row) + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = SQLiteViewerApp(root)
    root.mainloop()
