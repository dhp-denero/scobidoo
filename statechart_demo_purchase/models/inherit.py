# Copyright 2016-2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class GrandParent(models.AbstractModel):
    _name = 'test.inherit.grand.parent'
    _inherit = 'statechart.mixin'

    name = fields.Char()


class Parent(models.Model):
    _inherit = 'test.inherit.grand.parent'
    _name = 'test.inherit.parent'
    _statechart_file = \
        'statechart_demo_purchase/models/statechart_parent_demo.yml'

    def button_parent_method(self):
        pass


class Child1(models.Model):
    _name = 'test.inherit.child1'
    _inherit = 'test.inherit.parent'

    def button_parent_method(self):
        return super(Child1, self).button_parent_method()


class Child2(models.Model):
    _name = 'test.inherit.child2'
    _inherit = 'test.inherit.parent'
