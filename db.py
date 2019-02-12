#!usr/bin/env python 
from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'app'

TABLES = {}
TABLES['accidentes'] = (
    "CREATE TABLE `accidentes` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50),"
    "  `edad` int(4) ,"
    "  `reportero` enum('accidentado','conocido','desconocido') NOT NULL,"
    "  `latitud` FLOAT NOT NULL,"
    "  `longitud` FLOAT NOT NULL,"
    "  `fecha` DATE NOT NULL,"
    "  `hora` TIME NOT NULL,"
    "  `tipo_accidente` ENUM('bache','frontal','trasero','lateral') NOT NULL,"
    "  `lesion` ENUM('mano','pierna','costilla','pastor') NOT NULL,"
    "  `atencion_conductor` BOOL NOT NULL,"
    "  `atencion_medica` BOOL NOT NULL,"
    "  `reporte_sspc` BOOL NOT NULL,"
    "  `repote_servicios_medicos` BOOL NOT NULL,"
    "  `tiempo_respuesta_sspc` FLOAT,"
    "  `tiempo_respuesta_medica` FLOAT,"
    "  `uso_casco` BOOL NOT NULL,"
    "  `uso_rodilleras` BOOL NOT NULL,"
    "  `uso_coderas` BOOL NOT NULL,"
    "  `uso_luces` BOOL NOT NULL,"
    "  `uso_material_reflejante` BOOL NOT NULL,"
    "  `trayecto_frecuente` BOOL,"
    "  `tipo_trayecto` ENUM('camino a casa','camino a trabajo','paseo'),"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def create_table(connection_config, database=DB_NAME, tables=TABLES):
	cnx = mysql.connector.connect(**connection_config)
	cursor = cnx.cursor()

	try:
	    cursor.execute("USE {}".format(database))
	except mysql.connector.Error as err:
	    print("Database {} does not exists.".format(database))
	    if err.errno == errorcode.ER_BAD_DB_ERROR:
	        create_database(cursor)
	        print("Database {} created successfully.".format(database))
	        cnx.database = database
	    else:
	        print(err)
	        exit(1)

	for table_name in tables:
	    table_description = tables[table_name]
	    try:
	        print("Creating table {}: ".format(table_name), end='')
	        cursor.execute(table_description)
	    except mysql.connector.Error as err:
	        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
	            print("already exists.")
	        else:
	            print(err.msg)
	    else:
	        print("OK")

	cursor.close()
	cnx.close()

def insert_data(table,**kwargs):
	


	print(kwargs['a'])


insert_data('bla', a='sdf', b='sdfsadf', c=2)

if __name__ == '__main__':
	from db_config import db_config
	create_table(db_config)