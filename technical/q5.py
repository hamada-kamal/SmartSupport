
# ************* the Explanations ******************

#1- create the SmartSupport model with field total_amount
#2- then create inheritSmart model that will inherit SmartSupport
#3- add new float field called taxs and the store set to True to save the value in the database
#4- in the inheritSmart model i created _calc_taxs function that loops in the self to calculate the value of taxs for each record
#5- i used the decorator @api.depends that usually used with the function fields  to calculate the taxs if the any changes happend in the field "total_amount"


  
from odoo import api, fields, models


class SmartSupport(models.Model):
    _name = 'smart.support'

    total_amount = fields.Float()


class inheritSmart(models.Model):
    _inherit = 'smart.support'

    @api.depends('total_amount')
    def _calc_taxs(self):
        for record in self:
            record.taxs = 0.05 * record.total_amount
    taxs = fields.Float(compute='_calc_taxs', string="Taxs", store=True)

