from odoo import models,fields,api
import time
import datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import date_utils

class Manager(models.Model):
    _name = 'manager'
    _description = 'Manager'

    
    name = fields.Char(string="Name", invisible=True)
    position = fields.Char(string = "Position")
    age = fields.Date(string="Day of birth")
    attendance_time_start = fields.Datetime(string='Check in')
    attendance_time_end = fields.Datetime(string='Check out')
    time_late = fields.Char(string="Arrival hours late", compute="_compute_time_late", readonly=True)
    
   
    year_kl = fields.Date(string="Year")
    present = fields.Date()
   
        
    @api.depends('attendance_time_start','attendance_time_end')
    def _compute_time_late(self):
        for r in self:
            if r.attendance_time_end and r.attendance_time_start:
                # attendance_time_start = fields.Datetime.to_datetime(r.attendance_time_start)
                # attendance_time_end = fields.Datetime.to_datetime(r.attendance_time_end)
                timelate = r.attendance_time_end - r.attendance_time_start
                r.time_late = timelate
            else: 
                r.time_late = ''
                
    
    @api.onchange('year_kl')  
    def test_add_date(self):
        if self.year_kl:
            self.present = fields.Date.add(self.year_kl,months=10)
    

    #thực hành to_date, end_of, start_of
    @api.onchange('year_kl') 
    def test_date(self):
        date_today = fields.Date.to_date('2022-06-01')  #định dạng "%Y,%m,%d"
        start_date = date_utils.start_of(date_today, 'week')
        end_date = date_utils.end_of(date_today, 'week')
        print(start_date)
        print(end_date)
        
        
    @api.onchange('year_kl')
    def test_to_string(self):
        date_today = fields.Date.to_string(fields.Date.context_today(self))
        print(date_today)
            
            
            
            
            
            
     
     
     
     
     
        
        
        