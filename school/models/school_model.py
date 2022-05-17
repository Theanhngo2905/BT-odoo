from odoo import fields, models , api

from odoo.exceptions import ValidationError
class SchoolModel(models.Model):
    '''
    các trường tự động khi tạo model : id(Integer) , create_date(datetime), create_uid(many2one)
    write_date(datetime), write_uid(many2one)
    '''
    
    _name = 'school'
    # tên của bảng 
    _description = 'Danh sách trường học'
    # Nhãn của bảng
    # các fields Char,Integer,Float,Selection,Date,Datetime,Text,Binary,Image,Các trường quan hệ 
    name = fields.Char(string='Tên Trường', required=True)
    # string = 'unicode' nhãn dán hiển thị của trường
    # required=bool => có bắt buộc nhập hay không
    email = fields.Char(string='Email',required=True)
    type = fields.Selection([('private', 'Dân Lập'), ('public', 'Công Lập')], string='Loại Trường', default='public')
    # selection nhận vào 1 list các tuple với cặp giá trị key và string, selection lưu vào database với kiểu Char 
    # default => có thể nhận int , str , bool , 1 hàm nhận vào recordset trả về giá trị tương ứng
    phone = fields.Char(string='Số điện thoại')
    add = fields.Char(string='Địa chỉ', index=True)
    # index thiết lập chế dộ index cho cột đó, sql sẽ thực hiện chế độ index nhóm các giá trị theo quy luật 
    # để thực hiện tìm kiếm nhanh hơn, chỉ nên dùng ở những trường có xu hướng tìm kiếm cao 
    price = fields.Float(string='Giá tiền 1 học phần' , compute='_pricee')
    # compute là hàm tính toán lạilại
    ahihi = fields.Html(string='ahaha',default=('<h1>ahaha</h1>'))
    dated = fields.Date(string='Ngày thành lập' , compute='_datedd')
    @api.depends('create_date')
    def _datedd(self):
        for r in self:
            if r.create_date:
                
                r.dated = r.create_date
            else : r.dated = '1999-01-01'
    @api.depends('type')   
    # nếu chỉ viết hàm compute mà không viết depends() thì giá trị không được tính lại khi update giá trị mới
    # tức là chỉ tính khi tạo record mới 
    # hàm depends giúp làm việc đó
    # hàm depends hỗ trợ việc "chấm" nghĩa là chấm được đến trường của models khác qua các trường quan hệ
    # còn onchange chỉ hỗ trợ những field ở model hiện tại
    # hàm onchange chỉ se được gọi khi giá trị thay đổi trên view và 
    # hàm compute được gọi khi giá trị phụ thuộc thay đổi trong database
    # hàm onchange không cần khai báo trên field còn hàm compute thì có
    def _pricee(self):
        # self là recordset chứa các record
        # trong view form thì recordset chứa 1 record với id tương ứng
        for r in self:
            if r.type:
                if r.type == 'private':
                    r.price = 500000
                else:
                    r.price = 300000 
            else: r.price =0
    class_list = fields.One2many('class', 'school_id', string='Danh sách lớp')
    # one2many là trường ảo và không lưu trong database
    teacher_list = fields.One2many('teacher', 'school_id', string='Danh sách giang viên')
    _sql_constraints = [('name', 'unique(name)', "Tên này đã được dùng")]
    #sql constraints thực thi và thực hiện ràng buộc tai CSDL 
    #api.constraints thực hiện chặng record ngay trên server
    #nên dùng sql constrain khi các ràng buộc giữa các dữ liệu trong sql với nhau, vd kiểm tra trùng tên trùng email
    #nên dùng sql python (api.constraints) khi thực hiện các phép logic python với record đó
    #VD kiểm tra email hợp lệ
    @api.constrains('email')
    def _check_email(self):
        for r in self:
            if self.email:
                if self.filtered(lambda self: '@' not in self.email):
                    raise ValidationError(("email khong hợp lệ"))
    
        