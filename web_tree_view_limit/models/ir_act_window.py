from odoo import api, fields, models, _
from odoo.addons.queue_job.job import job
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

    @api.multi
    @job
    def _cron_update_actions_limit(self, actions):
        for action in actions:
            action.write({
                'limit': action.default_limit
            })

        return 'Success'

    @api.multi
    @job
    def cron_update_actions_limit(self):
        actions = self.env['ir.actions.act_window'].search([])

        batch_actions = list()
        interval = 50
        for x in range(0, len(actions), interval):
            batch_actions.append(actions[x:x+interval])

        for actions in batch_actions:
            job_desc = _(
                "Assign values to actions: {}".format(actions)
            )
            self.with_delay(
                description=job_desc)._cron_update_actions_limit(actions)

        _logger.info("Cron Update Action windows limits completed")
