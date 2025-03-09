# 파일명: test_hello_mars.py
# 설명: Hello Mars 출력의 테스트 코드
# 작성자: Rigu1
# 작성일: 2025-03-08

PARENT_DIR = "/".join(__file__.split("/")[:-2])

FILE_NAME = "hello_mars.py"
FILE_PATH = PARENT_DIR + "/" + FILE_NAME

def test_hello_mars():
    context = {}

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        exec(file.read(), context)

    output = ""
    
    if context["MESSAGE"] == "Hello Mars":
        output += "🟢 PASS"
    else:
        output += "🔴 FAIL << The message is different from \"Hello Mars\"."
    
    print(output + " << test_hello_mars")

if __name__ == "__main__":
    test_hello_mars()
