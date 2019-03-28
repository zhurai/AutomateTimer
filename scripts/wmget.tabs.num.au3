; File gets the current tab index number
; (Number starts at 1)

$windowname = "WatchMe"

Local $Tab = ControlCommand("WatchMe","","[NAME:tabControl]","CurrentTab","")
ConsoleWrite($Tab & @CRLF)
