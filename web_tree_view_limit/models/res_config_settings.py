from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    web_tree_view_limit = fields.Integer(
        related='company_id.web_tree_view_limit',
        readonly=False,
    )

    @api.onchange("web_tree_view_limit")
    def onchange_default_limit(self):
        action_window = self.env['ir.actions.act_window']
        action_window.cron_update_actions_limit()
