# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchasetaxChange(models.Model):
    _inherit = 'purchase.order'

    tax_one = fields.Monetary(string=" Tax 1")
    tax_two = fields.Monetary(string=" Tax 2")
    tax_three = fields.Monetary(string=" Tax 3")
    tax_four = fields.Monetary(string=" Tax 4")
    tax_five = fields.Monetary(string=" Tax 5")

