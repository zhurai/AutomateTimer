; ConsoleWrite("TESTING!" & @CRLF)
; ConsoleWrite("TESTING!2" & @CRLF)
; ConsoleWrite("TESTING!3" & @CRLF)

ControlClick("WatchMe","","[NAME:tabControl]")
Local $Tab=ControlCommand("WatchMe","","[NAME:tabControl]","CurrentTab","")
ConsoleWrite($Tab)
