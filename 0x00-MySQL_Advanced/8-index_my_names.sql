-- Optimize simple search by first letter

CREATE INDEX idx_name_first ON names (name(1));