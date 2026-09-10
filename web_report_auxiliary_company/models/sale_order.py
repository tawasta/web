from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    aux_company_id = fields.Many2one("res.company", string="Auxiliary Company")

    report_company_id = fields.Many2one(
        "res.company",
        compute="_compute_report_company_id",
    )

    @api.depends("company_id", "aux_company_id")
    def _compute_report_company_id(self):
        for order in self:
            order.report_company_id = order.aux_company_id or order.company_id

    def action_confirm(self):
        res = super().action_confirm()

        if self.aux_company_id:
            for pick in self.picking_ids:
                pick.write({"aux_company_id": self.aux_company_id.id})

        return res

    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super()._prepare_invoice()
        if self.aux_company_id:
            invoice_vals["aux_company_id"] = self.aux_company_id.id

        return invoice_vals

    def action_quotation_send(self):
        res = super(
            SaleOrder, self.with_company(self.report_company_id)
        ).action_quotation_send()
        return res
