-- Creates a function SafeDiv that divides the first number by the second, or returns 0 if the second is 0
DELIMITER $$
-- Return 0 when b is 0 to avoid a division by zero, otherwise return a / b
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a/b;
    END IF;
END$$
DELIMITER ;
