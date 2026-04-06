# Sale Purchase Link

A custom Odoo 19.0 module that adds a direct link between Sales Orders and Purchase Orders.

## Features

### Create Purchase Order from Sales Order

- A **"Create PO"** button appears on the Sales Order form once the order is saved.
- Clicking the button automatically creates a Purchase Order with the same products and quantities from the Sales Order.
- A success notification is shown after creation, and the page refreshes automatically.
- The button is hidden after a Purchase Order has already been created (assuming 1:1 relationship).

### Smart Buttons (Bonus)

- **Sales Order → Purchase Order**: A "Purchase" smart button appears on the SO form after a PO is created. Clicking it navigates directly to the linked Purchase Order.
- **Purchase Order → Sales Order**: A "Sales Order" smart button appears on the PO form. Clicking it navigates back to the originating Sales Order.
