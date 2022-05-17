from odoo import models, fields, api


class Customer(models.Model):
     _name = 'customer'
     _description = 'Customer'

     name = fields.Char(string="Khách hàng", required=True)
     phone = fields.Char(string="Số điện thoại")
     address = fields.Char(string="Địa chỉ")
     product_ids = fields.Many2many('clothing.management', string="Sản phẩm đã mua")
     payment = fields.Integer(compute="_compute_payment", string="Tổng tiền")
     
     @api.depends('product_ids')
     def _compute_payment(self):
        for r in self:
            r.payment = sum(r.product_ids.mapped('price'))
            
            print(r.product_ids)
    
                
                
                
                
                