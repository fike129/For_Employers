using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Colllege
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "data_College_OLDDataSet._Студенты_С_ИП_21_1". При необходимости она может быть перемещена или удалена.
            this.студенты_С_ИП_21_1TableAdapter.Fill(this.data_College_OLDDataSet._Студенты_С_ИП_21_1);

        }
    }
}
