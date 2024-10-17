from odoo import models, fields


class ModelName(models.Model):
    _inherit = 'inherited_model_name'

    #
    existing_field_name = fields.FieldType(
        attribute_name="New_value"
    )
