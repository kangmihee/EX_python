
import wx
import wx.xrc
class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"간단계산기", pos = wx.DefaultPosition, size = wx.Size( 320,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt1 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"숫자1 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt1.Wrap( -1 )
        bSizer9.Add( self.txt1, 0, wx.ALL, 5 )
        
        self.inputnum1 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.inputnum1, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer9 )
        self.m_panel4.Layout()
        bSizer9.Fit( self.m_panel4 )
        bSizer5.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt2 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"숫자2 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt2.Wrap( -1 )
        bSizer10.Add( self.txt2, 0, wx.ALL, 5 )
        
        self.inputnum2 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.inputnum2, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer10 )
        self.m_panel5.Layout()
        bSizer10.Fit( self.m_panel5 )
        bSizer5.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"연산자 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer11.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.operator = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.operator, 0, wx.ALL, 5 )
        
        
        self.m_panel6.SetSizer( bSizer11 )
        self.m_panel6.Layout()
        bSizer11.Fit( self.m_panel6 )
        bSizer5.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt3 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"연산결과 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt3.Wrap( -1 )
        bSizer12.Add( self.txt3, 0, wx.ALL, 5 )
        
        self.result = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.result, 0, wx.ALL, 5 )
        
        
        self.m_panel7.SetSizer( bSizer12 )
        self.m_panel7.Layout()
        bSizer12.Fit( self.m_panel7 )
        bSizer5.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.button1 = wx.Button( self.m_panel8, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.button1, 0, wx.ALL, 5 )
        
        self.button2 = wx.Button( self.m_panel8, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.button2, 0, wx.ALL, 5 )
        
        self.button3 = wx.Button( self.m_panel8, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.button3, 0, wx.ALL, 5 )
        
        
        self.m_panel8.SetSizer( bSizer13 )
        self.m_panel8.Layout()
        bSizer13.Fit( self.m_panel8 )
        bSizer5.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.button1.Bind( wx.EVT_BUTTON, self.OnClick1 )
        self.button2.Bind( wx.EVT_BUTTON, self.OnClick2 )
        self.button3.Bind( wx.EVT_BUTTON, self.OnClick3 )
    
    def __del__( self ):
        pass
    
    
    def OnClick1( self, event ):
        event.Skip()
        inputnum1 = self.inputnum1.GetValue()
        inputnum2 = self.inputnum2.GetValue()
        operator = self.operator.GetValue()
        
        if inputnum1=='' or inputnum2=='' or operator == '':
            wx.MessageBox('모든값을 입력해주세요.','알림',wx.OK)
            return
        elif inputnum2 == '0' and operator == '/':
            wx.MessageBox('숫자 0으로는 나눌수 없습니다.','알림',wx.OK)
            return
          
        elif operator == '+' :
            result = int(inputnum1) + int(inputnum2)
            # result = eval(inputnum1 + operator + inputnum2) # eval함수 사용하면 따로 형변환필요 x
        elif operator == '-': 
            result = int(inputnum1) - int(inputnum2)
        elif operator == '*': 
            result = int(inputnum1) * int(inputnum2)       
        elif operator == '/': 
            result = int(inputnum1) / int(inputnum2)
            
        self.result.SetLabel(str(result))
                 
    def OnClick2( self, event ):
        event.Skip()
        self.inputnum1.SetValue(' ')
        self.inputnum2.SetValue(' ')
        self.operator.SetValue(' ')
        self.result.SetValue(' ')
            
    def OnClick3( self, event ):
        event.Skip()
        dlg = wx.MessageDialog(self, '정말 종료 하실건가요?', '알림', wx.YES_NO)
        imsi = dlg.ShowModal()
        if imsi == wx.ID_YES:
            dlg.Destroy()
            self.Close()
  
if __name__ == '__main__':
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()
