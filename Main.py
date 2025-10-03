import Game_GUI
import Bot_AI as SB
import tkinter as tk

class WindowManger:
    def __init__(self, root):
        self.root = root
        self.setup_app = None
        self.game_app = None
        self.end_app = None

        self.setup_screen()
    
    def Del_screen(self):
        for window in self.root.winfo_children():
                window.destroy()
        return
    
    def setup_screen(self):
        self.Del_screen()
        self.setup_app = Game_GUI.SetupGUI(self.root, self.game_stt)
    
    def game_stt(self):
         self.Del_screen()
         self.diff = self.setup_app.diff_var.get()
         self.ply_mark = self.setup_app.ply_var.get()
         self.bot_mark = self.setup_app.bot_var.get()

         print(f"Starting Game with Difficulty: {self.diff}, Player Chose: {self.ply_mark}, Bot got: {self.bot_mark}") 
         self.game_logic = GameLogic(root, self.ply_mark, self.bot_mark, self.diff)
         

    def end_screen(self, result):
         self.Del_screen()
         self.end_app = Game_GUI.EndGUI(self.root, result, self.setup_screen, self.root.quit)

class GameLogic:
    def __init__(self, root, ply_mark, bot_mark, diff):
        self.root = root
        self.ply_mark = ply_mark
        self.bot_mark = bot_mark
        self.diff = diff
        self.Is_Ply_Turn = True

        if(self.ply_mark == "O"): self.Is_Ply_Turn = False
        
        self.Game_State = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.BotPckn = getattr(SB, f"BotPick_{self.diff}")
        self.Game_Ended = self.Is_Terminal_WLD()

        self.gm_UI = Game_GUI.GameGUI(self.root, self)
        if(not self.Is_Ply_Turn): self.root.after(500, self.Bot_Move)
        self.Update_UI()
    
    def Is_Terminal_WLD(self):
        Filled = 2
        GS = self.Game_State
        for i in range(len(GS)):
            if(GS[i] == 0): Filled = 0
    
        winCond = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for i in winCond:
            sum = 0
            for j in i:
                sum+=GS[j-1]
            if(sum == 15): 
                return 5
            elif(sum == 3): 
                return 1
        return Filled
    
    def Bot_Move(self):
        Pick = self.BotPckn(self.Game_State)
        self.Game_State[Pick] = 5
        self.Is_Ply_Turn = True
        self.Update_UI()

        self.Game_Ended = self.Is_Terminal_WLD()
        if(self.Game_Ended):
            self.GM_end(self.Game_Ended)

    def Ply_Move(self, Pick):
        if(not self.Is_Ply_Turn or self.Game_State[Pick] != 0): return

        self.Game_State[Pick] = 1
        self.Is_Ply_Turn = False
        self.Update_UI()

        self.Game_Ended = self.Is_Terminal_WLD()
        if(self.Game_Ended):
            self.GM_end(self.Game_Ended)
            return
        
        self.root.after(500, self.Bot_Move)
    
    def Update_UI(self):
        self.gm_UI.Update_Board(self.Game_State, self.ply_mark, self.bot_mark)
        if self.Is_Ply_Turn: T_Text = "X"
        else: T_Text = "O"
        self.gm_UI.Update_Turn(T_Text)
        return

    def GM_end(self, res):
        print("------GAME OVER------")
        if(res == 2): print("The Game was a DRAW!")
        elif(res == 5): print(f"Bot won :( as {self.bot_mark}")
        elif(res == 1): print(f"You Won! as {self.ply_mark}")
        app.end_screen(res)
        


if __name__ == "__main__":
     root = tk.Tk()
     app = WindowManger(root)
     root.mainloop()