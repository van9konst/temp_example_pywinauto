using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DataGridView
{
    public partial class Form1 : Form
    {
        public class Item
        {
            public string Code {get; set; }
            public string Description { get; set; }
        }
        public ObservableCollection<Item> Items = new ObservableCollection<Item>();
        public Form1()
        {
            InitializeComponent();

            Items.Add(new Item() { Code = "ABCD", Description = "asdasda" });
            Items.Add(new Item() { Code = "WTF", Description = "hdfhsery" });

            dataGridView1.DataSource = Items;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Items.Add(new Item { Code = DateTime.Now.ToString(), Description = DateTime.Now.ToString() });
            dataGridView1.DataSource = null;
            dataGridView1.DataSource = Items;
            dataGridView1.Refresh();
        }
    }
}
