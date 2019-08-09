# sizer
# tuple = (3,)  ...  3 또는 (3)은 tuple이 아니다.
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 250)) 
        
        panel1 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)      
        
        panel1.SetBackgroundColour("BLUE")
        panel2.SetBackgroundColour("red")
        
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel1, 1, wx.EXPAND)  # 1/3 영역    # EXPAND : 확장
        box.Add(panel2, 2, wx.EXPAND)  # 2/3 영역
        
        self.SetSizer(box)               
        self.Center()
        self.Show()
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title='사이저연습')
    app.MainLoop()