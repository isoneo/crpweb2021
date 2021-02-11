REM initial migration and initial user setup
if "%COMPUTERNAME%" == "AMDWILLHQ" (python "D:/Scripts/webdev/crpweb2021/setup_related/Wipeout_psql_db_recreate.py") else (python "C:\scripts\www\capybara\capybara\initial_data\Wipeout_psql_db_recreate.py")
cd ..
cd backend

python manage.py makemigrations
python manage.py migrate

if "%COMPUTERNAME%" == "AMDWILLHQ" (python "D:/Scripts/webdev/crpweb2021/setup_related/user_create/email_import.py") else (python "C:\scripts\www\capybara\capybara\initial_data\user_create\email_import.py")
