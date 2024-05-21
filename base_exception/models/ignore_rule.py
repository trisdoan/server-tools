from odoo import fields, models


class IgnoreRule(models.Model):
    _name = "ignore.rule"
    _inherit = "exception.rule"
    _description = "Ignore Rule"
    _order = "active desc, sequence asc"

    exception_ids = fields.One2many(
        "exception.rule", "ignore_rule_id", string="Exception rules"
    )
