from odoo import fields, models,api
from odoo.exceptions import ValidationError

class DormRoom(models.Model):
    _name = "dorm.room"
    _description = "Dorm Room"
    name = fields.Char("Tên phòng", required=True)
    floor = fields.Selection([("1","Tầng 1"),("2","Tầng 2"),("3","Tầng 3")], compute="_check_floor", store=True)
    total_student = fields.Integer("Số sinh viên tối đa", default=0, compute="_people_in_room", store=True)
    dormitory_manager_id = fields.Many2one('dormitory.manager',"Trường")
    student_ids = fields.One2many('student','room_id','Sinh viên')
    student_register = fields.Char("Số sinh viên hiện tại đang ở trong phòng", compute="_sum_student")
    currency_id = fields.Many2one("res.currency", string="Đơn vị")
    price = fields.Monetary(string="Giá phòng 1 tháng", compute="_price")
    total_price = fields.Float(string="Tổng số tiền phòng 1 tháng", compute="_total_price")
    
    _sql_constraints = [('name', 'unique (name)', "Tên này đã được dùng. Mời nhập tên khác !!!")]
    @api.depends('floor')
    def _people_in_room(self):
        for rc in self:
            if rc.floor == "1":
                rc.total_student = 8
            else:
                rc.total_student = 10
    
    @api.constrains('name')
    def _check_name(self):
        for rc in self:
            try:
                name = int(rc.name)
            except:
                raise ValidationError('Tên phòng phải là số bắt đầu từ 100 với tầng 1, 200 với tầng 2 và 300 với tầng 3 !!!')
            if int(rc.name) not in range(101, 111) and int(rc.name) not in range(201, 211) and int(rc.name) not in range(301, 311):
                raise ValidationError("Tên phòng phải thuộc khoảng từ 100 đến 110 với tầng 1, 200 đến 210 với tầng 2, 300 đến 310 với tầng 3 !!!")

              
    @api.constrains('student_ids')
    def _check_student(self):
        for r in self:
            if r.floor == "1" and len(r.student_ids) > 2:
                raise ValidationError("Phòng đã đầy. Mời sang phòng khác!!!")
            elif r.floor == "2" and len(r.student_ids) > 10:
                raise ValidationError("Phòng đã đầy. Mời sang phòng khác!!!")
            elif r.floor == "3" and len(r.student_ids) > 10:
                raise ValidationError("Phòng đã đầy. Mời sang phòng khác!!!")
    
    @api.depends('name')
    def _check_floor(self):
        for rc in self:
            if rc.name == False:
                rc.floor = ""
            else:
                if int(rc.name[0]) == 1:
                    rc.floor = "1"
                elif int(rc.name[0]) == 2:
                    rc.floor = "2"
                elif int(rc.name[0]) == 3:
                    rc.floor = "3"
    
    @api.depends('floor')
    def _price(self):
        for rc in self:
            if rc.floor == False:
                rc.price = 0
            elif rc.floor == "1":
                rc.price = 35
            elif rc.floor == "2":
                rc.price = 25
            elif rc.floor == "3":
                rc.price = 25
    
    @api.depends("price", "student_ids")
    def _total_price(self):
        for rc in self:
            rc.total_price = rc.price * len(rc.student_ids)

    
    #Tính số sv hiện tại đang ở trong phòng
    @api.depends("student_ids")
    def _sum_student(self):
        for rc in self:
            rc.student_register = f"{len(rc.student_ids)}/{rc.total_student}"
                    