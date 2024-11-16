
-- Query to create materialized view for current lube stock
CREATE MATERIALIZED VIEW api_current_lube_stock AS
SELECT 
    p.id AS product_id,
    p.name AS product_name,
    COALESCE(SUM(si.quantity) - COALESCE(SUM(dls.quantity), 0), 0) AS remaining_stock,
    p.price AS price_per_item,
    (COALESCE(SUM(si.quantity) - COALESCE(SUM(dls.quantity), 0), 0) * p.price) AS total_value
FROM 
    api_product p
LEFT JOIN 
    api_stockinventory si ON p.id = si.product_id
LEFT JOIN 
    api_dailylubesales dls ON p.id = dls.product_id
WHERE 
    p.is_active = TRUE AND p.is_fuel = FALSE
GROUP BY 
    p.id, p.name, p.price;


-- Query to create trigger function to refresh materialized view
CREATE OR REPLACE FUNCTION refresh_api_current_lube_stock()
RETURNS TRIGGER AS $$
BEGIN
    REFRESH MATERIALIZED VIEW api_current_lube_stock;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;


-- Query to create triggers to refresh materialized view
CREATE TRIGGER refresh_api_current_lube_stock_on_stockinventory
AFTER INSERT OR UPDATE OR DELETE ON api_stockinventory
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_api_current_lube_stock();


CREATE TRIGGER refresh_api_current_lube_stock_on_dailylubesales
AFTER INSERT OR UPDATE OR DELETE ON api_dailylubesales
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_api_current_lube_stock();


CREATE TRIGGER refresh_api_current_lube_stock_on_product
AFTER INSERT OR UPDATE OR DELETE ON api_product
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_api_current_lube_stock();


-- Query to create indexes
CREATE INDEX idx_api_current_lube_stock_product_id ON api_current_lube_stock (product_id);



-- Drop all

-- Drop Triggers
DROP TRIGGER IF EXISTS refresh_api_current_lube_stock_on_stockinventory ON api_stockinventory;
DROP TRIGGER IF EXISTS refresh_api_current_lube_stock_on_dailylubesales ON api_dailylubesales;
DROP TRIGGER IF EXISTS refresh_api_current_lube_stock_on_product ON api_product;

-- Drop Function
DROP FUNCTION IF EXISTS refresh_api_current_lube_stock();

-- Drop Materialized View
DROP MATERIALIZED VIEW IF EXISTS api_current_lube_stock;
