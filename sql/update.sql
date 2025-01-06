CREATE PROCEDURE CW2.UpdateTrail
    @TrailID INT,
    @TrailName NVARCHAR(100),
    @TrailDescription NVARCHAR(MAX)
AS
BEGIN
    UPDATE CW2.Trail
    SET TrailName = @TrailName, TrailDescription = @TrailDescription
    WHERE TrailID = @TrailID;
END;
