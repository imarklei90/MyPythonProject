#-*- encoding:utf-8 -*-
import wx

if __name__ == '__main__':
    app = wx.App()
    win = wx.Frame(None,title = 'Simple Editor',size=(410,335)) #使用父部件的构造函数的第一个参数创建
    win.Show()

    openButton = wx.Button(win,label = 'Open',pos = (225,5),size = (80,25)) #使用父部件win创建

    saveButton = wx.Button(win,label = 'Save',pos = (315,5),size = (80,25))

    fileName = wx.TextCtrl(win,pos = (5,5),size = (210,25))

    contents = wx.TextCtrl(win,pos = (5,35),size = (390,260),style = wx.TE_MULTILINE | wx.HSCROLL)

    app.MainLoop()
