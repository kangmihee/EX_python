
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

class MyForm ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"직급별 자료보기", pos = wx.DefaultPosition, size = wx.Size( 419,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직급 입력: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtjik = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtjik, 0, wx.ALL, 5 )
        
        self.btnOk = wx.Button( self.m_panel1, wx.ID_ANY, u"검색", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btnOk, 0, wx.ALL, 5 )
        
        self.btnExit = wx.Button( self.m_panel1, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btnExit, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer3 )
        self.m_panel1.Layout()
        bSizer3.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.txtList = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer4.Add( self.txtList, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.txtList.SetEditable(False)
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.OnjikSearch )
        self.btnExit.Bind( wx.EVT_BUTTON, self.OnClose )
        
        self.DbLoad()
    
    def __del__( self ):
        pass
      
      
    def DbLoad(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select jikwon_no, jikwon_name, jikwon_pay from jikwon"
            cursor.execute(sql)            
            for(no, name, pay) in cursor:
                self.txtList.AppendText(' {}\t{}\t{}\n'.format(no, name, pay)) # t:tab
                                   
        except Exception as e:
            print('err : ', e)
            
        finally:
            cursor.close()
            conn.close()
    
    
    # Virtual event handlers, overide them in your derived class
    def OnjikSearch( self, event ):
        jik = self.txtjik.GetValue()        
        if len(jik) >= 2 and re.match('[가-힇]', jik):
            #self.txtList.SetValue(jik)
            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()
                sql = ("select jikwon_no, jikwon_name, jikwon_pay from jikwon\
                        where jikwon_jik like '{0}%'".format(jik))
                cursor.execute(sql)
                self.txtList.SetValue('')
                
                for(no, name, pay) in cursor:
                    self.txtList.AppendText(' {}\t{}\t{}\n'.format(no, name, pay)) # t:tab
                           
            except Exception as e:
                print('OnJikSearch er : ', e)
                
            finally:
                cursor.close()
                conn.close()
                        
        else:
            wx.MessageBox('직급은 두 자 이상, 한글만 가능!', '에러', wx.OK|wx.ICON_ERROR)
            self.txtjik.SetFocus()
           
    
    def OnClose( self, event ):
        dlg = wx.MessageDialog(self, '정말 종료 하실건가요?', '알림', wx.YES_NO)
        imsi = dlg.ShowModal()
        if imsi == wx.ID_YES:
            dlg.Destroy()
            self.Close()
 
                
if __name__ == '__main__':
    app = wx.App()
    MyForm(None).Show()
    app.MainLoop()

    

