import tkinter as tk
from tkinter import filedialog, messagebox
import string

class CipherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cipher Tool")

        # Create a frame for the input fields
        self.input_frame = tk.LabelFrame(master, text="Input")
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Create a label and input field for the key
        self.key_label = tk.Label(self.input_frame, text="Key (min. 12 characters):")
        self.key_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.key_entry = tk.Entry(self.input_frame, width=40)
        self.key_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Create a label and text area for the input text
        self.input_text_label = tk.Label(self.input_frame, text="Input Text:")
        self.input_text_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.input_text_area = tk.Text(self.input_frame, height=10, width=40)
        self.input_text_area.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # Create a button for uploading a file
        self.upload_button = tk.Button(self.input_frame, text="Upload File", command=self.upload_file)
        self.upload_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        # Create a frame for the cipher selection
        self.cipher_frame = tk.LabelFrame(master, text="Cipher")
        self.cipher_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Create radio buttons for selecting the cipher
        self.cipher_var = tk.StringVar()
        self.cipher_var.set("Vigenere")
        self.vigenere_radio = tk.Radiobutton(self.cipher_frame, text="Vigenere Cipher", variable=self.cipher_var, value="Vigenere")
        self.vigenere_radio.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.playfair_radio = tk.Radiobutton(self.cipher_frame, text="Playfair Cipher", variable=self.cipher_var, value="Playfair")
        self.playfair_radio.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.hill_radio = tk.Radiobutton(self.cipher_frame, text="Hill Cipher", variable=self.cipher_var, value="Hill")
        self.hill_radio.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # Create buttons for encrypting and decrypting
        self.encrypt_button = tk.Button(self.cipher_frame, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.decrypt_button = tk.Button(self.cipher_frame, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        # Create a label and text area for the output
        self.output_label = tk.Label(master, text="Output:")
        self.output_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.output_text_area = tk.Text(master, height=10, width=40)
        self.output_text_area.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.input_text_area.delete("1.0", "end")
                self.input_text_area.insert("1.0", file.read())

    def encrypt(self):
        key = self.key_entry.get()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long")
            return
        cipher = self.cipher_var.get()
        input_text = self.input_text_area.get("1.0", "end-1c")
        if cipher == "Vigenere":
            output_text = self.vigenere_encrypt(input_text, key)
        elif cipher == "Playfair":
            output_text = self.playfair_encrypt(input_text, key)
        else:
            output_text = self.hill_encrypt(input_text, key)
        self.output_text_area.delete("1.0", "end")
        self.output_text_area.insert("1.0", output_text)

    def decrypt(self):
        key = self.key_entry.get()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long")
            return
        cipher = self.cipher_var.get()
        input_text = self.input_text_area.get("1.0", "end-1c")
        if cipher == "Vigenere":
            output_text = self.vigenere_decrypt(input_text, key)
        elif cipher == "Playfair":
            output_text = self.playfair_decrypt(input_text, key)
        else:
            output_text = self.hill_decrypt(input_text, key)
        self.output_text_area.delete("1.0", "end")
        self.output_text_area.insert("1.0", output_text)

    def vigenere_encrypt(self, text, key):
        key = key.upper()
        text = text.upper()
        output_text = ""
        for i in range(len(text)):
            shift = ord(key[i % len(key)]) - 65
            output_text += chr((ord(text[i]) - 65 + shift) % 26 + 65)
        return output_text

    def vigenere_decrypt(self, text, key):
        key = key.upper()
        text = text.upper()
        output_text = ""
        for i in range(len(text)):
            shift = ord(key[i % len(key)]) - 65
            output_text += chr((ord(text[i]) - 65 - shift) % 26 + 65)
        return output_text

    def playfair_encrypt(self, text, key):
        key = key.upper()
        text = text.upper()
        key_matrix = self.playfair_get_key_matrix(key)
        output_text = ""
        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            if len(pair) == 1:
                pair += "X"
            if pair[0] == " " or pair[1] == " ":
                output_text += pair
            else:
                row1, col1 = self.playfair_get_position(pair[0], key_matrix)
                row2, col2 = self.playfair_get_position(pair[1], key_matrix)
                if row1 == row2:
                    output_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
                elif col1 == col2:
                    output_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
                else:
                    output_text += key_matrix[row1][col2] + key_matrix[row2][col1]
        return output_text

    def playfair_decrypt(self, text, key):
        key = key.upper()
        text = text.upper()
        key_matrix = self.playfair_get_key_matrix(key)
        output_text = ""
        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            if len(pair) == 1:
                pair += "X"
            if pair[0] == " " or pair[1] == " ":
                output_text += pair
            else:
                row1, col1 = self.playfair_get_position(pair[0], key_matrix)
                row2, col2 = self.playfair_get_position(pair[1], key_matrix)
                if row1 == row2:
                    output_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
                elif col1 == col2:
                    output_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
                else:
                    output_text += key_matrix[row1][col2] + key_matrix[row2][col1]
        return output_text

    def playfair_get_key_matrix(self, key):
        key = key.replace(" ", "").upper()
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_matrix = []
        for char in key:
            if char not in key_matrix:
                key_matrix.append(char)
        for char in alphabet:
            if char not in key_matrix:
                key_matrix.append(char)
        key_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]
        return key_matrix

    def playfair_get_position(self, char, key_matrix):
        for i in range(5):
            for j in range(5):
                if key_matrix[i][j] == char:
                    return i, j

    def hill_encrypt(self, text, key):
        key = self.hill_get_key_matrix(key)
        text = text.upper()
        output_text = ""
        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            if len(pair) == 1:
                pair += "X"
            vector = [ord(pair[0]) - 65, ord(pair[1]) - 65]
            result = self.hill_matrix_multiply(key, vector)
            output_text += chr(result[0] % 26 + 65) + chr(result[1] % 26 + 65)
        return output_text

    def hill_decrypt(self, text, key):
        key = self.hill_get_key_matrix(key)
        key_inverse = self.hill_get_inverse_matrix(key)
        text = text.upper()
        output_text = ""
        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            if len(pair) == 1:
                pair += "X"
            vector = [ord(pair[0]) - 65, ord(pair[1]) - 65]
            result = self.hill_matrix_multiply(key_inverse, vector)
            output_text += chr(result[0] % 26 + 65) + chr(result[1] % 26 + 65)
        return output_text

    def hill_get_key_matrix(self, key):
        key = key.replace(" ", "").upper()
        key_matrix = []
        for char in key:
            key_matrix.append(ord(char) - 65)
        key_matrix = [key_matrix[i:i+2] for i in range(0, 4, 2)]
        return key_matrix

    def hill_get_inverse_matrix(self, key):
        det = key[0][0]*key[1][1] - key[0][1]*key[1][0]
        det_inverse = pow(det, -1, 26)
        inverse_matrix = [[(key[1][1]*det_inverse) % 26, (-key[0][1]*det_inverse) % 26],
                          [(-key[1][0]*det_inverse) % 26, (key[0][0]*det_inverse) % 26]]
        return inverse_matrix

    def hill_matrix_multiply(self, matrix1, matrix2):
        result = [0, 0]
        for i in range(2):
            for j in range(2):
                result[i] += matrix1[i][j] * matrix2[j]
        return result

root = tk.Tk()
my_gui = CipherGUI(root)
root.mainloop()