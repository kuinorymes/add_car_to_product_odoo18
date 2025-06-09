from odoo import models, fields, api


class FleetVehicleModel(models.Model):
    _inherit = "fleet.vehicle.model"

    model_year_from = fields.Integer("Year from")
    model_year_to = fields.Integer("Year to")
    model_type = fields.Char("Model type")
    volume = fields.Many2one("vehicle.engine.volume", string="Volume")
    ovoko_car_id = fields.Char("Ovoko Car ID")

    years_of_release = fields.Char(
        string="Years Of Release",
        compute="_compute_years_of_release",
        store=False,
    )

    @api.depends("model_year_from", "model_year_to")
    def _compute_years_of_release(self):
        for record in self:
            if record.model_year_from and record.model_year_to:
                record.years_of_release = f"{record.model_year_from} - {record.model_year_to}"
            elif record.model_year_from:
                record.years_of_release = str(record.model_year_from)
            elif record.model_year_to:
                record.years_of_release = str(record.model_year_to)
            else:
                record.years_of_release = ""