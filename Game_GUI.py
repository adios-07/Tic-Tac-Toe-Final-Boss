import tkinter as tk


class SetupGUI:
    def __init__(self, root, Start_Game):
        self.root = root

        self.C_BG = '#3d3d3d'
        self.C_CTR = '#4a4a4a'
        self.C_BTN = '#5a5a5a'
        self.C_TEXT = '#E0E0E0'
        self.C_Lbl = "#5a5a5a"
        self.C_Grn =  '#7ED321'
        self.C_Grn_Sl = "#95FF24"
        self.C_Blu = '#4287f5'
        self.C_X = '#4287f5'
        self.C_O = '#f57e42'
        self.F_LRG = ('Inter', 70, 'bold')
        self.F_Med = ('Inter', 32, 'bold')
        self.F_Sml = ('Inter', 18, 'bold')
        self.F_btn = ('Inter', 16, 'bold')

        self.root.title("Tic Tac Toe: Bot Edition")
        self.root.config(bg=self.C_BG)
        self.root.geometry('400x570')
        self.root.resizable(False, False)

        self.Main_CTR = tk.Frame(root, bg=self.C_BG, padx=20, pady=20)

        self.Game_Label = tk.Label(
            self.Main_CTR, bg=self.C_CTR, 
            text = "Game Setup",
            font = self.F_Med, fg=self.C_Grn,
            padx=5,pady=5
            )
        
        self.diff_frame = tk.Frame(self.Main_CTR, bg=self.C_BG)
        self.diff_lbl = tk.Label(self.diff_frame, text="Choose Difficulty: ", font=self.F_Sml, fg=self.C_Lbl, bg=self.C_BG)
        self.diff_lbl.pack(padx=0, pady=10, anchor='w')

        self.diff_var = tk.StringVar(value="Easy")
        self.diff_rbs = {}

        for val in ["Easy", "Medium", "Hard"]:
            rb = tk.Radiobutton(
                self.diff_frame,
                text=val,
                variable=self.diff_var,
                value=val,
                font=self.F_btn,
                fg=self.C_TEXT,
                bg=self.C_BTN,
                selectcolor=self.C_BTN,
                indicatoron=0,
                relief='flat', bd=0,
                activebackground=self.C_BTN,
                activeforeground=self.C_TEXT
            )
            self.diff_rbs[val] = rb
            rb.pack(side='left', padx=5, fill='x', expand=True)

        self.diff_var.trace_add('write', self.Update_Diff_Btn)


        self.ply_frame = tk.Frame(self.Main_CTR, bg=self.C_BG)
        self.ply_lbl = tk.Label(self.ply_frame, text="Choose Your Mark: ", font=self.F_Sml, fg=self.C_Lbl, bg=self.C_BG)
        self.ply_lbl.pack(padx=0, pady=10, anchor='w')

        self.ply_var = tk.StringVar(value="X")
        self.bot_var = tk.StringVar(value="O")
        
        self.x_rb = tk.Radiobutton(
                self.ply_frame,
                text="X", variable=self.ply_var, value="X", 
                font=self.F_LRG, fg=self.C_X, bg=self.C_BTN,
                selectcolor=self.C_BTN, indicatoron=0, relief='flat', bd=0,
                activebackground=self.C_BTN,
                activeforeground=self.C_X
                )
        self.x_rb.pack(side='left', padx=5, fill='x', expand=True,)

        self.o_rb = tk.Radiobutton(
                self.ply_frame,
                text="O", variable=self.ply_var, value="O", 
                font=self.F_LRG, fg=self.C_O, bg=self.C_BTN,
                selectcolor=self.C_BTN, indicatoron=0, relief='flat', bd=0,
                activebackground=self.C_BTN,
                activeforeground=self.C_O
                )
        self.o_rb.pack(side='left', padx=5, fill='x', expand=True,)

        self.ply_var.trace_add('write', self.Update_Mark_Btn)


        self.Stt_Btn = tk.Button(
            self.Main_CTR, text="Start Game",
            font=self.F_Med, 
            bg=self.C_Grn, fg=self.C_Lbl,
            relief='flat', bd=0,
            activebackground=self.C_Grn_Sl,
            activeforeground="#191919",
            command=Start_Game
        )


        self.Main_CTR.pack(padx=10, pady=10, fill='both', expand=True)
        self.Game_Label.pack(fill='x')
        self.diff_frame.pack(padx=0, pady=(20,0), fill='x')
        self.ply_frame.pack(padx=0, pady=20, fill='x')
        self.Stt_Btn.pack(padx=0, pady=20, fill='x', expand=True)

        self.Update_Diff_Btn()
        self.Update_Mark_Btn()


    def Update_Diff_Btn(self, *args):
        slctd_diff = self.diff_var.get()
        for val, rb in self.diff_rbs.items():
            if(val == slctd_diff):
                rb.config(bg=self.C_Blu, selectcolor=self.C_Blu)
            else:
                rb.config(bg=self.C_BTN, selectcolor=self.C_BTN)

    def Update_Mark_Btn(self, *args):
        slctd_mrk = self.ply_var.get()
        if(slctd_mrk == "X"):
            self.x_rb.config(bg=self.C_Blu, selectcolor=self.C_Blu, fg=self.C_TEXT)
            self.o_rb.config(bg=self.C_BTN, selectcolor=self.C_BTN, fg=self.C_O)
            self.bot_var = tk.StringVar(value="O")
        else:
            self.o_rb.config(bg=self.C_Blu, selectcolor=self.C_Blu, fg=self.C_TEXT)
            self.x_rb.config(bg=self.C_BTN, selectcolor=self.C_BTN, fg=self.C_X)
            self.bot_var = tk.StringVar(value="X")



class GameGUI:
    def __init__(self, root, cntlr):
        self.root = root
        self.cntlr = cntlr

        self.C_BG = '#3d3d3d'
        self.C_CTR = '#4a4a4a'
        self.C_BTN = '#5a5a5a'
        self.C_TEXT = '#E0E0E0'
        self.C_Lbl = "#5a5a5a"
        self.C_Grn =  '#7ED321'
        self.C_Blu = '#4287f5'
        self.C_X = '#4287f5'
        self.C_O = '#f57e42'
        self.F_LRG = ('Inter', 40, 'bold')
        self.F_Med = ('Inter', 30, 'bold')
        self.F_Sml = ('Inter', 25, 'bold')

        self.root.title("Tic Tac Toe: Bot Edition")
        self.root.config(bg=self.C_BG)
        self.root.geometry('400x570')
        self.root.resizable(False, False)

        self.Main_CTR = tk.Frame(root, bg=self.C_BG, padx=20, pady=20)
        self.Main_CTR.pack(padx=10, pady=10)

        self.Game_Label = tk.Label(
            self.Main_CTR, bg=self.C_CTR,
            padx=5,pady=7,
            text = "Game Window",
            font = self.F_Med, fg=self.C_Grn
            )
        
        self.Game_Grid = tk.Frame(self.Main_CTR, bg=self.C_CTR)

        self.Turn_Ind = tk.Label(
            self.Main_CTR,
            bg = self.C_BG,
            padx=0,pady=10,
            text = "Turn: ",
            anchor='w',
            font = self.F_Sml, fg=self.C_TEXT
        )

        #Pack in Order
        self.Game_Label.pack(side='top', fill='x', pady=(0, 10), padx=5)
        self.Game_Grid.pack(pady=10)
        self.Turn_Ind.pack(side='bottom', fill='x', pady=(10,0), padx=(5))

        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                self.Game_Grid, text="", 
                font=self.F_LRG, width=3, height=1,
                bg=self.C_BTN, relief="flat", bd=0,
                activebackground = '#6a6a6a',
                command=lambda ind=i: self.cntlr.Ply_Move(ind)
                )
            btn.grid(row = (i//3), column = (i%3), padx=5, pady=5)
            self.buttons.append(btn)
        return
    
    def Update_Board(self, GS, ply, bot): 
        if ply == "X": ply_c = self.C_X
        else: ply_c = self.C_O
        if bot == "X": bot_c = self.C_X
        else: bot_c = self.C_O
        for i in range(len(GS)):
            if(GS[i] == 1):
                self.buttons[i].config(text=ply, bg=self.C_BTN, state='disabled', disabledforeground=ply_c)
            elif(GS[i] == 5):
                self.buttons[i].config(text=bot, bg=self.C_BTN, state='disabled', disabledforeground=bot_c)
            else:
                self.buttons[i].config(text="", state='normal')
        return

    def Update_Turn(self, T_Text):
        self.Turn_Ind.config(text=f"Turn: {T_Text}")
        return


class EndGUI:
    def __init__(self, root, result, restt_gm, qt_gm):
        self.root = root

        self.C_BG = '#3d3d3d'
        self.C_CTR = '#4a4a4a'
        self.C_BTN = '#5a5a5a'
        self.C_TEXT = '#E0E0E0'
        self.C_Lbl = "#5a5a5a"
        self.C_Grn =  '#7ED321'
        self.C_Grn_Sl = '#95FF24'
        self.C_Red = "#f33131"
        self.C_Blu = '#4287f5'
        self.C_X = '#4287f5'
        self.C_O = '#f57e42'
        self.F_LRG = ('Inter', 40, 'bold')
        self.F_Med = ('Inter', 32, 'bold')
        self.F_Sml = ('Inter', 18, 'bold')
        self.F_btn = ('Inter', 16, 'bold')

        self.root.title("Game Over")
        self.root.config(bg=self.C_BG)
        self.root.geometry('390x250')
        self.root.resizable(False, False)

        self.Main_CTR = tk.Frame(root, bg=self.C_BG, padx=20, pady=20)
        self.Main_CTR.pack(padx=10, pady=10, fill='both', expand=True)

        if(result == 1):
            res = "YOU Win! ;)"
            res_c = self.C_Grn_Sl
        elif(result == 5):
            res = "You Lost! :("
            res_c = self.C_Red
        else:
            res = "it was a Draw"
            res_c = self.C_TEXT

        self.Res_Lbl = tk.Label(
            self.Main_CTR,
            text=res, fg=res_c, bg=self.C_BG,
            font=self.F_Med
        )

        self.rstt_Game = tk.Button(
            self.Main_CTR,
            text="Play Again ^_^", font=self.F_btn, fg=self.C_Lbl, bg=self.C_Grn,
            relief='flat', bd=0,
            activebackground=self.C_Grn_Sl,
            activeforeground="#191919",
            command=restt_gm
        )

        self.qt_Game = tk.Button(
            self.Main_CTR,
            text="Quit *..*", font=self.F_btn, fg=self.C_Lbl, bg=self.C_Grn,
            relief='flat', bd=0,
            activebackground=self.C_Grn_Sl,
            activeforeground="#191919",
            command=qt_gm
        )

        self.Res_Lbl.pack(padx=20, pady=(10,20))
        self.rstt_Game.pack(padx=50, pady=(0,20), fill='x', expand=True)
        self.qt_Game.pack(padx=50, pady=(0, 10), fill='x', expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = EndGUI(root, 5, max(1,2), min(1,3))
    #app = GameGUI(root, "Hard", "O", "X")
    root.mainloop()