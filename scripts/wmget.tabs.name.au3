; File gets the current tab name

#include <StringConstants.au3>

$windowname = "WatchMe"

$text = WinGetText($windowname)
$text2 = StringStripWS($text, $STR_STRIPLEADING + $STR_STRIPTRAILING + $STR_STRIPSPACES)
$array = StringRegExp($text2,"(\N*)",$STR_REGEXPARRAYMATCH)

ConsoleWrite($array[0] & @CRLF)










