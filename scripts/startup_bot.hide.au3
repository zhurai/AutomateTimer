Sleep(1000)

$hWnd = WinGetHandle("C:\Windows\py.exe")
WinMove($hWnd,"",598,0)
WinSetState($hWnd, "", @SW_MINIMIZE)

$hWnd2 = WinGetHandle("C:\Windows\system32\cmd.exe")
WinMove($hWnd2,"",598,0)
WinSetState($hWnd2, "", @SW_MINIMIZE)

$hWnd3 = WinGetHandle("Command Prompt")
WinMove($hWnd3,"",598,0)
WinSetState($hWnd3, "", @SW_MINIMIZE)

WinActivate("WatchMe")
