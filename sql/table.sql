
CREATE SCHEMA CW2;
GO
-- Create Route Table
CREATE TABLE CW2.Routet (
    RouteID INT PRIMARY KEY IDENTITY(1,1),
    RouteType NVARCHAR(50) NOT NULL
);

-- Create Trail Table
CREATE TABLE CW2.Trailt (
    TrailID INT PRIMARY KEY IDENTITY(1,1),
    TrailName NVARCHAR(100) NOT NULL,
    TrailSummary NVARCHAR(MAX) NULL,
    TrailDescription NVARCHAR(MAX) NULL,
    Difficulty NVARCHAR(50) NOT NULL,
    Location NVARCHAR(100) NOT NULL,
    Length DECIMAL(5,2) NOT NULL,
    ElevationGain DECIMAL(5,2) NOT NULL,
    RouteID INT NOT NULL,
    CONSTRAINT FK_Trail_Route FOREIGN KEY (RouteID) REFERENCES CW2.Route(RouteID)
);

-- Create Trail Feature Table
CREATE TABLE CW2.TrailFeaturet (
    TrailFeatureID INT PRIMARY KEY IDENTITY(1,1),
    TrailFeature NVARCHAR(100) NOT NULL
);

-- Create Link Table for Trail and Trail Features
CREATE TABLE CW2.TrailTrailFeaturet (
    TrailID INT NOT NULL,
    TrailFeatureID INT NOT NULL,
    PRIMARY KEY (TrailID, TrailFeatureID),
    CONSTRAINT FK_TrailTrailFeature_Trail FOREIGN KEY (TrailID) REFERENCES CW2.Trail(TrailID),
    CONSTRAINT FK_TrailTrailFeature_TrailFeature FOREIGN KEY (TrailFeatureID) REFERENCES CW2.TrailFeature(TrailFeatureID)
);
