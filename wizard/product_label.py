# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api


class PrintProductLabel(models.TransientModel):
    _name = 'print.product.label'
    _description = 'Custom print product label'
    _inherit = 'mail.thread'

    name = fields.Char(string='Print Product Label')
    format_ids = fields.Many2one(
        string="Format",
        comodel_name='ir.actions.report',
        domain=[('model','=','print.product.label.lines')],
        default='529'
    )