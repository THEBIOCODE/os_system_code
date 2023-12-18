콘솔에 출력없이 백그라운드로 실행
import subprocess

# 실행할 프로그램 경로
program_path = r'C:\Path\to\Your\Program.exe'

# subprocess를 사용하여 프로그램 실행
subprocess.Popen(program_path, creationflags=subprocess.CREATE_NO_WINDOW)
