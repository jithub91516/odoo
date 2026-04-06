from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    purchase_order_id = fields.Many2one(
        'purchase.order',
        string='Purchase Order',
        copy=False,
    )

    def action_create_purchase_order(self):
        self.ensure_one()

        po_lines = [(0, 0, {
            'product_id': line.product_id.id,
            'product_qty': line.product_uom_qty,
            'product_uom_id': line.product_uom_id.id,
            'price_unit': 0,
            'date_planned': fields.Datetime.now(),
            'name': line.name,
        }) for line in self.order_line if line.product_id]

        purchase_order = self.env['purchase.order'].create({
            'partner_id': self.env.company.partner_id.id,
            'order_line': po_lines,
            'origin': self.name,
            'sale_order_id': self.id,
        })

        self.purchase_order_id = purchase_order.id

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Purchase Order Created',
                'message': f'{purchase_order.name} has been created successfully.',
                'type': 'success',
                'sticky': False,
                'next': {'type': 'ir.actions.client', 'tag': 'reload'},
            },
        }

    def action_view_purchase_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'res_id': self.purchase_order_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
