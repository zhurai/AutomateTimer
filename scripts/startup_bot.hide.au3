Sleep(1000)

$hWnd = WinGetHandle("C:\Windows\py.exe")
WinMove($hWnd,"",600,0,780,341)
WinSetState($hWnd, "", @SW_MINIMIZE)

$hWnd2 = WinGetHandle("C:\Windows\system32\cmd.exe")
WinMove($hWnd2,"",600,0,780,341)
WinSetState($hWnd2, "", @SW_MINIMIZE)

$hWnd3 = WinGetHandle("Command Prompt")
WinMove($hWnd3,"",600,0,780,341)
WinSetState($hWnd3, "", @SW_MINIMIZE)

WinActivate("WatchMe")
