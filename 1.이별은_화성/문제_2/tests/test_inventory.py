# test_inventory.py
# 인벤토리 기능 테스트
# 2025-03-17
# Rigu1

ROOT_PATH = '/'.join(__file__.split('/')[:-2])

TARGET_FILE_NAME = 'inventory.py'
TARGET_FILE_PATH = ROOT_PATH + '/' + TARGET_FILE_NAME

INVENTORY_BOUNDARIES = {
    'first_item': 'Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability',
    'last_item': 'Phenolic Resin,Various,Various,Various,0',
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

    inventory_item = inventory_manager.get_inventory_data()

    if inventory_item is None:
        return

    actual_first_item = inventory_item[0]
    actual_last_item = inventory_item[-1]

    expected_first_item = INVENTORY_BOUNDARIES['first_item']
    expected_last_item = INVENTORY_BOUNDARIES['last_item']

    if actual_first_item != expected_first_item:
        print(f'🔴  FAIL: The data is different.')
        return

    if actual_last_item != expected_last_item:
        print(f'🔴  FAIL: The data is different.')
        return

    print('🟢  PASS')


# 2. Mars_Base_Inventory_List.csv 내용을 읽어서 Python의 리스트(List) 객체로 변환
# 3. 배열 내용을 적제 화물 목록을 인화성이 높은 순으로 정렬
# 4. 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력
# 5. 인화성 지수가 0.7 이상되는 목록을 CSV 포멧(Mars_Base_Inventory_danger.csv)으로 저장

# bonus-1. 인화성 순서로 정렬된 배열의 내용을 이진 파일형태로 저장 (파일이름은 Mars_Base_Inventory_List.bin)
# bonus-2. 저장된 Mars_Base_Inventory_List.bin 의 내용을 다시 읽어 들여서 화면에 내용을 출력

if __name__ == '__main__':
    inventory_manager = setup_inventory_manager()
    test_print_inventory_list(inventory_manager)
