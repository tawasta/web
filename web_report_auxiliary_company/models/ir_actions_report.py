from odoo import models


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    def _render_qweb_html(self, report_ref, docids, data=None):
        context = data.get("context", False)
        active_model = context and context.get("active_model") or False
        if (
            active_model
            in ["account.move", "sale.order", "stock.picking", "purchase.order"]
            and "aux_company_id" in self.env[active_model]._fields
        ):
            return super(
                IrActionsReport, self.with_context(use_aux_company=True)
            )._render_qweb_html(
                report_ref=report_ref,
                docids=docids,
                data=data,
            )
        else:
            return super()._render_qweb_html(
                report_ref=report_ref,
                docids=docids,
                data=data,
            )
