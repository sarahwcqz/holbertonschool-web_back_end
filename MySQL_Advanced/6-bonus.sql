-- Creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER $$
-- Create the project if it does not exist yet, then add the correction with its id
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE proj_id INT;
    IF NOT EXISTS (SELECT name, id FROM projects WHERE name = project_name) THEN
        INSERT INTO projects SET name = project_name;
    END IF;
    SELECT id INTO proj_id FROM projects WHERE name = project_name;
    INSERT INTO corrections SET corrections.user_id = user_id, project_id = proj_id, score = score;
END$$
DELIMITER ;
