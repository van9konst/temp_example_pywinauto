from pywinauto import application
from pywinauto.controls import uia_controls

vx_path = r"C:\DataGridView\temp_example_pywinauto\DataGridView\bin\Debug\DataGridView.exe"

vx = application.Application(backend="uia")
vx.connect(path=vx_path)
wvx = vx.window()
print(wvx.window_text())
wvx.print_control_identifiers()
wvx.window(auto_id="button1", control_type="Button").click_input()

"""from original pywinauto"""
# def test_get_column(self):
#     """Test get_column() method for the ListView controls"""
#     # ListView
#     self.listview_tab.set_focus()
#     listview = self.listview_tab.children(class_name=u"ListView")[0]
#     listview_col = listview.get_column(1)
#     self.assertEqual(listview_col.texts()[0], u"Name")
#
#     # ListBox
#     self.listbox_datagrid_tab.set_focus()
#     listbox = self.listbox_datagrid_tab.children(class_name=u"ListBox")[0]
#     self.assertRaises(IndexError, listbox.get_column, 0)
#
#     # DataGrid
#     datagrid = self.listbox_datagrid_tab.children(class_name=u"DataGrid")[0]
#     datagrid_col = datagrid.get_column(2)
#     self.assertEqual(datagrid_col.texts()[0], u"B")
#
#     self.assertRaises(IndexError, datagrid.get_column, 10)

# Assume that this is  a gridView
wvx.window(auto_id="dataGridView1").get_column()
wvx.window(auto_id="dataGridView1").wrapper_object().get_column()
wvx.window(auto_id="dataGridView1")[1].get_column()
wvx.window(auto_id="dataGridView1").wrapper_object()[1].get_column()

# Assume that this is  a Table
wvx.window(auto_id="dataGridView1").get_item(0, 0)

wvx.window(auto_id="dataGridView1").children(control_type="Custom")[1].children()
wvx.window(auto_id="dataGridView1").children(control_type="Custom")[1].texts()
