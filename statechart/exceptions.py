# Copyright 2016-2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.exceptions import UserError


class NoTransitionError(UserError):
    pass
