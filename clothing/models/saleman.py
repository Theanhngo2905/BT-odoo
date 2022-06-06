from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Saleman(models.Model):
    _name = 'saleman'
    _description = 'Saleman'

    name = fields.Char(string="Họ và tên", required=True)
    image = fields.Binary(string="Image")
    phone = fields.Char(string="Số điện thoại")
    address = fields.Char(string="Địa chỉ")
    birthday = fields.Date(string="Ngày sinh")
    age = fields.Integer(string="Tuổi", compute='_compute_age')
    start_date = fields.Date(string="Từ ngày")
    end_date = fields.Date(string="Đến ngày")
    hour_of_work = fields.Integer(string="Số giờ làm việc", compute="_compute_hour_of_work")
    time_off = fields.Integer(string="Số ngày nghỉ")
    salary = fields.Integer(string="Lương", compute="_compute_salary")
    overtime = fields.Float(string="Tăng ca (số giờ)", digits=(2,1))
    total_salary = fields.Integer(string="Tổng lương", compute="_compute_total_salary")
     
    @api.depends('birthday')
    def _compute_age(self):
        current_year = fields.Date.today().year
        for r in self:
            if r.birthday:
                r.age = current_year - r.birthday.year 
            else: 
                r.age = 0
                
    @api.constrains('birthday')
    def _check_birthday(self):
        for r in self:
            if r.birthday > fields.Date.today():
                raise ValidationError("Ngày tháng năm sinh phải nhỏ hơn ngày tháng năm hiện tại")
      
        
    @api.depends('start_date', 'end_date')
    def _compute_hour_of_work(self):
        for r in self:
            if r.end_date and r.start_date:
                r.hour_of_work =  (r.end_date.day-r.start_date.day) * 8
            else: r.hour_of_work = 0
        
         
                 
    @api.depends('hour_of_work', 'time_off')
    def _compute_salary(self):
        salary_per_1hour = 30000
        for r in self:
            r.salary = (salary_per_1hour * r.hour_of_work) - (salary_per_1hour * r.time_off)
             
    @api.depends('overtime')
    def _compute_total_salary(self):
        salary_overtime = 50000
        for r in self:
            if r.overtime:
                r.total_salary = r.salary + (r.overtime * salary_overtime)
            else: 
                r.total_salary = r.salary
                
                
                
                
                
                
                
                
                
                
                         