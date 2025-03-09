# 파일명: test_main.py
# 설명: 로그 출력의 테스트 코드
# 작성자: Rigu1
# 작성일: 2025-03-09

TEST_FILE_NAME = __file__.split("/")[-1]

PARENT_DIR = "/".join(__file__.split("/")[:-2])
STATIC_DIR = PARENT_DIR + "/static"

LOG_FILE_NAME = "mission_computer_main.log"
LOG_FILE_PATH = STATIC_DIR + "/" + LOG_FILE_NAME

LOG = ["timestamp,event,message", 
       "2023-08-27 12:00:00,INFO,Center and mission control systems powered down."]

def test_main():
    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as file:
            log_data = file.read().splitlines()
    except FileNotFoundError:
        print(f"❌  ERROR: 로그 파일을 찾을 수 없습니다: {LOG_FILE_NAME}" )
        return

    if LOG[0] != log_data[0] or LOG[-1] != log_data[-1]:
        print(f"🔴  FAIL: The log is different.")
        return

    print(f"🟢  PASS")
    return

if __name__ == "__main__":
    print(TEST_FILE_NAME)
    test_main()
    