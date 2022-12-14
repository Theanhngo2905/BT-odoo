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
    
    
    
    #th???c h??nh unlink()
    def unlink_test(self):
        #kh??ng truy???n v??o tham s???, kh??ng tr??? v???, 
        #d??ng ????? x??a 1 ho???c nhi???u records 
        self.unlink()
        
        
        
    #th???c h??nh h??m filter()
    def filter_test(self):
        #h??m filterd truy???n v??o func ????? l???c 1 record trong 1 recordset, v?? record c???n th???a m??n ??k trong func
        #filtered_domain th?? truy???n v??o domain, record c???n t??m ph???i th???a m??n ??k to??n t??? trong domain
        
        items = self.env['item'].search([]) 
        
        items_filter = items.filtered_domain([('state', '=','new')])
        for i in items_filter:
            print(i.item_level)
  

    #th???c h??nh h??m browse([ids])
    def browse_test(self):
        
        #tr??? v??? 1 recordset c??c record d???a theo ds ids truy??n v??o c???n t??m
        for r in self:
            a = r.id
            item_browse = r.env['item'].browse(a).mapped('name')
            print(item_browse)
        
        
    #th???c h??nh h??m write([vals])=>bool
    def write_test(self):
        #c???p nh???t t???t c??? record trong recordset hi???n t???i vs gi?? tr??? m???i mong mu???n 
        items_write = self.env['item'].browse([1,2,3,4]).write({'name':'trouser', 'mota': 'fasshion week paris'})
        print(items_write)
        
        
    #th???c h??nh h??m copy()
    # def copy_test(self):
    #     for i in self:
    #         b = i.id
    #         items_copy = i.env['item'].browse([b]).copy({})
    #         print(items_copy)
        
    
    
    #th???c h??nh h??m name_create()
    def name_create_test(self):
            item_name_create = self.env['item'].name_create({'name':'t-shirt'})
            print(item_name_create)
        
    
    
    #th???c h??nh h??m name_search([limit=100, name,arg])
    def search_test(self):
        for r in self:
            #
            item_search = r.env['item'].search([('color', '=', 'den')], offset=None, limit=12, order='name_of_product')
            print(item_search)
        
        
    #th???c h??nh h??m search_count()
    def search_count_test(self):
        for r in self:
            #n???u search_count truy???n v??o 1 list r??ng n?? s??? tr??? v??? t???ng s??? b???n ghi c???a model hi???n c??
            item_search_count = r.env['item'].search_count([('color', '=', 'den')])
            print(item_search_count)
    
    
    #th???c h??nh h??m search_name()
    def search_name_test(self):
        for r in self:
            item_search_name = r.env['item'].name_search()
            print(item_search_name)
        
    
    
    #th???c h??nh h??m read([field])
    # def read_test(self):
    #     #tham s??? truy???n v??o l?? 1 list c??c field mu???n read
    #     #tr??? v??? 1 list c??c dict g???m key v?? c??c gi?? tr??? t????ng ???ng, m???i dict l?? 1 record
    #     for r in self:
    #         item_read = r.env['item'].browse([2,4,6,8]).read(['name', 'type'])
    #         print(item_read)
    
    
    #th???c h??nh h??m read_group([domain, fields,groupby,offset=None,limit=None,orderby=False,lazy=True])
    def read_group_test(self):
        for r in self:
            item_read_group = r.env['item'].read_group([], ['name', 'type', 'size'], groupby=['name'])
            print(item_read_group)
    
    
    
    
    #th??c h??nh h??m fields_get([fields],[attribute])
    def field_get_test(self):
        for r in self:
            item_field_get = r.env['item'].fields_get(['name', 'item_level', 'item_id'])
            print(item_field_get)
        
        
    #th???c h??nh h??m fields_view_get([view_id/view_type='form'])
    def field_view_get(self):
        for r in self:
            item_field = r.env['item'].fields_view_get(view_id=8)
            print(item_field)
     
        
    #th???c h??nh h??m sorted(key=None, reserve=False)
    def sort_test(self):
        #s???p x???p recordset theo th??? t??? c???a key
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
       
     
    
     
         