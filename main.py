from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import logging

from table_executor import start
from configs import Config


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(module)-12s %(funcName)-12s %(message)s',
    datefmt='%m-%d %H:%M'
)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)


class LoadExcelMenu(GridLayout):

    def go(self):
        app = App.get_running_app()
        config_data = {
            'file_path': app.root.ids.path.text,
            'prices_sheet_name': app.root.ids.price_sheet_name.text,
            'sheet_name': app.root.ids.sheet_name.text,
            'new_sheet_name': f'{app.root.ids.sheet_name.text} Copy'
        }
        config = Config()
        config.load_configs(config_data)
        try:
            start(config)
            result = 'Success'
        except Exception as err:
            logging.error(str(err))
            result = str(err)
        return result


class ExcelApp(App):
    Window.size = (500, 380)
    title = 'Excell app'

    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return LoadExcelMenu()

    def _on_file_drop(self, window, file_path):
        app = App.get_running_app()
        app.root.ids.path.text = file_path.decode('UTF-8')
        return file_path


if __name__ == '__main__':
    ExcelApp().run()
