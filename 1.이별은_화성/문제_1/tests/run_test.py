# 파일명: run_test.py
# 설명: tests 폴더 내의 테스트 파일 실행 스크립트
# 작성자: Rigu1
# 작성일: 2025-03-11

TESTS_DIR = 'tests/'
TEST_FILES = ['test_hello_mars.py', 'test_main.py']


for test_file in TEST_FILES:
    file_path = TESTS_DIR + test_file
    with open(file_path, 'r', encoding='utf-8') as file:
        print(f'{test_file}...')
        exec(file.read())
        print()
