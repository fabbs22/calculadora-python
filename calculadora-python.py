import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("350x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E3440")

        self.expressao = ""

        self.visor = tk.Entry(
            root,
            font=("Arial", 24),
            bg="#3B4252",
            fg="#ECEFF4",
            bd=10,
            relief=tk.FLAT,
            justify="right"
        )
        self.visor.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=15)

        self.botoes_frame = tk.Frame(root, bg="#2E3440")
        self.botoes_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

        botoes = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2)
        ]

        self.criar_botoes(botoes)

    def criar_botoes(self, botoes):
        for i in range(5):
            self.botoes_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.botoes_frame.columnconfigure(i, weight=1)

        for texto, linha, coluna in botoes:
            if texto in ['/', '*', '-', '+', '=']:
                cor_bg = "#88C0D0"
                cor_fg = "#2E3440"
            elif texto == 'C':
                cor_bg = "#BF616A"
                cor_fg = "#ECEFF4"
            else:
                cor_bg = "#4C566A"
                cor_fg = "#ECEFF4"

            colspan = 2 if texto == '=' else 1

            btn = tk.Button(
                self.botoes_frame,
                text=texto,
                font=("Arial", 16, "bold"),
                bg=cor_bg,
                fg=cor_fg,
                activebackground="#D8DEE9",
                bd=0,
                command=lambda t=texto: self.ao_clicar(t)
            )
            btn.grid(row=linha, column=coluna, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    def ao_clicar(self, valor):
        if valor == "C":
            self.expressao = ""
            self.atualizar_visor("")
        elif valor == "=":
            try:
                resultado = str(eval(self.expressao))
                self.atualizar_visor(resultado)
                self.expressao = resultado
            except Exception:
                self.atualizar_visor("Erro")
                self.expressao = ""
        else:
            self.expressao += str(valor)
            self.atualizar_visor(self.expressao)

    def atualizar_visor(self, valor):
        self.visor.delete(0, tk.END)
        self.visor.insert(0, valor)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()