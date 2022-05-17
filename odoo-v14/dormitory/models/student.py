from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "student"
    _description = "Student information"
    
    student_code = fields.Char("Mã sinh viên",required = True)
    name_student = fields.Char("Tên sinh viên", required=True)
    image = fields.Binary("Ảnh sinh viên")
    date_of_birth = fields.Date("Ngày tháng năm sinh")
    address = fields.Char("Địa chỉ")
    khoa_hoc = fields.Char("Khóa học")
    class_student = fields.Char("Lớp")
    email = fields.Char("Email sinh viên")
    phone = fields.Char("Số điện thoạt")
    room_id = fields.Many2one("dorm.room", "Phòng")
    canteen_list = fields.Many2many("canteen.information", "student_canteen_rel", "student_id", "canteen_id")
    total_student = fields.Char("Số người hiện đang ở trong phòng", readonly=True, store=True)
    total_price = fields.Float(string="Tổng số tiền cần phải đóng trong 1 tháng", compute="_total_price")
    
    @api.onchange('room_id')
    def _onchange_room_id(self):
        if self.room_id:
            self.total_student = self.room_id.student_register
    
    @api.depends('room_id', "canteen_list")
    def _total_price(self):
        for rc in self:
            rc.total_price = rc.room_id.price + sum(rc.canteen_list.mapped('price'))
    
    @api.constrains("room_id")
    def _check_room(self):
        for rc in self:
            if rc.room_id.floor == "1" and len(rc.room_id.student_ids) > 8:
                 raise ValidationError("Phòng đã đầy. Mời sang phòng khác!!!")
            elif rc.room_id.floor == "2" and len(rc.room_id.student_ids) > 10:
                raise ValidationError("Phòng đã đầy. Mời sang phòng khác!!!")
            elif rc.room_id.floor == "3" and len(rc.room_id.student_ids) > 10:
                raise ValidationError("Phòng đã đầy. Mời sang phòng khác!!!")
            
    