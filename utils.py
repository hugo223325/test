




# PLC update settings 
PLC_PERIOD_SEC = 0.4    
PLC_PERIOD_HOURS = PLC_PERIOD_SEC / 3600.0
PLC_SAMPLES = 205000 # ~ 24 hours run time



# Topology
IP = {
    'plc1': '192.168.1.10',
    'plc2': '192.168.1.20',
    'plc3': '192.168.1.30',
    'plc4': '192.168.1.40',
    'plc5': '192.168.1.50',
    'scada': '192.168.1.60',
    'attacker': '192.168.1.77',
}
ADDRESS = {
    'plc1': '192.168.1.10:44818',
    'plc2': '192.168.1.20:44818',
    'plc3': '192.168.1.30:44818',
    'plc4': '192.168.1.40:44818',
    'plc5': '192.168.1.50:44818',
    'scada': '192.168.1.60:44818',
    'attacker': '192.168.1.77:44818',
}

NETMASK = '/24'

MAC = {
    'plc1': '00:1D:9C:C7:B0:70',
    'plc2': '00:1D:9C:C8:BC:46',
    'plc3': '00:1D:9C:C8:BD:F2',
    'plc4': '00:1D:9C:C7:FA:2C',
    'plc5': '00:1D:9C:C8:BC:2F',
    'scada': '00:1D:9C:C7:FA:2D',
    'attacker': 'AA:AA:AA:AA:AA:AA',
}






# Others
PLC1_DATA = {
    'TODO': 'TODO',
}
PLC2_DATA = {
    'TODO': 'TODO',
}
PLC3_DATA = {
    'TODO': 'TODO',
}



# PLC utils 
PLC1_ADDR = IP['plc1']
PLC1_TAGS = (
    ('T101', 1, 'REAL'),
    ('H101', 1, 'REAL'),
)
PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 0,
    'server': PLC1_SERVER
}


PLC2_ADDR = IP['plc2']
PLC2_TAGS = (
    ('T201', 2, 'REAL'),
    ('H201', 2, 'REAL'),
    ('F201', 2, 'REAL')
)
PLC2_SERVER = {
    'address': PLC2_ADDR,
    'tags': PLC2_TAGS
}
PLC2_PROTOCOL = {
    'name': 'enip',
    'mode': 0,
    'server': PLC2_SERVER
}


PLC3_ADDR = IP['plc3']
PLC3_TAGS = (
    ('P301', 3, 'REAL'),
)
PLC3_SERVER = {
    'address': PLC3_ADDR,
    'tags': PLC3_TAGS
}
PLC3_PROTOCOL = {
    'name': 'enip',
    'mode': 0,
    'server': PLC3_SERVER
}






# Params for create and initiate sqlite
PATH = 'test_db.sqlite'
NAME = "test_db"
STATE = {
    'name': NAME,
    'path': PATH
}


SCHEMA = """
CREATE TABLE test_db (
    name              TEXT NOT NULL,
    pid               INTEGER NOT NULL,
    value             TEXT,
    PRIMARY KEY (name, pid)
);
"""

SCHEMA_INIT = """
    INSERT INTO test_db VALUES ('T101',   1, '30.0');
    INSERT INTO test_db VALUES ('H101',   1, '22.0');
    
    INSERT INTO test_db VALUES ('T201',   2, '20.0');
    INSERT INTO test_db VALUES ('H201',   2, '15.0');
    INSERT INTO test_db VALUES ('F201',   2, '20.0');

    INSERT INTO test_db VALUES ('P301',   3, '1.00');
"""