; File gets list of current tab controls
#include <WinAPISysWin.au3>

$window = WinGetHandle('WatchMe')
$array=_WinAPI_EnumChildWindows($window,True)
Local $newarray[0][4]
$currindex = 0
Local $maxlen[4]
$maxlen[0] = 0
$maxlen[1] = 0
$maxlen[2] = 0
$maxlen[3] = 0

For $i = 1 to UBound($array) -1
	$text=_WinAPI_GetWindowText($array[$i][0])
	if not ($text = "") and not ($text = "Reset") and not ($text = "Start") and not ($text = "Stop") and not ($text = "menu") Then
		if (StringInStr($array[$i][1],"WindowsForms10.EDIT")) then
			ReDim $newarray[UBound($newarray) + 1][4]
			Local $len[4]

			; [Text] | [Reset] | [Start/Stop] | [Status]
			$reset = $array[$i+1][0]
			$startstop = $array[$i+2][0]
			$status = _WinAPI_GetWindowText($array[$i+2][0])

			; Since the status is the reverse of what is going on
			if $status="Start" Then
				$status = "Stopped"
			elseif $status="Stop" Then
				$status = "Started"
			endif

			$len[0] = StringLen($text)
			$len[1] = StringLen($reset)
			$len[2] = StringLen($startstop)
			$len[3] = StringLen($status)

			if $len[0] > $maxlen[0] Then
				$maxlen[0] = $len[0]
			endif
			if $len[1] > $maxlen[1] Then
				$maxlen[1] = $len[1]
			endif
			if $len[2] > $maxlen[2] Then
				$maxlen[2] = $len[2]
			endif
			if $len[3] > $maxlen[3] Then
				$maxlen[3] = $len[3]
			endif

			$newarray[$currindex][0] = $text
			$newarray[$currindex][1] = $reset
			$newarray[$currindex][2] = $startstop
			$newarray[$currindex][3] = $status

			$currindex=$currindex+1
		endif
	endif
Next

For $i = 0 to UBound($newarray)-1

	$string1=StringFormat("%-"&$maxlen[0]&"s",$newarray[$i][0])
	$string2=StringFormat("%-"&$maxlen[1]&"s",$newarray[$i][1])
	$string3=StringFormat("%-"&$maxlen[2]&"s",$newarray[$i][2])
	$string4=StringFormat("%-"&$maxlen[3]&"s",$newarray[$i][3])
	ConsoleWrite($string1 & " | " & $string2 & " | " & $string3 & " | " & $string4 & @CRLF)

Next



; add StringFormat("%10s", $s)
