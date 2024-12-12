# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    save_money = fields.Float(
        string="Quanto Tenere Da Parte",
        store=True,
        readonly=True,
        compute="_compute_save_money",)
    

    @api.depends("amount_total_signed")
    def _compute_save_money(self):
        for record in self:
            record.save_money = (record.amount_total_signed * 35)/100