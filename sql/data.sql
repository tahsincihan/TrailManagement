INSERT INTO CW2.Trail (TrailName, TrailSummary, TrailDescription, Difficulty, Location, Length, ElevationGain, RouteID)
VALUES
    ('Sunny Forest', 'A scenic loop trail with forest views', 'An easy loop trail perfect for families.', 'Easy', 'Plymouth', 3.50, 150.00, 1),
    ('Mountain Ridge', 'A challenging out-and-back trail with mountain views', 'A difficult trail with steep inclines.', 'Hard', 'Exeter', 6.00, 400.00, 2),
    ('Coastal Walk', 'A gentle point-to-point trail along the coast', 'Trail with stunning ocean views.', 'Moderate', 'Torquay', 4.50, 120.00, 3),
    ('Riverbank Path', 'A family-friendly trail along the river', 'A gentle riverside path with picnic spots.', 'Easy', 'Dawlish', 2.80, 50.00, 1),
    ('Highland Trek', 'A challenging mountain hike', 'Steep and rocky, but worth the views.', 'Hard', 'Teignmouth', 7.00, 500.00, 2);

-- Insert into Trail Feature Table
INSERT INTO CW2.TrailFeature (TrailFeature)
VALUES
    ('Waterfall'),
    ('Wildflowers'),
    ('Rocky Path'),
    ('Picnic Spot'),
    ('Ocean View'),
    ('Mountain Summit'),
    ('Historical Landmark');

-- Insert into Link Table (Trail to Features)
INSERT INTO CW2.TrailTrailFeature (TrailID, TrailFeatureID)
VALUES
    (1, 2), -- Sunny Forest has Wildflowers
    (2, 3), -- Mountain Ridge has Rocky Path
    (2, 6), -- Mountain Ridge has Mountain Summit
    (3, 5), -- Coastal Walk has Ocean View
    (4, 4), -- Riverbank Path has Picnic Spot
    (5, 6), -- Highland Trek has Mountain Summit
    (5, 3); -- Highland Trek has Rocky Path
