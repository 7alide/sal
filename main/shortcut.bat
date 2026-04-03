@echo off
set "targetDir=%~dp0"
set "targetPath=%targetDir%sal.bat"
set "shortcutPath=%userprofile%\Desktop\SAL.lnk"
set "iconPath=%targetDir%icon.ico"

echo set WshShell = WScript.CreateObject("WScript.Shell") > "%temp%\MakeShortcut.vbs"
echo set oShellLink = WshShell.CreateShortcut("%shortcutPath%") >> "%temp%\MakeShortcut.vbs"
echo oShellLink.TargetPath = "%targetPath%" >> "%temp%\MakeShortcut.vbs"
echo oShellLink.WorkingDirectory = "%targetDir%" >> "%temp%\MakeShortcut.vbs"
echo oShellLink.WindowStyle = 1 >> "%temp%\MakeShortcut.vbs"
echo oShellLink.IconLocation = "%iconPath%" >> "%temp%\MakeShortcut.vbs"
echo oShellLink.Description = "7alide SAL for Windows" >> "%temp%\MakeShortcut.vbs"
echo oShellLink.Save >> "%temp%\MakeShortcut.vbs"

cscript /nologo "%temp%\MakeShortcut.vbs"
del "%temp%\MakeShortcut.vbs"

echo Success!