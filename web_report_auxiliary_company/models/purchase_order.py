from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    aux_company_id = fields.Many2one("res.company", string="Auxiliary Company")

    report_company_id = fields.Many2one(
        "res.company",
        compute="_compute_report_company_id",
    )

    @api.depends("company_id", "aux_company_id")
    def _compute_report_company_id(self):
        for order in self:
            order.report_company_id = order.aux_company_id or order.company_id

    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super()._prepare_invoice()
        if self.aux_company_id:
            invoice_vals["aux_company_id"] = self.aux_company_id.id

        return invoice_vals

    def _prepare_picking(self):
        self.ensure_one()
        picking_vals = super()._prepare_picking()
        if self.aux_company_id:
            picking_vals["aux_company_id"] = self.aux_company_id.id

        return picking_vals

    def action_rfq_send(self):
        res = super(
            PurchaseOrder, self.with_company(self.report_company_id)
        ).action_rfq_send()
        return res
