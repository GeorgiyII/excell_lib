class Config:

    def __init__(self):
        self.file_path = None
        self.header_rows = [1, 2, 3]
        self.prices_sheet_name = None
        self.row_with_params_number = 2
        self.separator_symbol = ';'
        self.rows_with_merged_cells = [1, 2]
        self.sheet_name = None
        self.new_sheet_name = None

    def load_configs(self, data):
        for attr in data:
            self.__setattr__(attr, data[attr])
        return self

    def make_new_worksheet(self):
        self.new_sheet_name = f"{self.sheet_name} Copy"
