
import wx
import wx.xrc
import MySQLdb
import re
from astropy.units.cds import enable

config = {
    'host':'127.0.0.1',   # dict type
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}


class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CRUD Text", pos = wx.DefaultPosition, size = wx.Size( 307,384 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"번호 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtNo, 0, wx.ALL, 5 )
        
        self.btnInsert = wx.Button( self.m_panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnInsert, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnUpdate = wx.Button( self.m_panel2, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btnUpdate, 0, wx.ALL, 5 )
        
        self.btnConfirm = wx.Button( self.m_panel2, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btnConfirm, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"전화 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txtTel = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtTel, 0, wx.ALL, 5 )
        
        self.btnDel = wx.Button( self.m_panel3, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btnDel, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstMem = wx.ListCtrl( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer5.Add( self.lstMem, 1, wx.ALL|wx.EXPAND, 5 )
               
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 0, wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.staCnt = wx.StaticText( self.m_panel5, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCnt.Wrap( -1 )
        bSizer6.Add( self.staCnt, 0, wx.ALL, 5 )
                
        self.m_panel5.SetSizer( bSizer6 )
        self.m_panel5.Layout()
        bSizer6.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )
                
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
               
        # Connect Events
        self.btnInsert.id = 1
        self.btnUpdate.id = 2
        self.btnConfirm.id = 3
        self.btnDel.id = 4
        
        self.btnInsert.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        self.btnUpdate.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        self.btnConfirm.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        self.btnDel.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        
        self.btnConfirm.Enable(enable=False)
        
        # lstMen에 제목 부여
        self.lstMem.InsertColumn(0, '번호', width=50)
        self.lstMem.InsertColumn(1, '이름', width=50)
        self.lstMem.InsertColumn(2, '전화', width=50)
        
        self.ViewListData()

    
    def __del__( self ):
        pass
        
    def ViewListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from pymem"
            cursor.execute(sql)
            self.lstMem.DeleteAllItems() # 전체데이터 초기화
            count = 0
            for data in cursor:
                i = self.lstMem.InsertItem(10000, 0)
                self.lstMem.SetItem(i, 0, str(data[0]))
                self.lstMem.SetItem(i, 1, data[1])
                self.lstMem.SetItem(i, 2, data[2])
                count += 1
            self.staCnt.SetLabelText(str(count))

        except Exception as e:
            #print('ViewListData err : ', e)
            wx.MessageBox('읽기오류 : ', str(e)  )
            
        finally:
            cursor.close()
            conn.close()
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnClick( self, event ):
        id = event.GetEventObject().id
        if id == 1:
            self.MemInsert()
        elif id == 2:
            self.MemUpdate()       # 수정 준비
        elif id == 3:
            self.MemUpdateOk()     # 수정 처리
        elif id == 4:
            self.MemDelete()
        elif id == 5:
            self.MemUpdateCancel() # 수정 취소
        
    def MemInsert(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if no == '' or name == '' or tel == '' :
            wx.MessageBox('자료를 입력하시오', '입력', wx.OK)
            return
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            data = self.SelectData(no);
            if data != None:
                wx.MessageBox('이미 사용중인 번호입니다', '알림', wx.OK)
                self.txtNo.SetFocus()
                return
            
            # 등록작업 계속
            sql = "insert into pymem values(%s,%s,%s)"  
            cursor.execute(sql, (no, name, tel))
            conn.commit()
            
            self.ViewListData() # 등록 후 목록보기
            self.txtNo.SetValue('')
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
             
        except Exception as e:
            print('MemInsert err : ', str(e))
            conn.rollback()
            
        finally:
            cursor.close()
            conn.close()                
    
    def MemUpdate(self):
        dlg = wx.TextEntryDialog(None, '수정 할 번호 입력', '수정')
        if dlg.ShowModal() == wx.ID_OK :
            if dlg.GetValue == '' : return
            upno = dlg.GetValue()
            #print(upno)
            data = self.SelectData(upno)
            if data ==  None:
                wx.MessageBox(upno + '번은 동록된 자료가 아닙니다.', '알림', wx.OK)
                return
            
            # 수정 준비 계속
            self.txtNo.SetValue(str(data[0]))
            self.txtName.SetValue(str(data[1]))
            self.txtTel.SetValue(str(data[2]))
            
            self.txtNo.SetEditable(False) # pk라서 수정 불가로 설정해주기
            self.btnConfirm.Enable(True)
            self.btnUpdate.SetLabel("취소")
            self.btnUpdate.id = 5
                       
        else:
            return
        
        dlg.Destroy()
        
    
    def MemUpdateOk(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if name == '' or tel == '' :
            wx.MessageBox('자료를 입력하시오', '입력', wx.OK)
            return
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
                      
            # 수정작업 계속
            sql = "update pymem set irum = %s, junwha = %s where bun = %s"  
            cursor.execute(sql, (name, tel, no))
            conn.commit()
            
            self.ViewListData() # 수정 후 목록보기
            self.txtNo.SetValue('')
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            
            self.txtNo.SetEditable(True)
            self.btnUpdate.SetLabel("수정")
            self.btnUpdate.id = 2
            self.btnConfirm.Enabled(False)
            
        except Exception as e:
            print('MemUpdateOk err : ', str(e))
            conn.rollback()
            
        finally:
            cursor.close()
            conn.close()
    
    def MemDelete(self):
        dlg = wx.TextEntryDialog(None, '삭제 할 번호 입력', '삭제')
        if dlg.ShowModal() == wx.ID_OK :
            if dlg.GetValue == '' : return
            delno = dlg.GetValue()
            data = self.SelectData(delno)
            if data ==  None:
                wx.MessageBox(delno + '번은 동록된 자료가 아닙니다.', '알림', wx.OK)
                return
            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()
                sql = "delete from pymem where bun=%s"  
                cursor.execute(sql, (delno,))
                conn.commit()
                
                self.ViewListData() # 삭제 후 목록보기
                self.txtNo.SetValue('')
                self.txtName.SetValue('')
                self.txtTel.SetValue('')
             
            except Exception as e:
                print('MemInsert err : ', str(e))
                conn.rollback()
                
            finally:
                cursor.close()
                conn.close()            
                       
        else:
            return
        
        dlg.Destroy()
    
    def MemUpdateCancel(self):
        self.txtNo.SetEditable(True)
        self.btnUpdate.SetLabel("취소")
        self.btnUpdate.id = 2
        self.btnConfirm.Enable(False)
        self.txtNo.SetValue('')
        self.txtName.SetValue('')
        self.txtTel.SetValue('')
    
    def SelectData(self, no):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from pymem where bun={}".format(no)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
                      
        except Exception as e:
            print('SelectData err : ', str(e))
            
        finally:
            cursor.close()
            conn.close()
        
   
if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()

    

