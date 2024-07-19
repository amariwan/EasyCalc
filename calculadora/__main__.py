import customtkinter
from .calculos import *

TITLE = "Calculator"
WIDTH = 470
HEIGHT = 620

class Calculator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # CONFIGURE WINDOW
        self.title(TITLE)
        self.resizable(False, False)
        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        # Main frame for the calculator UI
        self.main_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)
        ######################

        # Label to display operations
        self.label_operacao_value = customtkinter.StringVar()
        self.label_operacao = customtkinter.CTkLabel(
            self.main_frame,
            text="0 + 1",
            textvariable=self.label_operacao_value,
            anchor="e"
        )
        self.label_operacao.grid(row=0, sticky='nsew', padx=(10, 10))
        ####################

        # Entry widget for user input showing results
        self.entrada_value = customtkinter.StringVar()
        self.clear_entry_value()
        self.entrada = customtkinter.CTkEntry(
            self.main_frame,
            justify="right",
            textvariable=self.entrada_value,
            fg_color="transparent",
            font=("CTkFont", 50),
            border_width=0,
            height=40, corner_radius=0
        )
        # Remove the blinking text cursor
        self.entrada.configure(insertontime=0)
        self.entrada.grid(row=1, sticky="nsew", pady=(10, 50))
        self.entrada.bind("<Key>", self.format_text)
        #################

        # Button frame for calculator buttons
        self.buttons_frame = customtkinter.CTkFrame(
            self.main_frame, corner_radius=0, fg_color="transparent")
        self.buttons_frame.grid(row=2, sticky="nsew")
        self.buttons_frame.columnconfigure((0, 1, 2, 3), weight=1)
        self.buttons_frame.rowconfigure(0, weight=1)

        # ROW 0
        self.button_mod, self.render_button_mod = self.create_button(
            "%", (0, 0), "#323232", "#3c3c3c", command=lambda: self.select_operation("%"))
        self.button_CE, self.render_button_CE = self.create_button(
            "CE", (1, 0), "#323232", "#3c3c3c", command=self.clear_entry_value)
        self.button_C, self.render_button_C = self.create_button(
            "C", (2, 0), "#323232", "#3c3c3c", command=self.clear_all)
        self.button_clear, self.render_button_clear = self.create_button(
            "<x", (3, 0), "#323232", "#3c3c3c", command=self.remove_last_character)

        # ############# ROW 1
        self.button_1_div_x, self.render_button_1_div_x = self.create_button(
            "1/x", (0, 1), "#323232", "#3c3c3c", command=lambda: self.select_operation("1/"))
        self.button_square, self.render_button_square = self.create_button(
            "x²", (1, 1), "#323232", "#3c3c3c", command=lambda: self.select_operation("pow"))
        self.button_root_square, self.render_button_root_square = self.create_button(
            "√x", (2, 1), "#323232", "#3c3c3c", command=lambda: self.select_operation("sqrt"))
        self.button_div, self.render_button_div = self.create_button(
            "/", (3, 1), "#323232", "#3c3c3c", command=lambda: self.select_operation("/"))

        # ############# ROW 2
        self.button7, self.render_button7 = self.create_button(
            "7", (0, 2), command=lambda: self.insert_entry_value("7"))
        self.button8, self.render_button8 = self.create_button(
            "8", (1, 2), command=lambda: self.insert_entry_value("8"))
        self.button9, self.render_button9 = self.create_button(
            "9", (2, 2), command=lambda: self.insert_entry_value("9"))
        self.button_x, self.render_button_x = self.create_button(
            "X", (3, 2), "#323232", "#3c3c3c", command=lambda: self.select_operation("X"))

        # ############ Row 3
        self.button4, self.render_button4 = self.create_button(
            "4", (0, 3), command=lambda: self.insert_entry_value("4"))
        self.button5, self.render_button5 = self.create_button(
            "5", (1, 3), command=lambda: self.insert_entry_value("5"))
        self.button6, self.render_button6 = self.create_button(
            "6", (2, 3), command=lambda: self.insert_entry_value("6"))
        self.button_minus, self.render_button_minus = self.create_button(
            "-", (3, 3), "#323232", "#3c3c3c", command=lambda: self.select_operation("-"))

        # ############ Row 4
        self.button1, self.render_button1 = self.create_button(
            "1", (0, 4), command=lambda: self.insert_entry_value("1"))
        self.button2, self.render_button2 = self.create_button(
            "2", (1, 4), command=lambda: self.insert_entry_value("2"))
        self.button3, self.render_button3 = self.create_button(
            "3", (2, 4), command=lambda: self.insert_entry_value("3"))
        self.button_plus, self.render_button_plus = self.create_button(
            "+", (3, 4), "#323232", "#3c3c3c", command=lambda: self.select_operation("+"))

        # ############ Row 5
        self.button_plus_minus, self.render_button_plus_minus = self.create_button(
            "+/-", (0, 5), command=lambda: self.select_operation("negative"))
        self.button0, self.render_button0 = self.create_button(
            "0", (1, 5), command=lambda: self.insert_entry_value("0"))
        self.button_float, self.render_button_float = self.create_button(
            ",", (2, 5), command=lambda: self.insert_entry_value(","))
        self.button_result, self.render_button_result = self.create_button(
            "=", (3, 5), "#80c6fe", "#6da9d8", "#323232", command=self.calculate)
        
    # BUTTON WIDGET CREATION
    def create_button(self, text: str, pos: tuple,
                      fg_color="#3c3c3c",
                      hover_color="#323232", text_color="white", 
                      command=lambda: print("button")):
        """
        Creates a custom button with specified properties.
        """
        button = customtkinter.CTkButton(
            self.buttons_frame,
            corner_radius=5,
            font=("CTkFont", 19),
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            height=70,
            text=text,
            command=command
        )
        button.grid(column=pos[0], row=pos[1], padx=(2, 2), pady=(2, 2))
        return button

    # ENTRY FUNCTIONS
    def insert_entry_value(self, text):
        """
        Inserts text into the entry widget and formats the text.
        """
        current_text = self.entrada_value.get()
        if text == ',' and current_text.count(',') > 0:
            return

        self.entrada.insert('end', text)
        self.format_text()

    def format_text(self):
        """
        Formats the text in the entry widget.
        """
        current_value = self.entrada_value.get()
        if len(current_value) < 1:
            self.clear_entry_value()
        else:
            formatted_value = self.apply_number_mask(current_value)
            self.entrada_value.set(formatted_value)

    def apply_number_mask(self, text):
        """
        Formats integer numbers with thousand separators.
        """
        text_without_punctuation = self.remove_punctuation(text)
        if text_without_punctuation.isnumeric():
            text = f"{int(text_without_punctuation):,}".replace(",", ".")
        return text

    def clear_all(self):
        """
        Clears both the entry value and operation label.
        """
        self.clear_entry_value()
        self.label_operacao_value.set("")

    def clear_entry_value(self):
        """
        Clears the value in the entry widget.
        """
        self.entrada_value.set('0')

    def remove_last_character(self):
        """
        Removes the last character from the entry widget.
        """
        current_length = len(self.entrada_value.get())
        if current_length > 1:
            self.entrada.delete(current_length - 1, 'end')
        else:
            self.clear_entry_value()

    def format_key_event(self, event):
        """
        Formats text based on key events (numbers and commas).
        """
        current_value = self.entrada_value.get()
        if event.char.isdigit() or (event.char == ',' and current_value.count(',') < 1):
            self.insert_entry_value(event.char)
        elif event.keysym == "BackSpace":
            self.remove_last_character()
        return 'break'

    def select_operation(self, operation):
        """
        Updates the operation label with the selected operation.
        """
        value = self.entrada_value.get()
        if operation in ["sqrt", "pow", '1/', 'negative']:
            value = f"{operation}({value})"
        else:
            value = f"{value} {operation}"

        self.label_operacao_value.set(value)

    # Converts text from "1.000,01" to "1000.01"
    def remove_punctuation(self, text) -> str:
        return text.replace('.', '').replace(",", ".")

    # Converts values from "1000.01" to "1.000,01"
    def add_punctuation(self, text) -> str:
        def format_number(x): return f"{x:,}".replace(
            ".", "<").replace(",", ".").replace("<", ",")
        return format_number(text)

    # Converts the operation string "1250.35 + 0.5" to "1.250,35 + 0,5"
    def format_operation_text(self, operation):
        operation_list = operation.split(' ')
        for i, value in enumerate(operation_list):
            if value.isdigit() or value.replace('.', '').isdigit():
                operation_list[i] = self.add_punctuation(eval(value))

        operation_str = ' '.join(operation_list)
        return self.replace_operators(operation_str, 'value')

    def operators(self):
        """
        Returns a dictionary of operators and their corresponding functions.
        """
        return {
            "+": "+",
            "X": "*",
            "-": "-",
            "/": "/",
            "%": "%",
            "sqrt": "calculos.sqrt",
            "pow": "calculos.pow_square",
            "1/": "calculos.one_divided_n",
            "negative": "calculos.negative"
        }

    def replace_operators(self, operation, mode='key'):
        """
        Replaces operators with their corresponding function or symbol.
        """
        operators = self.operators()
        for key, value in operators.items():
            if mode == 'key':
                operation = operation.replace(key, value)
            else:
                operation = operation.replace(value, key)

        return operation

    def evaluate_add_punctuation(self, operation):
        """
        Evaluates the operation and adds punctuation to the result.
        """
        try:
            result = eval(operation)
            return self.add_punctuation(result)
        except ZeroDivisionError:
            return 'ZeroDivisionError'

    def calculate_result(self, operation_value, entry_value):
        """
        Calculates the result based on the current operation and entry value.
        """
        operators = self.operators()
        def contains_operator(x): return any(op in x for op in operators.values())

        operation = self.replace_operators(operation_value)
        operation_list = operation.split(' ')

        has_operator = contains_operator(operation)
        
        if has_operator:
            if len(operation_list) > 2:
                operation_list[0] = entry_value
            else:
                operation_list.append(entry_value)
                if len(operation_list) == 2:
                    operation_list.pop()

            operation = ' '.join(operation_list)
            result = operation
        else:
            operation = result = entry_value

        return self.evaluate_add_punctuation(result), self.format_operation_text(operation)

    def calculate(self):
        """
        Calculates the result of the operation and updates the UI.
        """
        operation_value = self.label_operacao_value.get()
        entry_value = self.entrada_value.get()

        operation_value = self.remove_punctuation(operation_value)
        entry_value = self.remove_punctuation(entry_value)

        result, formatted_operation = self.calculate_result(operation_value, entry_value)

        self.label_operacao_value.set(formatted_operation)
        self.entrada_value.set(result)
