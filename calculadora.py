import customtkinter as ctk
import math
# from PIL import Image  # Não precisamos mais importar PIL

# Configurações de aparência
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Variável de expressão
expression = ""

def add_to_expression(value):
    global expression
    expression += str(value)
    entry_var.set(expression)

def clear():
    global expression
    expression = ""
    entry_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    entry_var.set(expression)

def calculate():
    global expression
    try:
        expr = expression.replace('÷', '/').replace('x', '*').replace('π', str(math.pi))
        expr = expr.replace('√', 'math.sqrt').replace('^', '**').replace('mod', '%')

        if '+' in expr and '%' in expr:
            parts = expr.split('+')
            if len(parts) == 2:
                try:
                    left_part = parts[0]
                    right_part = parts[1].strip()
                    if right_part.endswith('%'):
                        percent_value_str = right_part[:-1]
                        base_number = eval(left_part)
                        percent_value = eval(percent_value_str)
                        result = base_number + (base_number * percent_value / 100)
                        entry_var.set(str(result))
                        expression = str(result)
                        return
                except Exception as e:
                    entry_var.set("Erro")
                    expression = ""
                    print(f"Erro ao calcular adição com porcentagem: {e}")
                    return
        elif '-' in expr and '%' in expr:
            parts = expr.split('-')
            if len(parts) == 2:
                try:
                    left_part = parts[0]
                    right_part = parts[1].strip()
                    if right_part.endswith('%'):
                        percent_value_str = right_part[:-1]
                        base_number = eval(left_part)
                        percent_value = eval(percent_value_str)
                        result = base_number - (base_number * percent_value / 100)
                        entry_var.set(str(result))
                        expression = str(result)
                        return
                except Exception as e:
                    entry_var.set("Erro")
                    expression = ""
                    print(f"Erro ao calcular subtração com porcentagem: {e}")
                    return
        elif '*' in expr and '%' in expr:
            parts = expr.split('*')
            if len(parts) == 2:
                try:
                    left_part = parts[0]
                    right_part = parts[1].strip()
                    if right_part.endswith('%'):
                        percent_value_str = right_part[:-1]
                        base_number = eval(left_part)
                        percent_value = eval(percent_value_str)
                        result = base_number * (percent_value / 100)
                        entry_var.set(str(result))
                        expression = str(result)
                        return
                except Exception as e:
                    entry_var.set("Erro")
                    expression = ""
                    print(f"Erro ao calcular multiplicação com porcentagem: {e}")
                    return
        elif '/' in expr and '%' in expr:
            parts = expr.split('/')
            if len(parts) == 2:
                try:
                    left_part = parts[0]
                    right_part = parts[1].strip()
                    if right_part.endswith('%'):
                        percent_value_str = right_part[:-1]
                        base_number = eval(left_part)
                        percent_value = eval(percent_value_str)
                        result = base_number / (percent_value / 100) if percent_value != 0 else "Erro"
                        entry_var.set(str(result))
                        expression = str(result)
                        return
                except Exception as e:
                    entry_var.set("Erro")
                    expression = ""
                    print(f"Erro ao calcular divisão com porcentagem: {e}")
                    return
        elif '%' in expr:
            parts = expr.split('%')
            if len(parts) == 2 and not parts[1]:
                try:
                    left_operand = eval(parts[0])
                    result = left_operand / 100
                    entry_var.set(str(result))
                    expression = str(result)
                    return
                except Exception as e:
                    entry_var.set("Erro")
                    expression = ""
                    print(f"Erro ao calcular porcentagem: {e}")
                    return

        result = eval(expr)
        entry_var.set(str(result))
        expression = str(result)
    except Exception as e:
        entry_var.set("Erro")
        expression = ""
        print(f"Erro geral ao calcular: {e}")

# Interface principal
app = ctk.CTk()
app.title("Calculadora Simples")
app.geometry("360x540") # Reduzi a altura novamente
app.resizable(False, False)

# Campo de entrada
entry_var = ctk.StringVar()
entry = ctk.CTkEntry(app, textvariable=entry_var, font=("Arial", 28), width=320, height=80, justify="right")
entry.pack(pady=20, fill="x")

# Frame dos botões
frame = ctk.CTkFrame(app)
frame.pack(expand=True, fill="both")

# Lista de botões
buttons = [
    ["C", "÷", "%", "⌫"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "^", "="]
]

# Dicionário para guardar os botões
button_objects = {}

# Gera os botões dinamicamente
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "=":
            action = calculate
            button_color = "orange"
        elif text == "C":
            action = clear
            button_color = None
        elif text == "⌫":
            action = backspace
            button_color = None
        else:
            action = lambda x=text: add_to_expression(x)
            button_color = None

        button = ctk.CTkButton(
            frame,
            text=text,
            command=action,
            width=70,
            height=70,
            font=("Arial", 20),
            fg_color=button_color
        )
        button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
        button_objects[(i, j)] = button

# Ajuste das colunas e linhas do frame dos botões
for i in range(4):
    frame.grid_columnconfigure(i, weight=1, uniform="equal")
for i in range(5):
    frame.grid_rowconfigure(i, weight=1, uniform="equal")

app.mainloop()