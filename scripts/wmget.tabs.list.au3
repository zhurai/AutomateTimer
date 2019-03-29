; File gets list of current tabs
#include <WinAPISysWin.au3>

$windowname = "WatchMe"
$window = WinGetHandle($windowname)
$array=_WinAPI_EnumChildWindows($window,False)

For $i = 1 to UBound($array) -1
	$text=_WinAPI_GetWindowText($array[$i][0])
	if not ($text = "") and not ($text = "Reset") and not ($text = "Start") and not ($text = "Stop") and not ($text = "menu") Then
		if not (StringInStr($text,"-")) and not (StringInStr($text,":")) and (StringInStr($array[$i][1],"WindowsForms10.Window.8")) then
			ConsoleWrite($text & @CRLF)
		endif
	endif
Next
