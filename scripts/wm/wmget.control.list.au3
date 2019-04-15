; File gets list of current tab controls
#include <WinAPISysWin.au3>
#include <Array.au3>
#include <WinAPI.au3>

Func GetAllWindowsControls($hCallersWindow,  $bOnlyVisible=Default, $type=Default,$sStringIncludes=Default,$getlength=Default)
	Local $array[0]
	Local $currcount=0
	Local $statictype=0

    If Not IsHWnd($hCallersWindow) Then
        ConsoleWrite("$hCallersWindow must be a handle...provided=[" & $hCallersWindow & "]" & @CRLF)
        Return False
    EndIf
    ; Get all list of controls
    If $bOnlyVisible = Default Then $bOnlyVisible = False
    If $sStringIncludes = Default Then $sStringIncludes = ""
	If $type = Default Then $type =""
	If $getlength = Default Then $getlength=False

	$sClassList = WinGetClassList($hCallersWindow)

	if $type="STATIC" Then
		$statictype = 0
	elseif $type="STATIC2" Then
		$statictype=1
		$type="STATIC"
	endif

    ; Create array
    $aClassList = StringSplit($sClassList, @CRLF, 2)

    ; Sort array
    _ArraySort($aClassList)
    ;_ArrayDelete($aClassList, 0)

    ; Loop
    $iCurrentClass = ""
    $iCurrentCount = 1
    $iTotalCounter = 1


    For $i = 0 To UBound($aClassList) - 1
        If $aClassList[$i] = $iCurrentClass Then
            $iCurrentCount += 1
        Else
            $iCurrentClass = $aClassList[$i]
            $iCurrentCount = 1
        EndIf

        $hControl = ControlGetHandle($hCallersWindow, "", "[CLASSNN:" & $iCurrentClass & $iCurrentCount & "]")
        $text = StringRegExpReplace(ControlGetText($hCallersWindow, "", $hControl), "[\n\r]", "{@CRLF}")
        $aPos = ControlGetPos($hCallersWindow, "", $hControl)
        $sControlID = _WinAPI_GetDlgCtrlID($hControl)
        $bIsVisible = ControlCommand($hCallersWindow, "", $hControl, "IsVisible")
        If $bOnlyVisible And Not $bIsVisible Then
            $iTotalCounter += 1
            ContinueLoop
        EndIf

        ;If StringLen($sStringIncludes) > 0 Then
		;If Not StringInStr($text, $sStringIncludes) Then
        ;        $iTotalCounter += 1
        ;        ContinueLoop
        ;    EndIf
        ;EndIf

		if $type="" Then
			; show all
			ReDim $array[UBound($array) + 1]
			$array[$currcount] = $text
			$currcount=$currcount+1
		Else
			if StringInStr(StringFormat("%19s", $iCurrentClass & $iCurrentCount),$type) Then
				if $type="BUTTON" Then
					if $sStringIncludes="Reset" Then
						if StringInStr($text, $sStringIncludes) Then
							ReDim $array[UBound($array) + 1]
							$array[$currcount] = StringFormat("%10s", $hControl)
							$currcount=$currcount+1
						endif
					endif
					if $sStringIncludes="Start" or $sStringIncludes="Stop" Then
						if StringInStr($text, "Start") or StringInStr($text, "Stop") Then
							ReDim $array[UBound($array) + 1]
							$array[$currcount] = StringFormat("%10s", $hControl)
							$currcount=$currcount+1
						endif
					endif

				elseif $type="EDIT" Then
					if $getlength=True Then
						ReDim $array[UBound($array) + 1]
						$array[$currcount] = StringFormat("%4s", $aPos[1])
						$currcount=$currcount+1
					else
						ReDim $array[UBound($array) + 1]
						;ConsoleWrite("Func=[GetAllWindowsControls]: ControlCounter=[" & StringFormat("%3s", $iTotalCounter) & "] ControlID=[" & StringFormat("%5s", $sControlID) & "] Handle=[" & StringFormat("%10s", $hControl) & "] ClassNN=[" & StringFormat("%19s", $iCurrentClass & $iCurrentCount) & "] XPos=[" & StringFormat("%4s", $aPos[0]) & "] YPos=[" & StringFormat("%4s", $aPos[1]) & "] Width=[" & StringFormat("%4s", $aPos[2]) & "] Height=[" & StringFormat("%4s", $aPos[3]) & "] IsVisible=[" & $bIsVisible & "] Text=[" & $text & "]." & @CRLF)
						$array[$currcount] = $text
						$currcount=$currcount+1
					endif
				elseif $statictype=0 Then
					if StringInStr(StringFormat("%19s", $iCurrentClass & $iCurrentCount),$type) Then
						ReDim $array[UBound($array) + 1]
						$array[$currcount] = $text
						$currcount=$currcount+1
					EndIf
				; STATIC2 = STATIC but grab handle
				elseif $statictype=1 Then
					if StringInStr(StringFormat("%19s", $iCurrentClass & $iCurrentCount),"STATIC") Then
						ReDim $array[UBound($array) + 1]
						$array[$currcount] = StringFormat("%10s", $hControl)
						$currcount=$currcount+1
					EndIf
				EndIf
			Endif
		EndIf

        If Not WinExists($hCallersWindow) Then ExitLoop
        $iTotalCounter += 1
    Next
	Return $array
EndFunc   ;==>GetAllWindowsControls


$window = WinGetHandle('WatchMe')
Local $maxlen[5]
Local $skip[0]
$maxlen[0] = 0
$maxlen[1] = 0
$maxlen[2] = 0
$maxlen[3] = 0
$maxlen[4] = 0
$array1=GetAllWindowsControls($window,True,"EDIT")
$array2=GetAllWindowsControls($window,True,"BUTTON","Reset")
$array3=GetAllWindowsControls($window,True,"BUTTON","Start")
$array5=GetAllWindowsControls($window,True,"STATIC")
Local $array4[0]
$order=GetAllWindowsControls($window,True,"EDIT",Default,True)

For $i = 0 to UBound($array3) -1
	ReDim $array4[UBound($array4) + 1]
	$text=ControlGetText($window,"",HWnd($array3[$i]))
	if $text="Stop" Then
		$array4[$i]="Started"
	Elseif $text="Start" Then
		$array4[$i]="Stopped"
	EndIf
Next


; here change the ordering

$highest = 0
For $j = 0 to Ubound($order) -1
	for $i=0 to Ubound($order)-2
		if $order[$i] > $order[$i+1] Then
			$tempo=$order[$i+1]
			$order[$i+1] = $order[$i]
			$order[$i]=$tempo

			$temp1=$array1[$i+1]
			$temp2=$array2[$i+1]
			$temp3=$array3[$i+1]
			$temp4=$array4[$i+1]
			$temp5=$array5[$i+1]

			$array1[$i+1] = $array1[$i]
			$array2[$i+1] = $array2[$i]
			$array3[$i+1] = $array3[$i]
			$array4[$i+1] = $array4[$i]
			$array5[$i+1] = $array5[$i]

			$array1[$i]=$temp1
			$array2[$i]=$temp2
			$array3[$i]=$temp3
			$array4[$i]=$temp4
			$array5[$i]=$temp5
		endif
	Next
Next

_ArrayInsert($array1,0,"Name of Task")
_ArrayInsert($array2,0,"Reset")
_ArrayInsert($array3,0,"Start/Stop")
_ArrayInsert($array4,0,"Status")
_ArrayInsert($array5,0,"Time Left")

For $i = 0 to UBound($array1) -1

if StringLen($array1[$i]) > $maxlen[0] Then
		$maxlen[0]=StringLen($array1[$i])
	Endif


Next
For $i = 0 to UBound($array2) -1
	if StringLen($array2[$i]) > $maxlen[1] Then
		$maxlen[1]=StringLen($array2[$i])
	Endif
Next
For $i = 0 to UBound($array3) -1
	if StringLen($array3[$i]) > $maxlen[2] Then
		$maxlen[2]=StringLen($array3[$i])
	Endif
Next
For $i = 0 to UBound($array4) -1
	if StringLen($array4[$i]) > $maxlen[3] Then
		$maxlen[3]=StringLen($array4[$i])
	Endif
Next
For $i = 0 to UBound($array5) -1
	if StringLen($array5[$i]) > $maxlen[4] Then
		$maxlen[4]=StringLen($array5[$i])
	Endif
Next


Global $newarray[UBound($array1)][5]
For $i = 0 to UBound($array1) - 1
    $newarray[$i][0] = $array1[$i]
    $newarray[$i][1] = $array2[$i]
    $newarray[$i][2] = $array3[$i]
    $newarray[$i][3] = $array4[$i]
    $newarray[$i][4] = $array5[$i]
Next


For $i = 0 to UBound($newarray)-1

	$string1=StringFormat("%-"&$maxlen[0]&"s",$newarray[$i][0])
	$string2=StringFormat("%-"&$maxlen[1]&"s",$newarray[$i][1])
	$string3=StringFormat("%-"&$maxlen[2]&"s",$newarray[$i][2])
	$string4=StringFormat("%-"&$maxlen[3]&"s",$newarray[$i][3])
	$string5=StringFormat("%-"&$maxlen[4]&"s",$newarray[$i][4])
	ConsoleWrite($string1 & " | " & $string2 & " | " & $string3 & " | " & $string4 & " | " & $string5 & @CRLF)

Next
