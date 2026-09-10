from odoo import api, models


class Base(models.AbstractModel):
    _inherit = "base"

    @api.model
    def _mail_get_company_field(self):
        res = super()._mail_get_company_field()
        if (
            self._name in ["sale.order", "account.move", "purchase.order"]
            and "report_company_id" in self._fields
        ):
            return "report_company_id"
        return res
