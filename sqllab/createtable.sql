DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate date,
  quaketime text,
  quakedepth real,
  mag real,
  magType text,
  place text,
  quaketype text
);