# 파일명: test_main.py
# 설명: 로그 출력의 테스트 코드
# 작성자: Rigu1
# 작성일: 2025-03-09

TEST_FILE_NAME = __file__.split("/")[-1]

PARENT_DIR = "/".join(__file__.split("/")[:-2]) 

TARGET_FILE_NAME = "main.py"
TARGET_FILE_PATH = PARENT_DIR + "/" + TARGET_FILE_NAME

LOG = ["timestamp,event,message", 
       "2023-08-27 12:00:00,INFO,Center and mission control systems powered down."]

def test_main():
    global_namespace = {"__file__": TARGET_FILE_PATH} 

    with open(TARGET_FILE_PATH, "r", encoding="utf-8") as file:
        exec(file.read(), global_namespace) 

    LogManager = global_namespace.get("LogManager")

    log_manager = LogManager() 
    log_manager.load_log()
    log_data = log_manager.get_log_data()
    
    if LOG[0] != log_data[0] or LOG[-1] != log_data[-1]:
        print(f"🔴  FAIL: The log is different.")
        return

    print(f"🟢  PASS")

if __name__ == "__main__":
    print(TEST_FILE_NAME)
    test_main()
