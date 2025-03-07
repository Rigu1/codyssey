# 파일명: test_hello_mars.py
# 설명: Hello Mars 출력의 테스트 코드
# 작성자: Rigu1
# 작성일: 2025-03-08

file_path = "/".join(__file__.split("/")[:-2]) + "/hello_mars.py"
context = {}

with open(file_path, "r", encoding="utf-8") as file:
    exec(file.read(), context)

message = context["MESSAGE"]

def test_hello_mars():
    output = ""
    
    if message == "Hello Mars":
        output += "🟢 PASS"
    else:
        output += "🔴 FAIL"
    
    print(output + " << test_hello_mars")

if __name__ == "__main__":
    test_hello_mars()
