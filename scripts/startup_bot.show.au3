Sleep(1000)

$hWnd = WinGetHandle("C:\Windows\py.exe")
WinMove($hWnd,"",600,0,780,341)

$hWnd2 = WinGetHandle("C:\Windows\system32\cmd.exe")
WinMove($hWnd2,"",600,0,780,341)

$hWnd3 = WinGetHandle("Command Prompt")
WinMove($hWnd3,"",600,0,780,341)

WinActivate("WatchMe")
