-- Ranks country origins of bands by their total number of (non-unique) fans
-- Sum the fans of all bands from each origin, biggest total first
SELECT origin,
SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
