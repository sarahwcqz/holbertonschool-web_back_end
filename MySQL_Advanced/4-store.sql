-- Creates a trigger that decreases the quantity of an item after adding a new order
-- After each insert in orders, remove the ordered number from the item's quantity
CREATE TRIGGER remove_item
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
