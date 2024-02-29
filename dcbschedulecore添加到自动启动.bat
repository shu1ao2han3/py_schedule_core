@echo off

echo 实际上.exe的路径
set PATH_TO_EXE=C:\Users\aohan\Desktop\156\dcb_schedule_core.exe


echo 准备添加EXE路径到注册表
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v dcb_schedule_core /t REG_SZ /d "%PATH_TO_EXE%"
echo 注册表已添加成功，更新完成，"%PATH_TO_EXE%" 将在下次启动时运行。
pause