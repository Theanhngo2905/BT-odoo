from odoo import fields, models, api


class StudentModel(models.Model):
    _name = 'student'
    _description = 'Danh sách học sinh'
    
    name = fields.Char(string='Tên')
    dob = fields.Date(string='Ngày sinh')
    age = fields.Integer(string='Tuổi', compute='_age')

    def _age(self):
        for r in self:
            if r.dob:
                r.age = fields.Date.today().year - r.dob.year
            else :r.age = 0
    # def write(self, vals):
    #     for r in self:
    #         if r.id == 41:
    #             print('a')
    #     return super(StudentModel, self).write(vals)
    class_idss = fields.Many2one('class')
    class_id = fields.Many2one('class', string='Lớp')
    class_compute = fields.Char(string='Trường', compute='_compute_school_id')
    school_id = fields.Char(related = 'class_id.school_id.name')
    # school_id =fields.Many2one('school',string='Trường')
    @api.depends('class_id')
    def _compute_school_id(self):
        for r in self:
            if r.class_id:
                r.class_compute = r.class_id.school_id.name
            else:
                r.class_compute = ''

    subject_list = fields.Many2many('subject', 'map_student_subject', 'student_id', 'subject_id', string='Đăng ký môn học :')
    
    tuition = fields.Float(string='HỌc phí' ,compute='_tuition')
    @api.depends('subject_list','subject_list.credit','class_id.school_id.type')
    def _tuition(self):
        for r in self:
            if r.subject_list:
                r.tuition = sum(r.subject_list.mapped('credit'))*r.class_id.school_id.price
            else:
                r.tuition=0
