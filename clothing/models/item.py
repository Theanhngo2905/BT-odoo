from odoo import models, fields, api


class Items(models.Model):
    _name = 'item'
    
    name = fields.Char(string="Product's name", help="name of product is different from name of sku")
    image = fields.Binary(string="Image")
    mota = fields.Text(string="Description detail", translate=True)
    type = fields.Selection([('ao', 'Shirts'), ('quan', 'Trousers'), ('chanvay', 'Skirt'), ('vay', 'Dress')], string="Type")
    size = fields.Selection([('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL')], string="Size")
    color = fields.Selection([('den', 'Black'), ('trang', 'White'), ('xanh', 'Blue'), ('do', 'Red')])
    state = fields.Selection(string="Status", selection=[('new', 'New'), ('secondhand', 'Second Hand'), ('doitra', 'Return')], default="new")
    item_level = fields.Char(states={'new': [('invisible', False), ('readonly', False)],
                                                       'secondhand': [('invisible', False), ('readonly', False), ],
                                                       'doitra': [('invisible', False), ('readonly', True)]})
    price = fields.Integer(string="Price")
    ngay_nhap_kho = fields.Date(string="Delivery date")
    item_id = fields.Many2one('clothing.management', string="Kho", ondelete='restrict')
    item_relate = fields.Char(related="item_id.name", string="relate")
    
    
    @api.model
    def is_allowed_state(self, current_state, new_state):
        allowed_states = [('new','secondhand', ('secondhand','doitra'), ('doitra','seconhand'),('new', 'doitra'))]
        return (current_state, new_state in allowed_states)
    def change_product_state(self, state):
        for product in self:
            if product.is_allowed_state(product.state, state):
                product.state = state
            else:
                continue
    def change_to_new(self):
        self.change_product_state('new')
    def change_to_secondhand(self):
        self.change_product_state('secondhand')
    def change_to_doitra(self):
        self.change_product_state('doitra')
    
    
    
    #thực hành unlink()
    def unlink_test(self):
        #không truyền vào tham số, không trả về, 
        #dùng để xóa 1 hoặc nhiều records 
        self.unlink()
        
        
        
    #thực hành hàm filter()
    def filter_test(self):
        #hàm filterd truyền vào func để lọc 1 record trong 1 recordset, và record cần thỏa mãn đk trong func
        #filtered_domain thì truyền vào domain, record cần tìm phải thỏa mãn đk toán tử trong domain
        
        items = self.env['item'].search([]) 
        
        items_filter = items.filtered_domain([('state', '=','new')])
        for i in items_filter:
            print(i.item_level)
  

    #thực hành hàm browse([ids])
    def browse_test(self):
        
        #trả về 1 recordset các record dựa theo ds ids truyên vào cần tìm
        for r in self:
            a = r.id
            item_browse = r.env['item'].browse(a).mapped('name')
            print(item_browse)
        
        
    #thực hành hàm write([vals])=>bool
    def write_test(self):
        #cập nhật tất cả record trong recordset hiện tại vs giá trị mới mong muốn 
        items_write = self.env['item'].browse([1,2,3,4]).write({'name':'trouser', 'mota': 'fasshion week paris'})
        print(items_write)
        
        
    #thực hành hàm copy()
    # def copy_test(self):
    #     for i in self:
    #         b = i.id
    #         items_copy = i.env['item'].browse([b]).copy({})
    #         print(items_copy)
        
    
    
    #thực hành hàm name_create()
    def name_create_test(self):
            item_name_create = self.env['item'].name_create({'name':'t-shirt'})
            print(item_name_create)
        
    
    
    #thực hành hàm name_search([limit=100, name,arg])
    def search_test(self):
        for r in self:
            #
            item_search = r.env['item'].search([('color', '=', 'den')], offset=None, limit=12, order='name_of_product')
            print(item_search)
        
        
    #thực hành hàm search_count()
    def search_count_test(self):
        for r in self:
            #nếu search_count truyền vào 1 list rông nó sẽ trả về tổng số bản ghi của model hiện có
            item_search_count = r.env['item'].search_count([('color', '=', 'den')])
            print(item_search_count)
    
    
    #thực hành hàm search_name()
    def search_name_test(self):
        for r in self:
            item_search_name = r.env['item'].name_search()
            print(item_search_name)
        
    
    
    #thực hành hàm read([field])
    # def read_test(self):
    #     #tham số truyền vào là 1 list các field muốn read
    #     #trả về 1 list các dict gồm key và các giá trị tương ứng, mỗi dict là 1 record
    #     for r in self:
    #         item_read = r.env['item'].browse([2,4,6,8]).read(['name', 'type'])
    #         print(item_read)
    
    
    #thực hành hàm read_group([domain, fields,groupby,offset=None,limit=None,orderby=False,lazy=True])
    def read_group_test(self):
        for r in self:
            item_read_group = r.env['item'].read_group([], ['name', 'type', 'size'], groupby=['name'])
            print(item_read_group)
    
    
    
    
    #thưc hành hàm fields_get([fields],[attribute])
    def field_get_test(self):
        for r in self:
            item_field_get = r.env['item'].fields_get(['name', 'item_level', 'item_id'])
            print(item_field_get)
        
        
    #thực hành hàm fields_view_get([view_id/view_type='form'])
    def field_view_get(self):
        for r in self:
            item_field = r.env['item'].fields_view_get(view_id=8)
            print(item_field)
     
        
    #thực hành hàm sorted(key=None, reserve=False)
    def sort_test(self):
        #sắp xếp recordset theo thứ tự của key
        for r in self:
            item_sort = r.env['item'].search([]).sorted(key='name').mapped('name')
            print(item_sort)
        
    def button_create_multi(self):
        new_item_1 = self.env['item'].create([{'name':'aa','price':'500'},{'name':'bb'}])
        print(self.env['item'])
        
        
class NewItem(models.Model):
    _inherit = 'item'  
    
    @api.model_create_multi
    def create(self,vals_list):
        for val in vals_list:
            if 'price' in val:
                val['name'] = val['name'].upper()
        return super(NewItem, self).create(vals_list)
       
     
    
     
         