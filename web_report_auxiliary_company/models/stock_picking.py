from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    aux_company_id = fields.Many2one("res.company", string="Auxiliary Company")

    report_company_id = fields.Many2one(
        "res.company",
        compute="_compute_report_company_id",
    )

    @api.depends("company_id", "aux_company_id")
    def _compute_report_company_id(self):
        for picking in self:
            picking.report_company_id = picking.aux_company_id or picking.company_id
