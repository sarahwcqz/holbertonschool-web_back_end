-- Creates a trigger that resets valid_email only when the email has been changed
DELIMITER $$
-- Before each update on users, set valid_email to 0 if the new email differs
CREATE TRIGGER email_validation
BEFORE UPDATE ON users
FOR EACH ROW
IF OLD.email <> NEW.email THEN
    SET NEW.valid_email = 0;
END IF$$
DELIMITER ;
