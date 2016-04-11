# -*- coding: utf-8 -*-
#    OpenERP, Open Source Management Solution
#    Copyright (c) Rooms For (Hong Kong) Limited T/A OSCG. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp.osv import fields, osv

class res_company(osv.osv):
    _inherit = "res.company"
    _columns = {
        'months': fields.integer("Number of months to consider in Product Proc. Info Update", required=True),
    }

    _defaults = {
        'months': 6,
    }

res_company()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
