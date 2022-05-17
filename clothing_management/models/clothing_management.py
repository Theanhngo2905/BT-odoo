from odoo import models, fields, api


class clothing_management(models.Model):
     _name = 'clothing.management'
     _description = 'Clothing Management'

     name = fields.Char(string="Mã sản phẩm", required=True)
     name_of_product = fields.Char(string="Tên sản phẩm")
     image = fields.Binary(string="Image")
     mota = fields.Text(string="Mô tả chi tiết")
     type = fields.Selection([('ao', 'Áo'), ('quan', 'Quần'), ('chanvay', 'Chân váy'), ('vaylienthan', 'Váy công sở'), 
                              ('dongu', 'Đồ ngủ')], string="Kiểu dáng")
     size = fields.Selection([('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL')], string="Kích cỡ")
     color = fields.Selection([('den', 'Đen'), ('trang', 'Trắng'), ('xanh', 'Xanh'), ('do', 'Đỏ')])
     price = fields.Integer(string="Giá tiền")