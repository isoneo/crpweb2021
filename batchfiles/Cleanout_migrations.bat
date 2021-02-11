REM initial migration and initial user setup
if "%COMPUTERNAME%" == "AMDWILLHQ" (python "D:/Scripts/webdev\crpweb2021\setup_related\Cleanout Migration files.py") else (python "C:\scripts\www\capybara\capybara\initial_data\Cleanout Migration files.py")
