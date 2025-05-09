CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
BEGIN;
INSERT INTO brands (id,name) VALUES ('11111111-1111-1111-1111-111111111111','DemoBrand');
INSERT INTO organizations (id,brand_id,name) VALUES ('955c3c4d-3a03-4d79-9655-3871f5ad999d','11111111-1111-1111-1111-111111111111','East Franchise');
INSERT INTO organizations (id,brand_id,name) VALUES ('719aeacd-dc94-4476-874b-0d178d8c0c48','11111111-1111-1111-1111-111111111111','Central Franchise');
INSERT INTO organizations (id,brand_id,name) VALUES ('eac7fee9-07d9-4882-93f5-14f11d3f7b89','11111111-1111-1111-1111-111111111111','West Franchise');
INSERT INTO locations (id,organization_id,name) VALUES ('ea125f67-6b94-4992-8eb9-d832ae026106','955c3c4d-3a03-4d79-9655-3871f5ad999d','East‑NYC');
INSERT INTO locations (id,organization_id,name) VALUES ('3b1ae0b8-1886-476c-9147-18b9d0a4d846','955c3c4d-3a03-4d79-9655-3871f5ad999d','East‑Boston');
INSERT INTO locations (id,organization_id,name) VALUES ('8b91d138-3376-4ee2-b53e-07a73b5f095d','719aeacd-dc94-4476-874b-0d178d8c0c48','Central‑Chicago');
INSERT INTO locations (id,organization_id,name) VALUES ('fb7aa48f-d6c4-44cc-bb68-89529260c886','719aeacd-dc94-4476-874b-0d178d8c0c48','Central‑Dallas');
INSERT INTO locations (id,organization_id,name) VALUES ('afe3bacf-9d0d-4acd-b895-9947f58e23cb','eac7fee9-07d9-4882-93f5-14f11d3f7b89','West‑LA');
INSERT INTO locations (id,organization_id,name) VALUES ('079f2808-5770-44e6-b2d8-ee44bf76e3de','eac7fee9-07d9-4882-93f5-14f11d3f7b89','West‑SF');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('785097c8-2b34-410a-a8ea-bcaf10791c45','6D12E310B371FCB1','Panel-1','ea125f67-6b94-4992-8eb9-d832ae026106');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('5e2e1545-e0d0-42a1-b177-983ebd4dce32','3E1C019A462D5B3C','Panel-2','ea125f67-6b94-4992-8eb9-d832ae026106');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('ef08037f-e02e-424e-b630-7199c4d1b59d','9FD4E31C89A9433A','Panel-1','3b1ae0b8-1886-476c-9147-18b9d0a4d846');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('908cf0e5-b350-493e-866d-4d4652468ada','945923DE69EEC392','Panel-2','3b1ae0b8-1886-476c-9147-18b9d0a4d846');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('26bfa2d8-b041-4775-9d51-0c22476756f5','2B62D6A4301367AD','Panel-1','8b91d138-3376-4ee2-b53e-07a73b5f095d');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('2c77c21c-7deb-4ad5-a7d9-d501623817b2','79EADDE31BF8F3AC','Panel-2','8b91d138-3376-4ee2-b53e-07a73b5f095d');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('459842e9-b637-476f-9214-cae25242e33a','27A41104DFE32507','Panel-1','fb7aa48f-d6c4-44cc-bb68-89529260c886');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('86dfaee4-ef2f-4933-a7ba-943b1251acdd','DD67F2DE418FF162','Panel-2','fb7aa48f-d6c4-44cc-bb68-89529260c886');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('aabe5861-80bf-4244-b217-d2f67ade6682','F04504FF5C35B29D','Panel-1','afe3bacf-9d0d-4acd-b895-9947f58e23cb');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('f5dc198d-25e0-4a02-bb29-06806f2ec0ff','4C1A606F962FD437','Panel-2','afe3bacf-9d0d-4acd-b895-9947f58e23cb');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('bdb8a6e9-045f-43bf-a8e1-cc7b0fde55aa','B89021ABCCC13085','Panel-1','079f2808-5770-44e6-b2d8-ee44bf76e3de');
INSERT INTO electric_sensors (id,duid,name,location_id) VALUES ('1f223a7e-cde6-4bf2-9cdb-281423841e7e','5A09555751350906','Panel-2','079f2808-5770-44e6-b2d8-ee44bf76e3de');
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('785097c8-2b34-410a-a8ea-bcaf10791c45','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('785097c8-2b34-410a-a8ea-bcaf10791c45','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('785097c8-2b34-410a-a8ea-bcaf10791c45','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('5e2e1545-e0d0-42a1-b177-983ebd4dce32','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('5e2e1545-e0d0-42a1-b177-983ebd4dce32','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('5e2e1545-e0d0-42a1-b177-983ebd4dce32','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('ef08037f-e02e-424e-b630-7199c4d1b59d','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('ef08037f-e02e-424e-b630-7199c4d1b59d','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('ef08037f-e02e-424e-b630-7199c4d1b59d','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('908cf0e5-b350-493e-866d-4d4652468ada','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('908cf0e5-b350-493e-866d-4d4652468ada','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('908cf0e5-b350-493e-866d-4d4652468ada','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('26bfa2d8-b041-4775-9d51-0c22476756f5','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('26bfa2d8-b041-4775-9d51-0c22476756f5','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('26bfa2d8-b041-4775-9d51-0c22476756f5','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('2c77c21c-7deb-4ad5-a7d9-d501623817b2','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('2c77c21c-7deb-4ad5-a7d9-d501623817b2','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('2c77c21c-7deb-4ad5-a7d9-d501623817b2','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('459842e9-b637-476f-9214-cae25242e33a','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('459842e9-b637-476f-9214-cae25242e33a','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('459842e9-b637-476f-9214-cae25242e33a','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('86dfaee4-ef2f-4933-a7ba-943b1251acdd','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('86dfaee4-ef2f-4933-a7ba-943b1251acdd','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('86dfaee4-ef2f-4933-a7ba-943b1251acdd','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('aabe5861-80bf-4244-b217-d2f67ade6682','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('aabe5861-80bf-4244-b217-d2f67ade6682','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('aabe5861-80bf-4244-b217-d2f67ade6682','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('f5dc198d-25e0-4a02-bb29-06806f2ec0ff','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('f5dc198d-25e0-4a02-bb29-06806f2ec0ff','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('f5dc198d-25e0-4a02-bb29-06806f2ec0ff','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('bdb8a6e9-045f-43bf-a8e1-cc7b0fde55aa','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('bdb8a6e9-045f-43bf-a8e1-cc7b0fde55aa','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('bdb8a6e9-045f-43bf-a8e1-cc7b0fde55aa','Circuit 3',3);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('1f223a7e-cde6-4bf2-9cdb-281423841e7e','Circuit 1',1);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('1f223a7e-cde6-4bf2-9cdb-281423841e7e','Circuit 2',2);
INSERT INTO circuits (sensor_id,name,circuit_number) VALUES ('1f223a7e-cde6-4bf2-9cdb-281423841e7e','Circuit 3',3);
COMMIT;