-- Lists all bands with Glam rock as their main style, ranked by their longevity
-- Bands still active (split is NULL) are counted up to 2024, longest first
SELECT band_name, IFNULL(split, 2024) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
