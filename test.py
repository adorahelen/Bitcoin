import os
import platform # 운영체제 정보 감지 
import subprocess # 쉘 명령어 실행 

# 01. 운영체제 감지 함수 
def detect_os():
    return platform.system() # ex) 'windows', 'Linux', etc 

# if 유닉스 계열인 경우
def detect_filesystem_unix(path="/"):
    try:
        result = subprocess.run(['df', '-T', path], stdout=subprocess.PIPE, text=True)
        lines = result.stdout.strip().split('\n')
        if len(lines) > 1:
            return lines[1].split()[1]  # fs type
    except Exception as e:
        print("Error detecting filesystem:", e)
    return "Unknown"

# else 윈도우 계열인 경우 
def detect_filesystem_windows(drive="C:"):
    try:
        import win32api
        import win32file
        fs_name = win32file.GetVolumeInformation(drive + "\\")[4]
        return fs_name
    except ImportError:
        print("pywin32 is required for filesystem detection on Windows.")
    except Exception as e:
        print("Error:", e)
    return "Unknown"

# 재귀적으로 파일 목록 출력 (파일 크기와 경로)
def list_files_recursively(start_path):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            try:
                full_path = os.path.join(root, file)
                stat_info = os.stat(full_path)
                print(f"[FILE] {full_path} - Size: {stat_info.st_size} bytes")
            except Exception as e:
                print(f"Error reading {file}: {e}")

def main():
    os_type = detect_os()
    print(f"Detected OS: {os_type}")

    if os_type == "Linux" or os_type == "Darwin":
        fs_type = detect_filesystem_unix()
        print(f"Detected OS: {os_type}")

    elif os_type == "Windows":
        fs_type = detect_filesystem_windows()
        print(f"Detected OS: {os_type}")

    else:
        fs_type = "Unknown"
        print(f"Detected OS: {os_type}")


    print(f"Detected File System: {fs_type}")
    print("\nListing files from root...\n")
    if os_type == "Windows":
        #list_files_recursively("C:\\")
        print(f"Detected File System: {fs_type}")

    else:
        #list_files_recursively("/")
        print(f"Detected File System: {fs_type}")


if __name__ == "__main__":
    main()
