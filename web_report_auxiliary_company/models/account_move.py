from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    aux_company_id = fields.Many2one("res.company", string="Auxiliary Company")

    report_company_id = fields.Many2one(
        "res.company",
        compute="_compute_report_company_id",
    )

    @api.depends("company_id", "aux_company_id")
    def _compute_report_company_id(self):
        for move in self:
            move.report_company_id = move.aux_company_id or move.company_id

    def action_invoice_sent(self):
        res = super(
            AccountMove, self.with_company(self.report_company_id)
        ).action_invoice_sent()
        return res
