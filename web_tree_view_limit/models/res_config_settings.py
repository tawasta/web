from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    web_tree_view_limit = fields.Integer(
        related='company_id.web_tree_view_limit',
        readonly=False,
    )

    @api.multi
    def write(self, values):
        res = super(ResConfigSettings, self).write(values)
        limit = self.web_tree_view_limit
        actions = self.env['ir.actions.act_window'].search([])
        for action in actions:
            if 'tree' in action.view_mode:
                action.limit = limit
                action.default_limit = limit
        return res
