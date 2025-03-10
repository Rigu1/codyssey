# 파일명: main.py
# 설명: 로그 출력
# 작성자: Rigu1
# 작성일: 2025-03-10

class LogManager:
    PARENT_DIR = "/".join(__file__.split("/")[:-1]) if "/" in __file__ else "."
    STATIC_DIR = PARENT_DIR + "/static"
    
    LOG_FILE_NAME = "mission_computer_main.log"
    LOG_FILE_PATH = STATIC_DIR + "/" + LOG_FILE_NAME
    
    def __init__(self):
        self.log_data = []
        
    def load_log(self):
        """로그 파일을 읽어 log_data에 저장"""
        try:
            with open(self.LOG_FILE_PATH, "r", encoding="utf-8") as file:
                self.log_data = file.read().splitlines()
        except FileNotFoundError:
            print(f"❌ ERROR: 로그 파일을 찾을 수 없습니다: {self.LOG_FILE_PATH}")

    def get_log_data(self):
        return self.log_data

    def print_log(self):
        print(*self.log_data, sep="\n")
    
if __name__ == "__main__": 
    log_manager = LogManager()  
    log_manager.load_log()  
    log_manager.print_log()
