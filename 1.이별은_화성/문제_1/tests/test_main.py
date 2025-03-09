# 파일명: test_main.py
# 설명: 로그 출력의 테스트 코드
# 작성자: Rigu1
# 작성일: 2025-03-09

PARENT_DIR = "/".join(__file__.split("/")[:-2])
STATIC_DIR = PARENT_DIR + "/static"

FILE_NAME = "mission_computer_main.log"
FILE_PATH = STATIC_DIR + "/" + FILE_NAME

LOG = ["timestamp,event,messag", 
       "2023-08-27 12:00:00,INFO,Center and mission control systems powered down."]

def test_main():
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        log_data = file.read().splitlines()

    output = ""

    if LOG[0] != log_data[0] or LOG[-1] != log_data[-1]:
        output += "🔴 FAIL << The log is different. "

    if output == "":
        output += "🟢 PASS"
    
    print(output + " << test_main")

if __name__ == "__main__":
    test_main()