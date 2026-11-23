-- Creates an index idx_name_first_score on the table names, the first letter of name and the score
-- Index the first character of name, then the whole score within each letter
CREATE INDEX idx_name_first_score ON names (name(1), score);
