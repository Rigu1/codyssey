# inventory.py
# 인벤토리 관리 클래스
# 2025-03-18
# Rigu1


class InventoryManager:
    ERROR_MESSAGES = {
        FileNotFoundError: 'File not found >> {}',
        PermissionError: 'Permission denied >> {}',
        Exception: 'Unknown error >> {}',
    }

    STATIC_PATH = '/static'
    ROOT_PATH = '/'.join(__file__.split('/')[:-1])

    TARGET_FILE_NAME = 'Mars_Base_Inventory_List.csv'
    TARGET_FILE_PATH = ROOT_PATH + STATIC_PATH + '/' + TARGET_FILE_NAME

    OUTPUT_FILE_NAME = 'Mars_Base_Inventory_danger.csv'
    OUTPUT_FILE_PATH = ROOT_PATH + STATIC_PATH + '/' + OUTPUT_FILE_NAME

    BINARY_FILE_NAME = 'Mars_Base_Inventory_List.bin'
    BINARY_FILE_PATH = ROOT_PATH + STATIC_PATH + '/' + BINARY_FILE_NAME

    DELIMITER = ','
    REFERENCE_KEY = 'Flammability'
    THRESHOLD = 0.7

    def __init__(self):
        self.inventory_lines = self._get_split_by_delimiter(
            self._get_inventory_from_csv()
        )
        self.header = self.inventory_lines[0]
        self.inventory_items = self.inventory_lines[1:]

    def _get_inventory_from_csv(self):
        try:
            with open(self.TARGET_FILE_PATH, 'r', encoding='utf-8') as file:
                return file.read().splitlines()
        except Exception as e:
            error_message = self.ERROR_MESSAGES.get(
                type(e), self.ERROR_MESSAGES[Exception]
            ).format(self.TARGET_FILE_PATH)
            raise type(e)(error_message) from e

    def _get_split_by_delimiter(self, items):
        return [line.split(self.DELIMITER) for line in items]

    def get_inventory_lines(self):
        return self.inventory_lines

    def get_sorted_items_desc(self):
        sort_key_index = self.header.index(self.REFERENCE_KEY)

        sorted_inventory = sorted(
            self.inventory_items,
            key=lambda item: float(item[sort_key_index]),
            reverse=True,
        )

        return [self.header] + sorted_inventory

    def get_items_above_threshold(self):
        reference_key_index = self.header.index(self.REFERENCE_KEY)

        filtered_inventory = [
            item
            for item in self.inventory_items
            if float(item[reference_key_index]) >= self.THRESHOLD
        ]

        return [self.header] + filtered_inventory

    def save_dangerous_items(self):
        dangerous_inventory = self.get_items_above_threshold()

        try:
            with open(self.OUTPUT_FILE_PATH, 'w', encoding='utf-8') as file:
                for line in dangerous_inventory:
                    file.write(self.DELIMITER.join(map(str, line)) + '\n')

            print(f"Save dangerous items: {self.OUTPUT_FILE_PATH}")

        except Exception as e:
            error_message = self.ERROR_MESSAGES.get(
                type(e), self.ERROR_MESSAGES[Exception]
            ).format(self.OUTPUT_FILE_PATH)
            raise type(e)(error_message) from e

    def save_sorted_inventory_as_binary(self):
        sorted_inventory = self.get_sorted_items_desc()

        try:
            with open(self.BINARY_FILE_PATH, 'wb') as file:
                for line in sorted_inventory:
                    line_bytes = (
                        self.DELIMITER.join(map(str, line)) + '\n'
                    ).encode('utf-8')
                    file.write(line_bytes)

            print(
                f"Save sorted items as binary files: {self.BINARY_FILE_PATH}"
            )

        except Exception as e:
            error_message = self.ERROR_MESSAGES.get(
                type(e), self.ERROR_MESSAGES[Exception]
            ).format(self.BINARY_FILE_PATH)
            raise type(e)(error_message) from e

    def get_inventory_from_binary(self):
        try:
            with open(self.BINARY_FILE_PATH, 'rb') as file:
                binary_data = file.readlines()

            inventory_list = [
                line.decode('utf-8').strip() for line in binary_data
            ]

            return self._get_split_by_delimiter(inventory_list)

        except Exception as e:
            error_message = self.ERROR_MESSAGES.get(
                type(e), self.ERROR_MESSAGES[Exception]
            ).format(self.BINARY_FILE_PATH)
            raise type(e)(error_message) from e


if __name__ == '__main__':
    inventory_manager = InventoryManager()
    print(*inventory_manager.get_inventory_lines(), sep='\n')
    print(*inventory_manager.get_sorted_items_desc(), sep='\n')
    print(*inventory_manager.get_items_above_threshold(), sep='\n')
    inventory_manager.save_dangerous_items()
    inventory_manager.save_sorted_inventory_as_binary()
    print(*inventory_manager.get_inventory_from_binary(), sep='\n')
