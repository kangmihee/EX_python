
import wx
import wx.xrc
import MySQLdb
import re

config = {
    'host':'127.0.0.1',   # dict type
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}



class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"회원 로그인", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"사번 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer6.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txt1 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txt1, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"직원명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txt2 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txt2, 0, wx.ALL, 5 )
        
        self.btnLogin = wx.Button( self.m_panel3, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btnLogin, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer6 )
        self.m_panel3.Layout()
        bSizer6.Fit( self.m_panel3 )
        bSizer5.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt3 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt3.Wrap( -1 )
        bSizer3.Add( self.txt3, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel4.SetSizer( bSizer3 )
        self.m_panel4.Layout()
        bSizer3.Fit( self.m_panel4 )
        bSizer5.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.txt4 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer4.Add( self.txt4, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel5.SetSizer( bSizer4 )
        self.m_panel5.Layout()
        bSizer4.Fit( self.m_panel5 )
        bSizer5.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel41 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer51.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.txt5 = wx.TextCtrl( self.m_panel41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.txt5, 0, wx.ALL, 5 )
        
        self.m_staticText6 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer51.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        
        self.m_panel41.SetSizer( bSizer51 )
        self.m_panel41.Layout()
        bSizer51.Fit( self.m_panel41 )
        bSizer5.Add( self.m_panel41, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnLogin.Bind( wx.EVT_BUTTON, self.OnClick )
    
    def __del__( self ):
        pass
     
    # Virtual event handlers, overide them in your derived class
    def OnClick( self, event ):
        
        txt1 = self.txt1.GetValue()
        txt2 = self.txt2.GetValue()
        try:           
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select gogek_no, gogek_name, gogek_tel, gogek_jumin from \
            gogek inner join jikwon on gogek.gogek_damsano = jikwon.jikwon_no where \
            jikwon.jikwon_no=%s and jikwon.jikwon_name=%s"
            
            cursor.execute(sql, (txt1, txt2))            
            self.txt4.SetValue('')       
            self.txt5.SetValue('')      
            
            if len(txt2) >= 2 and re.match('[가-힣]', txt2) and len(txt1) <= 2:
                a = 0
                for (gogek_no, gogek_name, gogek_tel, gogek_jumin) in cursor:
                    if gogek_jumin[7] == '1':
                        gen = '남자'
                    elif gogek_jumin[7] == '2':
                        gen = '여자'
                    self.txt3.SetLabel(txt1 + '번  ' +txt2 + '의   관리고객') # t:tab
                    self.txt4.AppendText(' {}\t{}\t{}\t{}\n'.format(gogek_no, gogek_name, gogek_tel, gen)) # t:tab               
                    a += 1
                    
                self.txt5.AppendText(str(a)) 
                    
            else:
                wx.MessageBox('내용을 바르게 입력해주세요, 직원명은 한글만 가능!', '에러', wx.OK|wx.ICON_ERROR)
                self.txt1.SetFocus() 
            
        except Exception as e:
            print('err : ', e)
            
        finally:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()

    

