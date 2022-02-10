from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)


class IrActionsActWindow(models.Model):

    _inherit = "ir.actions.act_window"

    default_limit = fields.Integer()

    @api.multi
    @api.onchange("limit")
    def onchange_default_limit(self):
        _logger.info("ir.actions.act_window limit onchange triggered")
        for record in self:
            record.limit = record.default_limit
