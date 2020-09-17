# -*- coding: utf-8 -*-

from odoo import api, fields, models

class PurchasetaxChange(models.Model):
    _inherit = 'purchase.order'




    matrial_tax=fields.Integer(string="Matrial Tax")
