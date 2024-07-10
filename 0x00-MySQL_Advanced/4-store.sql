-- Creates a trigger that decreases the quantity of an item when an order is placed

CREATE TRIGGER dec_q AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;