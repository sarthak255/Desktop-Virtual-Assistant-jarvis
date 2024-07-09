# src/problem_fixer.py
import os
import psutil
import subprocess

# Function to fix common issues (Windows example)
def fix_common_issues():
    def clear_temp_files():
        temp_path = os.getenv('TEMP')
        for root, dirs, files in os.walk(temp_path):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Failed to delete {file}: {e}")

    def restart_explorer():
        subprocess.call(["taskkill", "/F", "/IM", "explorer.exe"])
        subprocess.call(["start", "explorer.exe"], shell=True)

    def check_disk():
        subprocess.call(["chkdsk", "/f", "C:"])

    def optimize_memory():
        os.system("echo 1 > /proc/sys/vm/drop_caches")

    clear_temp_files()
    restart_explorer()
    check_disk()
    optimize_memory()

# Test the problem fixer function
if __name__ == "__main__":
    fix_common_issues()
