from odoo import models,fields,api
 
class Customer(models.Model):
    _name = 'customer'
    _description = 'Customer'
    
    name = fields.Char(string="Khách hàng", required=True)
    phone = fields.Char(string="Số điện thoại", size=10, trim=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Giới tính")
    address = fields.Char(string="Địa chỉ")
    product_ids = fields.Many2many('item', string="Sản phẩm đã mua")
    payment = fields.Integer(compute="_compute_payment", string="Tổng tiền")
     
     
     
     #hàm mapped
    @api.depends('product_ids')
    def _compute_payment(self):
        for r in self:
            r.payment = sum(r.product_ids.mapped('price'))
            
            
            
    #thực hành hàm filter truyền vào func trả về recordset thỏa mãn đk của func
    def filter_test(self):
        customer_1 = self.env['customer'].search([]).filtered(lambda customer: customer.gender == 'male')  
        for i in customer_1:
            print(i.name)
            
            
    def find_customer(self):
        Customer_0 = self.env['customer']
        domain = ['&', ('gender', '=', 'female'), ('name', 'ilike','Linh')] 
        customes = Customer_0.search(domain)   
            
        
    def mapped_test(self):
        customer_2 = self.env['customer'].search([]).mapped(lambda customers: (customers.name, customers.payment))
        print(customer_2)
        
        
    def sorted_test(self):
        #sắp xếp recordset theo thứ tự của key
        #nếu k truyền gì thì trả về id của các bản ghi
        customer_3 = self.env['customer'].search([]).sorted(key=None)
        print(customer_3)
           
    
    
    #thực hanh truy cập bản ghi thông qua truy vấn cơ sở dữ liệu (self._cr.execute)
    def test_execute(self):
        self.flush()
        self._cr.execute("SELECT id, name, gender FROM customer WHERE gender = 'male'")
        data = self._cr.fetchall() 
        #kiểu trả về sẽ định dạng list of tuple, nếu muốn trả vể list of dict thì dùng hàm dictfetchall()
        #nếu muốn trả về một bản ghi thì dùng fetchone() hoặc dictfetchone()
        print(data)
        
        
        
        
        
        
        
        
        
          
        
            