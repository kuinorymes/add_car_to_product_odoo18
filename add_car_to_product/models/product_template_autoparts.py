from odoo import models, fields


class ProductTemplateAutoparts(models.Model):
    _inherit = "product.template"

    is_autoparts = fields.Boolean(string="Is autopart", store=True)