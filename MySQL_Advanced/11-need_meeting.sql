-- Creates a view need_meeting that lists students who need a meeting
-- Students scoring under 80 with no last meeting, or a last meeting older than one month
CREATE VIEW need_meeting AS
SELECT name FROM students WHERE score < '80' AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
