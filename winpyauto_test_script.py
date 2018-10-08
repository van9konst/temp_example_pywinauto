from pywinauto import application
from pywinauto.controls import uia_controls

vx_path = r"C:\DataGridView\DataGridView\bin\Debug\DataGridView.exe"

vx = application.Application(backend="uia")
vx.connect(path=vx_path)
wvx = vx.window()
print(wvx.window_text())
wvx.print_control_identifiers()
wvx.window(auto_id="button1", control_type="Button").click_input()

ss = wvx.window(auto_id="dataGridView1")

uia_controls.ListViewWrapper(ss).get_items()
#uia_controls.ListViewWrapper(wvx.window(auto_id="dataGridView1")).get_items()
uia_controls.ButtonWrapper(wvx.window(auto_id="button1", control_type="Button")).click()

