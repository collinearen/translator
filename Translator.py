import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
from tkinter import scrolledtext

import numpy as np


class Translator(tk.Tk):
    number_of_indents, position, position_to_str = 0, 0, 0
    input_line, python_code, poliz = "", "", ""
    micro_poliz = []
    lines = []
    lists_of_types = ["int", "bool", "str"]
    equals = {":=": "="}
    variable_flag, literals_flag, type_flag, end_flag, enter_flag, success_end_flag, while_flag = (False, False, False,                                                                                              False, False, False,                                                                                                  False)
    bin_op = {"-": " - ", "+": " + ", "*": " * ", "/": " / "}
    literal = {
        "==": " == ",
        ">=": " >= ",
        "<=": " <= ",
        "<": " < ",
        ">": " > ",
        "<>": " != ",
        "(": "(",
        ")": ")",
        "+": " + ",
        "-": " - ",
        "*": " * ",
        "/": " / ",
        "&&": " and ",
        "||": " or ",
        ",": " , """,
        ":": " = "}

    list_of_literals = ["==",
                        ">=",
                        "<=",
                        "<",
                        ">",
                        "<>",
                        "(",
                        ")",
                        "+",
                        "-",
                        "*",
                        "/",
                        "&&",
                        "||",
                        ",",
                        ":=",
                        ":"]

    types = {"int": "0",
             "bool": "False",
             "str": ""}

    identifiers_flag = True
    L = {chr(i) for i in range(ord('a'), ord('z') + 1)}
    N = {chr(i) for i in range(ord('0'), ord('9') + 1)}

    def __init__(self):
        super().__init__()
        self.title("Translator")

        frame_poliz = tk.Frame(borderwidth=1, relief=tk.SOLID)
        frame_enter = tk.Frame(borderwidth=1, relief=tk.SOLID)

        tk.Label(frame_enter, text="Откройте файл с исходным кодом").grid(row=1, column=0, columnspan=2)
        tk.Label(frame_enter, text="Python-код").grid(row=7, column=1)
        tk.Label(frame_enter, text="Исходный код").grid(row=7, column=0)
        tk.Label(frame_enter, text="Вывод ошибок и предупреждений").grid(row=11, column=0, columnspan=2)

        self.entry = tk.Entry(frame_poliz)
        btn_file = tk.Button(frame_enter, text="Загрузить код",
                             command=self.choose_file)

        btn_ini = tk.Button(frame_enter, text="Анализ",
                            command=self.analyze)
        btn_close = tk.Button(frame_enter, text="Выход из программы",
                              command=self.close)

        self.text_mistakes = scrolledtext.ScrolledText(frame_enter, width=30, height=10)
        self.text_start_python_code = scrolledtext.ScrolledText(frame_enter, width=20, height=15)
        self.text_end_python_code = scrolledtext.ScrolledText(frame_enter, width=20, height=15)
        self.poliz_text = scrolledtext.ScrolledText(frame_poliz, width=20, height=10)
        self.identifikator_text = scrolledtext.ScrolledText(frame_poliz, width=20, height=10)

        # Расположение кнопок и полей
        self.identifikator_text.grid(column=0, row=4)
        self.entry.grid(row=5, column=0, sticky=tk.W)
        frame_enter.pack(anchor=tk.NW, side=tk.LEFT)
        self.text_mistakes.grid(row=12, column=0, columnspan=2, sticky="ew")
        self.poliz_text.grid(column=0, row=1)
        self.text_end_python_code.grid(column=1, row=8)
        self.text_start_python_code.grid(column=0, row=8)
        btn_ini.grid(column=0, row=10, sticky="ew", columnspan=2)
        btn_close.grid(column=0, row=13, columnspan=2)

        btn_file.grid(row=2, column=0, sticky="ew", columnspan=2)

    def close(self):
        Translator.destroy(self)

    def choose_file(self):
        if self.text_end_python_code.get(0.0, tk.END) != "":
            self.text_end_python_code.delete(0.0, tk.END)
        if self.text_mistakes.get(0.0, tk.END) != "":
            self.text_mistakes.delete(0.0, tk.END)
        if self.text_start_python_code.get(0.0, tk.END) != "":
            self.text_start_python_code.delete(0.0, tk.END)
        self.text_mistakes.insert(tk.END, f"Запись кода")
        self.lines = []
        if self.entry.get() == "":
            filetypes = (
                ("Текстовый файл", "*.txt"),
                ("Любой", "*"),
                ("Изображение", "*.jpg *.gif *.png"))
            try:
                filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                              filetypes=filetypes)
            except:
                messagebox.showerror("Внимание", "Данный файл недоступен")
                return
        else:
            filename = self.entry.get()
            self.entry.delete(0, tk.END)
        python_code_entry = ""

        if filename:
            try:
                with open(filename, 'r') as file:
                    self.entry.insert(0, filename)

                    self.lines = np.array(file.readlines())
                    for i in range(len(self.lines)):
                        python_code_entry += self.lines[i]
                    self.text_start_python_code.insert(tk.END, f"{python_code_entry}")
            except:
                messagebox.showerror("Внимание", "Данный файл недоступен")
                self.text_mistakes.insert(tk.END, f"\nВ записи файла произошла ошибка")
                return

    def parser(self):
        self.input_line = self.lines[self.position].split(' ')
        if self.nonterminal_d():
            while not self.end_prog():

                if self.number_of_indents != 0:
                    for i in range(self.number_of_indents):
                        self.python_code += "   "
                if self.nonterminal_f():
                    continue
                if self.nonterminal_p():
                    continue
                if self.nonterminal_w():
                    continue
            return True
        else:
            self.text_mistakes.insert(tk.END, f"\nЕсть ошибки в переходе на D")
            return False

    def analyze(self):
        while True:
            self.text_mistakes.insert(tk.END, f"\nНачало проверки")
            if self.parser():
                self.text_mistakes.insert(tk.END, f"\nПрограмма прошла проверку")
                break
            else:
                self.text_mistakes.insert(tk.END, f"\nКод ошибочен")
                break

    def nonterminal_i(self):
        if self.input_line[self.position_to_str] in self.L:
            self.python_code += f'{self.input_line[self.position_to_str]}'
            self.micro_poliz += self.input_line[self.position_to_str]
            if self.identifiers_flag:
                with open("identifiers.txt", "a") as file:
                    file.writelines(f"{self.input_line[self.position_to_str]} "
                                    f" -> {self.input_line[self.position_to_str + 2]}\n")
            return True
        else:
            return False

    def parsing_literals(self):
        if self.literals_flag:
            if self.input_line[self.position_to_str] in self.literal:
                self.python_code += f'{self.literal.get(self.input_line[self.position_to_str])}'
                if self.input_line[self.position_to_str] in self.list_of_literals:
                    self.micro_poliz += self.input_line[self.position_to_str]
                self.literals_flag = False
                return True
            else:
                self.literals_flag = False
                if not self.while_flag:
                    self.text_mistakes.insert(tk.END,
                                              f"Ошибка литерала в строке {self.position + 1}\n"
                                              f"В позиции {self.position_to_str + 1}")
                return False
        else:
            self.literals_flag = False

            return False

    def Type_detection(self):
        if self.type_flag:
            if self.input_line[self.position_to_str] in self.types:
                self.python_code += f'{self.types.get(self.input_line[self.position_to_str])}'
                if self.input_line[self.position_to_str] in self.lists_of_types:
                    self.micro_poliz += self.input_line[self.position_to_str]
                self.type_flag = False
                return True
            else:
                self.type_flag = False
                self.text_mistakes.insert(tk.END,
                                          f"Ошибка типа в строке "
                                          f"{self.position + 1}\nВ позиции {self.position_to_str + 1}")
                return False
        else:
            self.type_flag = False
            return False

    def end_detection(self):

        if self.end_flag:
            if self.enter_flag:  
                if self.input_line[self.position_to_str] == "\n":
                    poliz_on_sending = []
                    poliz_on_sending_new = ''
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.lists_of_types:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.L:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.N:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.list_of_literals:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(poliz_on_sending)):
                        poliz_on_sending_new += poliz_on_sending[i]
                    self.poliz += poliz_on_sending_new
                    self.micro_poliz = []
                    self.python_code += "\n"

                    self.position_to_str = 0
                    self.position += 1
                    self.input_line = self.lines[self.position].split(
                        ' ')
                    self.end_flag = False
                    self.enter_flag = False
                    return True
                else:
                    self.end_flag = False
                    self.enter_flag = False
                    self.text_mistakes.insert(tk.END,
                                              f"Ошибка конца строки {self.position + 1}\n"
                                              f"В позиции {self.position_to_str + 1}")
                    return False
            if self.success_end_flag:
                if self.input_line[self.position_to_str] == ";\n":
                    poliz_on_sending = []
                    poliz_on_sending_new = ''
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.lists_of_types:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.L:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.N:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.list_of_literals:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(poliz_on_sending)):
                        poliz_on_sending_new += poliz_on_sending[i]
                    self.poliz += poliz_on_sending_new
                    self.micro_poliz = []
                    self.python_code += "\n"
                    self.position_to_str = 0
                    self.position += 1
                    self.input_line = self.lines[self.position].split(' ')
                    self.end_flag = False
                    self.success_end_flag = False
                    return True
                else:
                    self.python_code += "\n"
                    self.position_to_str = 0
                    self.position += 1
                    self.input_line = self.lines[self.position].split(' ')
                    self.end_flag = False
                    self.success_end_flag = False
                    self.text_mistakes.insert(tk.END,
                                              f"Ошибка конца строки {self.position + 1}\nВ позиции {self.position_to_str + 1}")
                    return False
            # особая проверка для while, связанная с особенностью определения <Выражения>
            if self.while_flag == True:
                self.end_flag = False
                self.success_end_flag = False
                self.while_flag = False
                return True
        else:
            self.end_flag = False
            return False

    # создание списка переменных
    def nonterminal_v(self):
        if self.nonterminal_i():
            self.position_to_str += 1
            self.literals_flag = True
            if self.parsing_literals():
                self.type_flag = True
                self.position_to_str += 1
                if self.Type_detection():
                    self.end_flag = True
                    self.position_to_str += 1
                    if self.end_detection():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def nonterminal_d(self):
        if self.lines[self.position + 1] == "var\n":
            self.position += 2
            self.input_line = self.lines[self.position].split(' ')
            while self.lines[self.position] != "begin\n":
                self.success_end_flag = True
                if self.nonterminal_v():
                    self.input_line = self.lines[self.position].split(' ')
                else:
                    break
            if self.lines[self.position] == "begin\n":
                self.position += 1
                self.input_line = self.lines[self.position].split(' ')
                self.identifiers_flag = False
                return True
            else:
                return False
        else:
            self.text_mistakes.insert(tk.END, f"\nvar отсутствует")
            return False

    # функция проверки на присваивание
    def Equality(self):
        if self.input_line[self.position_to_str] in self.equals:
            self.python_code += self.equals.get(self.input_line[self.position_to_str])
            self.micro_poliz.append(':=')
            return True
        else:
            return False

    # нетерминал унарного оператора
    def nonterminal_u(self):
        if self.input_line[self.position_to_str] == "-":
            self.python_code += "-"
            return True
        else:
            return False

    # нетерминал Const
    def nonterminal_const(self):
        if self.input_line[self.position_to_str] in self.N:
            self.python_code += self.input_line[self.position_to_str]
            self.micro_poliz.append(self.input_line[self.position_to_str])
            return True
        else:
            return False

    def nonterminal_o(self):
        if self.nonterminal_i():
            self.position_to_str += 1
            return True
        elif self.nonterminal_const():
            self.position_to_str += 1
            return True
        else:
            return False

    def nonterminal_b(self):
        if self.input_line[self.position_to_str] in self.bin_op:
            self.python_code += self.bin_op.get(self.input_line[self.position_to_str])
            self.micro_poliz.append(self.input_line[self.position_to_str])
            return True
        self.literals_flag = True
        if self.parsing_literals():
            return True
        else:
            return False

    # нетерминал Н
    def nonterminal_h(self):
        if self.input_line[self.position_to_str] == "(":  # проверка на открытие скобок
            self.position_to_str += 1
            self.python_code += "("
            if self.nonterminal_e():  # обращение к нетерминалу Е
                self.position_to_str += 1  # сдвиг по строке
                if self.input_line[self.position_to_str] == ")":
                    self.python_code += ")"
                    self.end_flag = True
                    if self.end_detection():  # проверка на конец строки
                        return True
                    else:
                        return False
        elif self.nonterminal_o():  # обращение к нетерминалу O
            self.end_flag = True
            if self.input_line[self.position_to_str] == ";\n":
                poliz_on_sending = []
                poliz_on_sending_new = ''
                for i in range(len(self.micro_poliz)):
                    if self.micro_poliz[i] in self.L:
                        poliz_on_sending.append(self.micro_poliz[i])
                for i in range(len(self.micro_poliz)):
                    if self.micro_poliz[i] in self.N:
                        poliz_on_sending.append(self.micro_poliz[i])
                for i in range(len(self.micro_poliz)):
                    if self.micro_poliz[i] in self.list_of_literals:
                        poliz_on_sending.append(self.micro_poliz[i])
                for i in range(len(poliz_on_sending)):
                    poliz_on_sending_new += poliz_on_sending[i]
                self.poliz += poliz_on_sending_new
                self.micro_poliz = []
                self.python_code += "\n"
                self.position_to_str = 0
                self.position += 1
                self.input_line = self.lines[self.position].split(' ')
                self.end_flag = False
                self.enter_flag = False
                return True
            else:
                if self.nonterminal_h():
                    return True
                return False
        elif self.nonterminal_b():

            self.position_to_str += 1
            if self.nonterminal_h():
                return True

        elif self.number_of_indents != 0:
            self.end_flag = True
            if self.end_detection():
                self.input_line = self.lines[self.position].split(' ')
                return True

    # нетерминал Е
    def nonterminal_e(self):
        if self.nonterminal_u():
            self.position_to_str += 1

            if self.nonterminal_h():
                return True
            else:
                return False
        elif self.nonterminal_h():
            return True
        else:
            return False

    def nonterminal_a(self):
        if self.nonterminal_i():  # обращение к нетерминалу I
            self.position_to_str += 1  # сдвиг по строке
            if self.Equality():  # обращение к проверке на присваивание
                self.position_to_str += 1  # сдвиг по строке
                if self.nonterminal_e ():  # обращение к нетерминалу Е
                    return True
                else:
                    return False
            else:
                if self.nonterminal_b():  # обращение к нетерминалу В
                    self.position_to_str += 1  # сдвиг по строке
                    if self.nonterminal_e():  # обращение к нетерминалу Е
                        return True

                return False
        else:
            return False

    def nonterminal_g(self):
        if self.nonterminal_a():
            return True
        else:
            return False

    def end_prog(self):
        if self.input_line[0] == "end.":
            if self.play_py_code():
                return True
        else:
            return False

    def nonterminal_f(self):
        if self.while_flag:
            self.success_end_flag = False
        else:
            self.success_end_flag = True
        if self.nonterminal_g():
            return True
        else:
            return False

    def play_py_code(self):
        filename = 'results.py'
        with open(filename, 'w') as file:
            file.write(self.python_code)
        exec(open(filename).read())
        self.text_end_python_code.insert(tk.END, f"\n{self.python_code}")

        results_polize_name = "poliz.txt"
        with open(results_polize_name, 'w') as file:
            file.write(self.poliz)

        self.poliz_text.insert(tk.END, f"\n{self.poliz}")
        return True

    def nonterminal_p(self):
        if self.input_line[self.position_to_str] == "print":
            self.position_to_str += 1
            self.python_code += "print("
            self.poliz += "print"
            if self.nonterminal_i():
                self.position_to_str += 1
                self.python_code += ")"
                self.end_flag = True
                self.success_end_flag = True
                if self.end_detection():
                    self.poliz += ")"
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def nonterminal_w(self):
        if self.input_line[self.position_to_str] == "while":
            self.number_of_indents += 1
            self.position_to_str += 1
            self.python_code += "while "
            self.poliz += "While"
            self.while_flag = True
            if self.nonterminal_f():
                if self.input_line[self.position_to_str] == "do\n":
                    self.python_code += ":\n"
                    poliz_on_sending = []
                    poliz_on_sending_new = ''
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.L:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.N:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(self.micro_poliz)):
                        if self.micro_poliz[i] in self.list_of_literals:
                            poliz_on_sending.append(self.micro_poliz[i])
                    for i in range(len(poliz_on_sending)):
                        poliz_on_sending_new += poliz_on_sending[i]
                    self.poliz += poliz_on_sending_new
                    self.micro_poliz = []
                    self.position_to_str = 0
                    self.position += 1
                    self.input_line = self.lines[self.position].split(' ')
                    return True
        if self.input_line[self.position_to_str] == "endwhile\n":
            self.number_of_indents -= 1
            self.position += 1
            self.poliz += "EndWhile"
            self.input_line = self.lines[self.position].split(' ')
            self.position_to_str = 0
            return True
        else:
            return False

if __name__ == "__main__":
    Window = Translator()
    Window.mainloop()
