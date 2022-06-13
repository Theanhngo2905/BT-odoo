

from odoo import models, fields, api
from odoo.exceptions import UserError


class ClothingManagement(models.Model):
    _name = 'clothing.management'
    _description = 'Clothing Management'
    
    name = fields.Char(require=True, string="SKU", size=8, trim=True, translate=False, groups='base.group_system')
    description = fields.Text(string="Detail", default='AAAAA')
    clothing_ids = fields.One2many('item', 'item_id', string="Sản phẩm")
    amount = fields.Integer(string="Total of product")
    start_date = fields.Date(string="Start date", default=fields.Date.today, help="Support for calendar view")
    stop_date = fields.Date(string="Stop date", help="Support for calendar view")
    date_time = fields.Datetime(string="DateTime")
    # quantity_end = fields.Integer(string="Số lượng còn lại", computed="_compute_quantity_end", 
    #                               inverse="_set_amount", search="_search_all")
    
    def test_orm(self):
        """Test hàm create"""
        vals_list = [
            {
                'name': 'Loan',
                # 'description': 'Cindy',
                'amount': 100,
                'start_date': '2022-06-12',
                'stop_date': '2022-06-18',
                'date_time': '2022-06-12 08:00:00',
            },
        ]
        # self.env['clothing.management'].create(vals_list)
        """Test hàm copy"""
        # self.copy()
        """Test hàm default_get()"""
        # self.default_get(['description', 'start_date'])
        #

        """Test hàm name_create(name)"""
        # self.env['clothing.management'].name_create('Dung')
        
        """Test hàm write()"""
        # item_value = {
        #     'name': 'Lien ket voi Loan'
        # }
        #
        # items = self.env['item'].search([])
        # vals = {
        #     'amount': 200,
        #     'clothing_ids': [(6, 0, items.ids)]
        # }
        # self.write(vals)
        
        """Test ham fields_get()"""
        # self.fields_get()
        
        clothing_view_tree = self.env.ref('clothing.clothing_management_view_tree')
        pass

    def name_get(self):
        return super(ClothingManagement, self).name_get()

    # thực hành actions URL
    def custom_button_method(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.youtube.com',
            "target": "new",
            } 
        
    # tạo mới bản ghi  
    def create_items(self):
        item_1 = {
            'name': 'Trouser',
            }
        item_2 = {
            'name': 'Skirt'
        }
        item_value = {
            'name': 'SKU2',
            'clothing_ids': [
                (0, 0, item_1),
                (0, 0, item_2)
                ]
            }
        record = self.env['clothing.management'].create(item_value)
    
    # cập nhật giá trị của bản ghi    
    def change_item_name(self):
        self.ensure_one()  # kiểm tra self có đúng 1 bản ghi hay không, nếu muốn update nhiều có thể xóa dòng này
        self.name = 'SKU2'   
        
    def default_get_2(self):  # trả về các giá trị mặc định của trường truyền vào
        default_get_1 = self.env['clothing.management'].default_get(['name', 'amount'])
        print(default_get_1)
        
        
