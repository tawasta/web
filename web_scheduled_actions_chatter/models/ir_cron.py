from odoo import fields, models


class IrCron(models.Model):
    _name = "ir.cron"
    _inherit = ["ir.cron", "mail.thread"]
    user_id = fields.Many2one(tracking=True)
    active = fields.Boolean(tracking=True)
    interval_number = fields.Integer(tracking=True)
    interval_type = fields.Selection(tracking=True)
    failure_count = fields.Integer(tracking=True)
