# inventory.py
# 인벤토리 관리 클래스
# 2025-03-18
# Rigu1


class InventoryManager:
    ERROR_MESSAGES = {
        FileNotFoundError: 'File not found >> {}',
        PermissionError: 'Permission denied >> {}',
    }

    STATIC_PATH = '/static'
    ROOT_PATH = '/'.join(__file__.split('/')[:-1])

    TARGET_FILE_NAME = 'Mars_Base_Inventory_List.csv'
    TARGET_FILE_PATH = ROOT_PATH + STATIC_PATH + '/' + TARGET_FILE_NAME

    def __init__(self):
        self.inventory_lines = self._get_data_from_file()

    def _get_data_from_file(self):
        try:
            with open(self.TARGET_FILE_PATH, 'r', encoding='utf-8') as file:
                return file.read().splitlines()
        except (FileNotFoundError, PermissionError) as e:
            error_message = self.ERROR_MESSAGES[type(e)].format(
                self.TARGET_FILE_PATH
            )
            raise type(e)(error_message) from e

    def get_inventory_lines(self):
        return self.inventory_lines


if __name__ == '__main__':
    inventory_manager = InventoryManager()
    print(*inventory_manager.get_inventory_lines(), sep='\n')
