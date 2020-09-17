# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchasetaxChange(models.Model):
    _inherit = 'purchase.order'

    tax_one = fields.Integer(string=" Tax 1")
    tax_two = fields.Integer(string=" Tax 2")
    tax_three = fields.Integer(string=" Tax 3")
    tax_four = fields.Integer(string=" Tax 4")
    tax_five = fields.Integer(string=" Tax 5")

