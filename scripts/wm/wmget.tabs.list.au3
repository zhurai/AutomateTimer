; File gets list of current tabs
#include <WinAPISysWin.au3>

$windowname = "WatchMe"
$window = WinGetHandle($windowname)
$array=_WinAPI_EnumChildWindows($window,False)
Local $newarray[0][2]
Local $header[2]
$currindex = 0
Local $maxlen[2]
$maxlen[0] = 0
$maxlen[1] = 0

For $i = 1 to UBound($array) -1
	$text=_WinAPI_GetWindowText($array[$i][0])
	if not ($text = "") and not ($text = "Reset") and not ($text = "Start") and not ($text = "Stop") and not ($text = "menu") Then
		if not (StringInStr($text,"-")) and not (StringInStr($text,":")) and (StringInStr($array[$i][1],"WindowsForms10.Window.8")) then
			ReDim $newarray[UBound($newarray) + 1][2]
			Local $len[2]

			$newarray[$currindex][0] = $currindex+1
			$newarray[$currindex][1] = $text

			$len[0] = StringLen($currindex+1)
			$len[1] = StringLen($text)

			if $len[0] > $maxlen[0] Then
				$maxlen[0] = $len[0]
			endif
			if $len[1] > $maxlen[1] Then
				$maxlen[1] = $len[1]
			endif

			$currindex=$currindex+1
		endif
	endif
Next

$header[0] = "Tab ID"
$header[1] = "Tab Name"

if StringLen($header[0]) > $maxlen[0] Then
	$maxlen[0] = StringLen($header[0])
endif
if StringLen($header[1]) > $maxlen[1] Then
	$maxlen[1] = StringLen($header[1])
endif

$header1=StringFormat("%-"&$maxlen[0]&"s",$header[0])
$header2=StringFormat("%-"&$maxlen[1]&"s",$header[1])

ConsoleWrite($header1 & " | " & $header2 & @CRLF)

For $i = 0 to UBound($newarray)-1

	$string1=StringFormat("%-"&$maxlen[0]&"s",$newarray[$i][0])
	$string2=StringFormat("%-"&$maxlen[1]&"s",$newarray[$i][1])
	ConsoleWrite($string1 & " | " & $string2 & @CRLF)

Next
