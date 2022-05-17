from odoo import models, fields

class DormitoryManager(models.Model):
    _name = "dormitory.manager"
    _description = "Dormitory Manager"
    
    name = fields.Char(string = "Tên KTX", required=True)
    email = fields.Char(string="Email")
    address = fields.Char(string="Địa chỉ")
    year_of_birth = fields.Date("Ngày thành lập")
    image = fields.Binary("Image's Dormitory", required=False, attachment=True)
    phone_number = fields.Char('Điện thoại')
    