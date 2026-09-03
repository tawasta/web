from odoo import api, models


class IrQweb(models.AbstractModel):
    _inherit = "ir.qweb"

    @api.model
    def _compile_expr(self, expr, **kwargs):
        """This is for t-out, t-if and others"""
        if expr and self.env.context.get("use_aux_company"):
            if "doc.company_id" in expr:
                expr = expr.replace(
                    "doc.company_id",
                    "doc.report_company_id",
                )
            if "o.company_id" in expr:
                expr = expr.replace(
                    "o.company_id",
                    "o.report_company_id",
                )

        return super()._compile_expr(expr, **kwargs)

    def _compile_directive_field(self, el, compile_context, level):
        """This is for t-field replacing"""
        field = el.get("t-field")

        if field and self.env.context.get("use_aux_company"):
            if "doc.company_id" in field:
                field = field.replace(
                    "doc.company_id",
                    "doc.report_company_id",
                )

            if "o.company_id" in field:
                field = field.replace(
                    "o.company_id",
                    "o.report_company_id",
                )
            el.set("t-field", field)

        return super()._compile_directive_field(el, compile_context, level)
