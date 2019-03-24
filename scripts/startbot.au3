Sleep(1000)

$hWnd = WinGetHandle("C:\Windows\py.exe")
WinSetState($hwnd, "", @SW_MINIMIZE)

$hWnd2 = WinGetHandle("C:\Windows\system32\cmd.exe")
WinSetState($hwnd2, "", @SW_MINIMIZE)