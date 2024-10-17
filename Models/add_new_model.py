# file_name : models/model_name.py
#
# ---------- Add new model ----------
#
from odoo import models


class ModelName(models.Model):
    _name = 'model.name'
    _description = 'Model Name'


# EX: Add new model "commission", file_name : commission_commission.py
#
# from odoo import models
#
# class CommissionCommission(models.Model):
#     _name = 'commission.commission'
#     _description = 'Commission'
#
#
# ---------- Add New Abstract Model ---------- Prepare Review
#
class AbstractModelName(models.AbstractModel):
    _name = 'model.name.base'
    _auto = True  # automatically create database backend
    _abstract = False  # not abstract


# EX: Add new abstract model "commission.commission.base", file_name : commission_commission_base.py
#
# from odoo import fields, models
#
# class CommissionCommissionBase(models.AbstractModel):
#     _name = 'commission.commission.base'
#
#
# ---------- Add New Transient Model ---------- Prepare Review
#
class TransientModelName(models.TransientModel):
    _name = 'model.name.wizard'
    _auto = True  # automatically create database backend
    _register = False  # not visible in ORM registry, meant to be python-inherited only
    _abstract = False  # not abstract
    _transient = True  # transient
    _transient_max_count = "number"
    _transient_max_hours = "number"

# EX: Add new model "ConfirmSaleTrust", file_name : sale_confirm_trust.py
#
# from odoo import fields, models
#
# class ConfirmSaleTrust(models.TransientModel):
#     _name = 'sale.trust.wizard'
#     _transient_max_count = 0
#     _transient_max_hours = 1.0
#
#     order_id = fields.Many2one('sale.order', string='Sale Order')
#     partner_id = fields.Many2one('res.partner', string='Customer', related='order_id.partner_id')
#
#     def approve_blacklisted_customer_order(self):
#         self.order_id.with_context({'approve_blacklisted_customer_order': 1}).action_confirm()
#
#
