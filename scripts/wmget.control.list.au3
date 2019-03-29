; File gets list of current tab controls
#include <WinAPISysWin.au3>

$window = WinGetHandle('WatchMe')
$array=_WinAPI_EnumChildWindows($window,True)

For $i = 1 to UBound($array) -1
	$text=_WinAPI_GetWindowText($array[$i][0])
	if not ($text = "") and not ($text = "Reset") and not ($text = "Start") and not ($text = "Stop") and not ($text = "menu") Then
		if not (StringInStr($text,":")) and (StringInStr($array[$i][1],"WindowsForms10.EDIT")) then
			; [Text] | [Reset] | [Start/Stop]
			$reset = $array[$i+1][0]
			$startstop = $array[$i+2][0]
			$status = _WinAPI_GetWindowText($array[$i+2][0])

			; Since the status is the reverse of what is going on
			if $status="Start" Then
				$status = "Stopped"
			elseif $status="Stop" Then
				$status = "Started"
			endif

			ConsoleWrite($text & " | " & $reset & " | " & $startstop & " | " & $status & @CRLF)
		endif
	endif
Next
