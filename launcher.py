import subprocess

def main():
    while True:
        login_type = subprocess.run(['python', 'Title Screen.py'], capture_output=True, text=True).stdout.strip()
        if not login_type:
            break
        subprocess.run(['python', 'UITraffic.py'])

if __name__ == "__main__":
    main()
