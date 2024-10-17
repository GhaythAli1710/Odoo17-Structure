from odoo import models, fields, api


class ModelName(models.Model):
    #
    field_m2o_id = fields.Many2one(
        comodel_name='target_model_name',
        string="field_name",
        ondelete="action",
        #
        domain=[('filtered_field_name', 'operator', None), ],
        context={'ctx_field_name': None},
        check_company=False,
    )
    # ondelete action options {'set null', 'restrict', 'cascade'}
    #
    # domain="[('field_name', 'operator', value)]"
    # To filter relational object fields records
    #
    # context={'field_name' : value}
    # use to set default value
    #
    # check_company=bool
    # Mark the field to be verified in _check_company()
    #
    # EX:
    # partner_id = fields.Many2one(
    #     comodel_name='res.partner',
    #     string='Account Holder',
    #     domain=['|', ('is_company', '=', True), ('parent_id', '=', False)],
    #     context={'partner_id': partner_id},
    #     check_company = True,
    #     ondelete="restrict"
    # )
    #
    field_o2m_ids = fields.One2many(
        comodel_name='target_model_name',
        inverse_name='relation_field_id',
        string="field_name",
        ondelete="action"
    )
    #
    field_m2m_ids = fields.Many2many(
        comodel_name='target_model_name',
        relation='table_name',
        column1='column1_name',
        column2='column2_name',
        string="field_name",
        ondelete="action"
    )
    #
    field_select = fields.Selection(
        selection=[
            ('option1_value', "option1_label"),
        ],
        ondelete="action",
        #
        string="field_name",
        help="help_text",
        invisible=False,
        readonly=False,
        required=False,
        default="option1_label"
    )
    # SELECTION_OPTION = [
    #     ('option1_value', "option1_label"),
    #     ('option2_value', "option2_label"),
    #     ('option2_value', "option3_label"),
    # ]
    #
    # ondelete action options {'set null', 'cascade', 'set default', 'set option1_value'}
    #
    field_bool = fields.Boolean(
        string="field_name",
        help="help_text",
        invisible=False,
        readonly=False,
        required=False,
        default=False
    )
    #
    field_int = fields.Integer(
        string="field_name",
        help="help_text",
        invisible=False,
        readonly=False,
        required=False,
        default=0
    )
    #
    field_float = fields.Float(
        string="field_name",
        help="help_text",
        invisible=False,
        readonly=False,
        required=False,
        default=0.00
    )
    #
    field_char = fields.Char(
        size="maximum_of_chars_size",
        translate=True,
        #
        string="field_name",
        help="help_text",
        invisible=False,
        readonly=False,
        required=False,
        default="empty_char"
    )
    #
    field_text = fields.Text(
        translate=True,
        #
        string="field_name",
        help="help_text",
        invisible=False,
        readonly=False,
        required=False,
        default="empty_text"
    )
    #
    field_binary = fields.Binary(
        string="field_name",
        help="help_text",
        invisible=False,
        required=False,
        default=None
    )
    #
    field_date = fields.Date(
        string="field_name",
        help="help_text",
        invisible=False,
        readonly=False,
        required=False,
        default=""
    )
    # default
    #
    field_date_time = fields.Datetime(
        string="field_name",
        help="help_text",
        invisible=False,
        readonly=False,
        required=False,
        default=""
    )
    # default
    #
    # ****************************************************************
    #
    # ----------------------- Extra attributes -----------------------
    #
    # company_dependent=bool,
    #  the field value is dependent of the current company;
    #  the value isn’t stored on the model table. It is registered as ir.property
    #
    # copy=bool,
    #
    # store=bool,
    #
    # index=bool,
    #
    # tracking=bool
    #
    # groups="group_external_id"
    # use groups to restrict field access rights
    #
    # compute='_compute_field_name'
    # inverse='_inverse_field_name'
    # search='_search_field_name'
    #
    field_compute = fields.FieldType(
        string="field_name",
        compute='_compute_field_name',
        inverse='_inverse_field_name',
        search='_search_field_name',
        store=True,
        readonly=True,
        copy=False,
        index=True,
        tracking=True,
        company_dependent=True,
        groups="base.group_user"
    )

    @api.depends('depend_field_name')
    def _compute_field_name(self):
        return self

    def _inverse_field_name(self):
        return self

    def _search_field_name(self, operator, value):
        return [('field_compute', operator, value)]

    #
    # Other compute type
    field_compute2 = fields.FieldType(
        related='related_field_name', store=True,
        depends=['depend_field_name'])
    #
    # EX :
    # nickname = fields.Char(
    #     related='partner_id.name', store=True,
    #     depends=['partner_id'])
    #
