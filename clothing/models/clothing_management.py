

from odoo import models, fields, api


class ClothingManagement(models.Model):
    _name = 'clothing.management'
    _description = 'Clothing Management'
    
    name = fields.Char(require=True, string="SKU", size=8, trim=True, translate=False, groups='base.group_system')
    description = fields.Text(string="Detail")
    clothing_ids = fields.One2many('item', 'item_id', string="Sản phẩm")
    amount = fields.Integer(string="Total of product")
    start_date = fields.Date(string="Start date", default=fields.Date.today, help="Support for calendar view")
    stop_date = fields.Date(string="Stop date", help="Support for calendar view")
    quantity_end = fields.Integer(string="Số lượng còn lại", computed="_compute_quantity_end", 
                                  inverse="_set_amount", search="_search_all")
    
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
        
        
