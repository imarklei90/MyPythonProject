# -*- encoding:utf-8 -*-

import wx

app = wx.App()
win = wx.Frame(None, title = 'Simple Editor', size = (410,335))
bkg = wx.Panel(win) # 添加背景组件

loadButton = wx.Button(bkg, label = 'Open')
saveButton = wx.Button(bkg, label = 'Save')
fileName = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style = wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer() # 创建尺寸器
hbox.Add(fileName, proportion = 1, flag = wx.EXPAND)
hbox.Add(loadButton, proportion = 0, flag = wx.LEFT, border = 5)
hbox.Add(saveButton, proportion = 0, flag = wx.LEFT, border = 5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
vbox.Add(hbox, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

bkg.setSizer(vbox)

win.Show()

app.MainLoop()
