@echo off

echo ʵ����.exe��·��
set PATH_TO_EXE=C:\Users\aohan\Desktop\156\dcb_schedule_core.exe


echo ׼�����EXE·����ע���
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v dcb_schedule_core /t REG_SZ /d "%PATH_TO_EXE%"
echo ע�������ӳɹ���������ɣ�"%PATH_TO_EXE%" �����´�����ʱ���С�
pause