# 파일명: test_main.py
# 설명: 로그 출력의 테스트 코드
# 작성자: Rigu1
# 작성일: 2025-03-09

PARENT_DIR = '/'.join(__file__.split('/')[:-2])

TARGET_FILE_NAME = 'main.py'
TARGET_FILE_PATH = PARENT_DIR + '/' + TARGET_FILE_NAME

LOG = [
    'timestamp,event,message',
    '2023-08-27 12:00:00,INFO,Center and mission control systems powered down.',
]


def setup_log_manager():
    global_namespace = {'__file__': TARGET_FILE_PATH}

    with open(TARGET_FILE_PATH, 'r', encoding='utf-8') as file:
        exec(file.read(), global_namespace)

    LogManager = global_namespace.get('LogManager')

    log_manager = LogManager()
    log_manager.load_log()
    return log_manager


def test_print_log(log_manager):
    print(f'> {test_print_log.__name__}')

    log_data = log_manager.get_log_data()

    if LOG[0] != log_data[0] or LOG[-1] != log_data[-1]:
        print('🔴  FAIL: The log is different.')
        return

    print('🟢  PASS')


def test_reverse_print_log(log_manager):
    print(f'> {test_reverse_print_log.__name__}')

    log_data = log_manager.get_reverse_log_data()

    if LOG[0] != log_data[-1] or LOG[-1] != log_data[0]:
        print('🔴  FAIL: The reverse log is different.')
        return

    print('🟢  PASS')


if __name__ == '__main__':
    log_manager = setup_log_manager()
    test_print_log(log_manager)
    test_reverse_print_log(log_manager)
