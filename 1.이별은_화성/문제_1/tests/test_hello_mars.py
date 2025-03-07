# 파일명: test_hello_mars.py 
# 설명: Hello Mars 출력의 테스트 코드
# 작성자: Rigu1
# 작성일: 2025-03-08

message = "Hello Mars"

def test_hello_mars(): 
    output = ""
    
    if message == "Hello Mars":
        output += "🟢 PASS"
    else :
        output += "🔴 FAIL"
        
    print(output + " << test_hello_mars")
        
test_hello_mars()