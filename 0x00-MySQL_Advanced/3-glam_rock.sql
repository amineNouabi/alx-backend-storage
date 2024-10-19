-- SQL Script that lists all bands with 'glam rock' as their main style.
-- ranked by their longevity.
SELECT band_name, (2022 - formed) AS lifespan
FROM metal_bands
WHERE LOWER(style) LIKE '%glam rock%'
ORDER BY lifespan DESC;
