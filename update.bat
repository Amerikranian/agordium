@echo off
cd src
if exist output\ (
    echo Nuking output
    rmdir /s /q output
)
echo Updating files
aws s3 ls --recursive audio-game-recordings > file_list.txt
echo Updating webpages
python main.py
echo Finished
cd ..