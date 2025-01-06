CREATE PROCEDURE CW2.InsertTrail
    @TrailName NVARCHAR(100),
    @TrailSummary NVARCHAR(MAX),
    @TrailDescription NVARCHAR(MAX),
    @Difficulty NVARCHAR(50),
    @Location NVARCHAR(100),
    @Length DECIMAL(5, 2),
    @ElevationGain DECIMAL(5, 2),
    @RouteID INT
AS
BEGIN
    INSERT INTO CW2.Trail (TrailName, TrailSummary, TrailDescription, Difficulty, Location, Length, ElevationGain, RouteID)
    VALUES (@TrailName, @TrailSummary, @TrailDescription, @Difficulty, @Location, @Length, @ElevationGain, @RouteID);

    PRINT 'Trail created successfully';
END;
