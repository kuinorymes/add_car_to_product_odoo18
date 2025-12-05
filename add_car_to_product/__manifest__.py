{
    "name": "Add Car To Product",
    "version": "1.0.0",
    "summary": "Add car to product",
    "description": "Allows to add car to product",
    "category": "Custom",
    "depends": ["base", "fleet", "product"],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/product_product_view.xml",
        "views/product_product_autoparts_views.xml",
        "views/fleet_vehicle_model_views.xml",
        "views/product_template_autopart_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
