# inventory.py
# 인벤토리 관리 클래스
# 2025-03-18
# Rigu1


class InventoryManager:
    STATIC_PATH = '/static'
    ROOT_PATH = '/'.join(__file__.split('/')[:-1])

    TARGET_FILE_NAME = 'Mars_Base_Inventory_List.csv'
    TARGET_FILE_PATH = ROOT_PATH + STATIC_PATH + '/' + TARGET_FILE_NAME

    def __init__(self):
        self.inventory_data = []

    def lord_data(self):
        try:
            with open(self.TARGET_FILE_PATH, 'r', encoding='utf-8') as file:
                self.inventory_data = file.read().splitlines()
        except FileNotFoundError:
            print(f'❌ ERROR: File not found')

        return None

    def print_inventory_data(self):
        print(*self.inventory_data, sep='\n')

    def get_inventory_data(self):
        return self.inventory_data


if __name__ == '__main__':
    inventory_manager = InventoryManager()
    inventory_manager.lord_data()
    inventory_manager.print_inventory_data()
