#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Change2CUI=y
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
; ConsoleWrite("TESTING!" & @CRLF)
; ConsoleWrite("TESTING!2" & @CRLF)
; ConsoleWrite("TESTING!3" & @CRLF)

ControlClick("WatchMe","","[NAME:tabControl]")
Local $Tab=ControlCommand("WatchMe","","[NAME:tabControl]","CurrentTab","")
ConsoleWrite($Tab & @CRLF)
