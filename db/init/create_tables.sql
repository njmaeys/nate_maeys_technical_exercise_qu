-- Brands
CREATE TABLE brands (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Locations
CREATE TABLE locations (
    id UUID PRIMARY KEY,
    organization_id UUID NOT NULL,
    name VARCHAR(255) NOT NULL
);

-- Electric Sensors
CREATE TABLE electric_sensors (
    id UUID PRIMARY KEY,
    duid VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    location_id UUID NOT NULL,
    FOREIGN KEY (location_id) REFERENCES locations(id)
);

-- Circuits
CREATE TABLE circuits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sensor_id UUID NOT NULL,
    name VARCHAR(255) NOT NULL,
    circuit_number INTEGER NOT NULL,
    FOREIGN KEY (sensor_id) REFERENCES electric_sensors(id)
);

-- Organizations
CREATE TABLE organizations (
    id UUID PRIMARY KEY,
    brand_id UUID NOT NULL,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (brand_id) REFERENCES brands(id)
);


