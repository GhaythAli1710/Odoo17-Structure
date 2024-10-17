# file_name : models/model_name.py
#
# ---------- inherit existing model on same table type 'models.Model' ----------
from odoo import models


class InheritedModelName(models.Model):
    _inherit = 'inherited_model_name'


# EX: inherit model "sale.order", file_name : sale_order.py
#
# from odoo import models
#
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#
# ---------- inherit existing abstract model on same table type 'models.AbstractModel' ----------
class InheritedAbstractModelName(models.AbstractModel):
    _inherit = 'inherited_abstract_model_name'


# EX: inherit base model "hr.employee.base", file_name : hr_employee_base.py
#
# from odoo import models
#
# class HrEmployeeBase(models.AbstractModel):
#     _inherit = 'hr.employee.base'
#
#
# ---------- inherit existing transient model on same table type 'models.TransientModel' ----------
class InheritedTransientModelName(models.TransientModel):
    _inherit = 'inherited_transient_model_name'


# EX: inherit transient model "...", file_name :  ....py
#
# from odoo import models
#
# class ...(models.TransientModel):
#     _inherit = '...'
#
#
# ---------- inherit existing model from any type on new table type 'models.Model' ----------
class NewModelName(models.Model):
    _name = 'new_model_name'
    _inherit = 'inherited_model_name'  # inherited_abstract_model_name, inherited_transient_model_name
    _description = 'New Model Name'


# EX1: inherit model "sale.order" in new model "custom", file_name : sale_custom.py
#
# from odoo import models
#
# class SaleCustom(models.Model):
#     _name = 'sale.custom'
#     _inherit = 'sale.order'
#     _description = 'Sale Custom'
#
#
# ---------- inherits existing model from any type on new table type 'models.Model' with synchronized values ----------
class NewSyncModelName(models.Model):
    _name = 'new_sync_model_name'
    _inherits = 'inherited_model_name'  # inherited_transient_model_name
    _description = 'New Sync Model Name'

# EX1: inherits model "sale.order" in new model "sync", file_name : sale_sync.py
#
# from odoo import models
#
# class SaleSync(models.Model):
#     _name = 'sale.sync'
#     _inherits = 'sale.order'
#     _description = 'Sale Sync'
#
