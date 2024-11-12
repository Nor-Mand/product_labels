# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api

from odoo.exceptions import UserError


class PrintProductLabel(models.TransientModel):
    _name = 'print.product.label'
    _description = 'Custom print product label'
    _inherit = 'mail.thread'

    name = fields.Char(string='Print Product Label')
    # Loop on action reports template names
    format_ids = fields.Many2one(
        string="Format",
        comodel_name='ir.actions.report',
        domain=[('model','=','print.product.label.lines')],
        default='_get_product_format_ids',
    )
    selected = fields.Boolean(string='Print', default=True)
    product_ids = fields.Many2one(comodel_name='product.template')

    @api.model
    def _get_product_label_ids(self):
        res = []
        """
            /* active_model is the technical name of the model
            /* active_id is the ID of the form active record or the tree view's 
               first record.
            /* active_ids is a list that contains the selected records or just one
               element.
            /* active_domain if the action is triggered from a form view
        """

    def _prepare_report(self):
        print('Hello')

    def action_print(self):
        labels = self.format_ids.filtered(lambda l: l.selected )
        if not labels:
            raise UserError('Nothing to  print, set the labels.')
        return labels