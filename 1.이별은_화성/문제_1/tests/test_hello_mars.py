# 파일명: test_hello_mars.py
# 설명: Hello Mars 출력의 테스트 코드
# 작성자: Rigu1
# 작성일: 2025-03-08

TEST_FILE_NAME = __file__.split("/")[-1]

PARENT_DIR = "/".join(__file__.split("/")[:-2])

TARGET_FILE_NAME = "hello_mars.py"
TARGET_FILE_PATH = PARENT_DIR + "/" + TARGET_FILE_NAME

MESSAGE = "Hello Mars"

def test_hello_mars():
    global_namespace = {}
    
    with open(TARGET_FILE_PATH, "r", encoding="utf-8") as file:
        exec(file.read(), global_namespace)
        
    massage = global_namespace["MESSAGE"]
        
    if massage == MESSAGE:
        print(f"🟢  PASS")
        return

    print(f"🔴  FAIL << The message is different from {MESSAGE}")
    return

if __name__ == "__main__":
    print(TEST_FILE_NAME)
    test_hello_mars()
