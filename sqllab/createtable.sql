DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate text,
  quaketime time with time zone,
  quakedepth real,
  mag real,
  magType text,
  place text,
  quaketype text
);