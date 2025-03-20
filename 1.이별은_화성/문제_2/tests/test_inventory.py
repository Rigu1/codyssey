# test_inventory.py
# 인벤토리 기능 테스트
# 2025-03-17
# Rigu1

ROOT_PATH = '/'.join(__file__.split('/')[:-2])

TARGET_FILE_NAME = 'inventory.py'
TARGET_FILE_PATH = ROOT_PATH + '/' + TARGET_FILE_NAME

INVENTORY_BOUNDARIES = {
    'first_lines': [
        'Substance',
        'Weight (g/cm³)',
        'Specific Gravity',
        'Strength',
        'Flammability',
    ],
    'last_lines': ['Phenolic Resin', 'Various', 'Various', 'Various', '0'],
}


def setup_inventory_manager():
    global_namespace = {'__file__': TARGET_FILE_PATH}

    with open(TARGET_FILE_PATH, 'r', encoding='utf-8') as file:
        exec(file.read(), global_namespace)

    InventoryManager = global_namespace.get('InventoryManager')

    inventory_manager = InventoryManager()
    return inventory_manager


# 1. Mars_Base_Inventory_List.csv 의 내용을 읽어 들어서 출력
def test_print_inventory_list(inventory_manager):
    print(f'> {test_print_inventory_list.__name__}')

    inventory_lines = inventory_manager.get_inventory_lines()

    if inventory_lines[0] != INVENTORY_BOUNDARIES['first_lines']:
        print(f'🔴  FAIL: First line mismatch.')
        return

    if inventory_lines[-1] != INVENTORY_BOUNDARIES['last_lines']:
        print(f'🔴  FAIL: Last line mismatch.')
        return

    print('🟢  PASS')


# 2. Mars_Base_Inventory_List.csv 내용을 읽어서 Python의 리스트(List) 객체로 변환
def test_get_inventory_list(inventory_manager):
    print(f'> {test_get_inventory_list.__name__}')

    inventory_lines = inventory_manager.get_inventory_lines()

    if not isinstance(inventory_lines, list):
        print(f'🔴  FAIL: Data is not a list.')
        return

    print('🟢  PASS')


# 3. 배열 내용을 적재 화물 목록을 인화성이 높은 순으로 정렬
def test_get_sort_inventory_list(inventory_manager):
    print(f'> {test_get_sort_inventory_list.__name__}')

    sorted_inventory = inventory_manager.get_sorted_items_desc()
    sort_key_index = sorted_inventory[0].index(inventory_manager.REFERENCE_KEY)

    for i in range(1, len(sorted_inventory) - 1):
        if float(sorted_inventory[i][sort_key_index]) < float(
            sorted_inventory[i + 1][sort_key_index]
        ):
            print(f'🔴  FAIL: Sorting order is incorrect.')
            return

    print('🟢  PASS')


# 4. 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력
def test_get_items_above_threshold(inventory_manager):
    print(f'> {test_get_items_above_threshold.__name__}')

    filtered_inventory = inventory_manager.get_items_above_threshold()
    threshold_index = filtered_inventory[0].index(
        inventory_manager.REFERENCE_KEY
    )

    for item in filtered_inventory[1:]:
        if float(item[threshold_index]) < inventory_manager.THRESHOLD:
            print(f'🔴  FAIL: Filtering incorrect.')
            return

    print('🟢  PASS')


# 5. 인화성 지수가 0.7 이상되는 목록을 CSV 포맷(Mars_Base_Inventory_danger.csv)으로 저장
def test_save_dangerous_items(inventory_manager):
    print(f'> {test_save_dangerous_items.__name__}')

    inventory_manager.save_dangerous_items()

    try:
        with open(
            inventory_manager.OUTPUT_FILE_PATH, 'r', encoding='utf-8'
        ) as file:
            lines = file.readlines()

        if not lines:
            print(f'🔴  FAIL: CSV file is empty.')
            return

    except FileNotFoundError:
        print(f'🔴  FAIL: CSV file not found.')
        return

    print('🟢  PASS')


# bonus-1. 인화성 순서로 정렬된 배열의 내용을 이진 파일형태로 저장 (파일이름은 Mars_Base_Inventory_List.bin)
# bonus-2. 저장된 Mars_Base_Inventory_List.bin 의 내용을 다시 읽어 들여서 화면에 내용을 출력
def test_save_and_load_binary_inventory(inventory_manager):
    print(f'> {test_save_and_load_binary_inventory.__name__}')

    inventory_manager.save_sorted_inventory_as_binary()
    loaded_inventory = inventory_manager.get_inventory_from_binary()

    if not loaded_inventory:
        print(f'🔴  FAIL: Binary file loading failed.')
        return

    if loaded_inventory[0] != inventory_manager.header:
        print(f'🔴  FAIL: Header mismatch.')
        return

    print('🟢  PASS')


if __name__ == '__main__':
    inventory_manager = setup_inventory_manager()

    test_print_inventory_list(inventory_manager)
    test_get_inventory_list(inventory_manager)
    test_get_sort_inventory_list(inventory_manager)
    test_get_items_above_threshold(inventory_manager)
    test_save_dangerous_items(inventory_manager)
    test_save_and_load_binary_inventory(inventory_manager)
