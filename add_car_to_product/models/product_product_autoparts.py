from odoo import api, fields, models


class ProductProductAutoparts(models.Model):
    _inherit = "product.product"

    is_autoparts = fields.Boolean(
        string="Is autopart",
        related="product_tmpl_id.is_autoparts",
        store=True
    )
    compatible_vehicle_ids = fields.Many2many(
        comodel_name="fleet.vehicle.model",
        relation="product_compatible_vehicle_rel",
        column1="product_id",
        column2="vehicle_model_id",
        string="Compatible Vehicles",
    )
    for_all_models = fields.Boolean(string="Fits All Models")
    oem = fields.Char(string="OEM")
    ovoko_part_id = fields.Char(string="Ovoko Part ID")

    vehicle_info = fields.Char(
        string="Vehicle Info",
        compute="_compute_vehicle_info",
        store=True,
    )

    @api.depends("compatible_vehicle_ids")
    def _compute_vehicle_info(self):
        for record in self:
            if record.compatible_vehicle_ids:
                vehicle = record.compatible_vehicle_ids[0]

                year_range = ""
                if vehicle.model_year_from and vehicle.model_year_to:
                    year_range = f"{vehicle.model_year_from} - {vehicle.model_year_to}"
                elif vehicle.model_year_from:
                    year_range = f"{vehicle.model_year_from} - ..."
                elif vehicle.model_year_to:
                    year_range = f"... - {vehicle.model_year_to}"

                parts = filter(
                    None,
                    [
                        vehicle.brand_id.name,
                        vehicle.name,
                        vehicle.model_type,
                        year_range,
                    ],
                )
                record.vehicle_info = " ".join(parts)
            else:
                record.vehicle_info = ""