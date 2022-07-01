import logging

from odoo import _, api, models

_logger = logging.getLogger(__name__)


class IrActionsActWindow(models.Model):

    _inherit = "ir.actions.act_window"

    @api.onchange("limit")
    def onchange_default_limit(self):
        _logger.info("ir.actions.act_window limit onchange triggered")
        action_window = self.env["ir.actions.act_window"]
        action_window.cron_update_actions_limit()

    # job method
    def _cron_update_actions_limit(self, actions):
        """Sets limits to window actions"""
        tree_limit = self.env.user.company_id.web_tree_view_limit
        for action in actions:
            action.write({"limit": tree_limit})

        return "Success"

    # job method
    def cron_update_actions_limit(self):
        """Creates a job which will set limits to window actions"""
        actions = self.env["ir.actions.act_window"].search([])

        batch_actions = list()
        interval = 100
        for x in range(0, len(actions), interval):
            batch_actions.append(actions[x : x + interval])

        for actions in batch_actions:
            job_desc = _("Assign values to actions: {}".format(actions))
            self.with_delay(description=job_desc, eta=15)._cron_update_actions_limit(
                actions
            )

        _logger.info("Cron Update Action windows limits completed")
