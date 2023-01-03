import json as js

class DictFill:
    def __init__(self) -> None:
        self.result = {}
        self.result_temp = [self.result]
        self.cur_key_queue = []
        self.delimeter = '-'

    def clean_val(self, val: str):
        if val.startswith((' ', self.delimeter)):
            val = val.replace(" " * val.find(self.delimeter) + self.delimeter + ' ', '')
        return val
    
    def move_in(self):
        self.result_temp.append(self.result_temp[-1][self.cur_key_queue[-1]])

    def move_out(self):
        self.result_temp.pop(-1)
        self.cur_key_queue.pop(-1)

    def add_new_item(self, val: str):
        if len(self.cur_key_queue) == 0:
            self.result[self.clean_val(val)] = {}
            self.cur_key_queue.append(self.clean_val(val))
            return

        level = val.find(self.delimeter)
        level = level // 2

        while level < len(self.result_temp) - 1:
            self.move_out()
    
        while level > len(self.result_temp) - 1:
            self.move_in()

        temp = self.result_temp[-1]
        temp[self.clean_val(val)] = {}
        self.cur_key_queue.append(self.clean_val(val))
        self.move_in()

    def convert(self, filename, json_fname, encoding):
        file = open(filename, "r", encoding=encoding)
        data = file.read()
        file.close()
        data = data.split('\n')

        for val in data:
            self.add_new_item(val)

        json_file = open(json_fname, 'w', encoding=encoding)
        json_file.write(js.dumps(self.result, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': ')))
        json_file.close()

if __name__ == '__main__':
    dictFill = DictFill()
    dictFill.delimeter = '-'
    dictFill.convert("test.txt", "test.json", "UTF-8")