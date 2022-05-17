from odoo import fields, models

class CanteenInformation(models.Model):
    _name = "canteen.information"
    _description = "Canteen Information"
    
    name = fields.Char(string="Tên món ăn", required=True)
    currency_id = fields.Many2one("res.currency", string="Đơn vị")
    price = fields.Monetary(string="Giá tiền")
    