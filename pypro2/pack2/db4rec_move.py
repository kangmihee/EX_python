# 레코드 이동
import wx
import wx.xrc
import MySQLdb

config = {
    'host':'127.0.0.1',   # dict type
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

rec_r = 0
datas = []

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"레코드 이동", pos = wx.DefaultPosition, size = wx.Size( 265,170 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL)
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"사번 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.lblSabun = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblSabun.Wrap( -1 )
        bSizer2.Add( self.lblSabun, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.lblIrum = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.lblIrum.Wrap( -1 )
        bSizer2.Add( self.lblIrum, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel2, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel2, wx.ID_ANY, u"<", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel2, wx.ID_ANY, u">", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel2, wx.ID_ANY, u">||", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4
        
        self.btn1.Bind( wx.EVT_BUTTON, self.OnClick )
        self.btn2.Bind( wx.EVT_BUTTON, self.OnClick )
        self.btn3.Bind( wx.EVT_BUTTON, self.OnClick )
        self.btn4.Bind( wx.EVT_BUTTON, self.OnClick )
        
        self.DbLoad()
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnClick( self, event ):
        id = event.GetEventObject().id
        global rec_r
        
        if id == 1:
            rec_r = 0
        elif id == 2:
            rec_r = rec_r - 1
            if rec_r < 0: 
                rec_r = 0
                return
        elif id == 3:
            rec_r = rec_r + 1
            if rec_r > (len(datas) - 1): 
                rec_r = len(datas) - 1
                return
        elif id == 4:
            rec_r = len(datas) - 1
            
        self.ShowData(rec_r)
        
    
    def DbLoad(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select jikwon_no, jikwon_name from jikwon"
            cursor.execute(sql)      
            
            global datas
            datas = cursor.fetchall()
            
            self.ShowData(rec_r)
                           
        except Exception as e:
            print('DbLoad err : ', e)
            
        finally:
            cursor.close()
            conn.close()
            
    def ShowData(self, r):
        self.lblSabun.SetLabel(str(datas[r][0]))
        self.lblIrum.SetLabel(str(datas[r][1]))


if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()