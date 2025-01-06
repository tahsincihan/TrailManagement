CREATE PROCEDURE CW2.GetAllTrails
AS
BEGIN
    SELECT t.TrailID, t.TrailName, t.Difficulty, r.RouteType, t.Length, t.ElevationGain, t.Location
    FROM CW2.Trail t
    JOIN CW2.Route r ON t.RouteID = r.RouteID;
END;
