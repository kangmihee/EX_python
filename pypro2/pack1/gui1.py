# GUI 
# import wx
# app = wx.App()
# frame = wx.Frame(None, wx.ID_ANY, 'Hi')
# frame.Show(True)
# app.MainLoop()

import wx

class Ex(wx.Frame):
    def __init__(self, parent, title):
        super(Ex, self).__init__(parent, title = title, size=(300, 300))
        
        # TextBox
        #self.txtA = wx.TextCtrl(self)   # 글써짐 가능
        #self.txtA = wx.TextCtrl(self, style = wx.TE_MULTILINE) # 엔터 옵션
        self.CreateStatusBar()
        
        # 메뉴 
        menuBar = wx.MenuBar()      
        munFile = wx.Menu() 
               
        munNew = munFile.Append(wx.ID_NEW, 'New', '새글')       
        munOpen = munFile.Append(wx.ID_OPEN, 'Open', '열기')
        munFile.AppendSeparator() # 구분선 생성
        munExit = munFile.Append(wx.ID_EXIT, 'Exit', '종료')
        
        menuBar.Append(munFile, 'File')
        self.SetMenuBar(menuBar)
        
        # 메뉴에 이벤트 장착
        self.Bind(wx.EVT_MENU, self.OnEvent1, munNew)  # munNew (New버튼)
        self.Bind(wx.EVT_MENU, self.OnEvent2, munExit) # munExit(Exit버튼)
        
        # 라벨과 텍스트 박스 
        panel = wx.Panel(self)
        wx.StaticText(panel, label='i d : ', pos = (5,5))
        wx.StaticText(panel, label='pwd : ', pos = (5,40))
        self.txtA = wx.TextCtrl(panel, pos=(40, 5))
        self.txtB = wx.TextCtrl(panel, pos=(40, 40), size=(200, -1)) # 높이나 넓이에 -1이면 자동으로 크기 지정             
        
        # 버튼
        btn1 = wx.Button(panel, label='일반버튼', pos=(5, 100))        
        btn2 = wx.ToggleButton(panel, label='토글버튼', pos=(100,100))
        btn3 = wx.Button(panel, label='종 료', pos=(200, 100), size=(50,-1)) 
        
        # 버튼 - 이벤트 처리방법1 
        #btn1.Bind(wx.EVT_BUTTON, self.OnClick1)      
        #btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClick2)
        #btn3.Bind(wx.EVT_BUTTON, self.OnClick3)      
                     
        # 버튼 - 이벤트 처리방법2 
        btn1.id = 1
        btn2.id = 2
        btn3.id = 3       
        btn1.Bind(wx.EVT_BUTTON, self.OnHandler)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnHandler)
        btn3.Bind(wx.EVT_BUTTON, self.OnHandler)
                  
        self.Center()
        self.Show()
        
    # 이벤트 핸들러
    def OnEvent1(self, event): # munNew(New버튼클릭시 이벤트)
        #print('event 처리')
        #self.txtA.SetLabelText('New 메뉴 선택') 
        msgDial = wx.MessageDialog(self, '메세지', '제목', wx.OK)
        msgDial.ShowModal() # Modal은 포커싱이 열린 창에만 해당
        msgDial.Destroy() # Modal 닫기
        
    def OnEvent2(self,event): # munExit(New버튼클릭시 이벤트)
        self.Close() # Frame 닫기
                
    def OnClick1(self, event):
        self.txtA.SetLabel("버튼1")
        
    def OnClick2(self, event):
        #print(event.GetEventObject().GetValue()) # True/False 반환
        if event.GetEventObject().GetValue():
            self.txtA.SetLabel("kbs") # True일때
            self.txtB.SetLabel("9")
        else:
            self.txtA.SetLabel("mbc") # False일때
            self.txtB.SetLabel("11")
          
    def OnClick3(self, event):
        self.txtA.SetLabel("버튼3")
        
    def OnHandler(self, event):
        #print(event.GetEventObject().id)
        if event.GetEventObject().id == 1:
            self.txtA.SetLabelText("1")
        elif event.GetEventObject().id == 2:
            self.txtA.SetLabelText("2")
        else:
            self.Close() # Frame 닫기
        
if __name__ == '__main__':
    app = wx.App()
    Ex(None, '연습용')
    app.MainLoop()
        
    