from mysql import connector

db_config = {'user':'root','database':'testdb'}


def insert_persona(nombre,apellido,biografia):
    try:
        conn = connector.connect(**db_config)
        cur = conn.cursor()
        cur.execute("""
        
        INSERT INTO persona (nombre,apellido,biografia)
        VALUES (%s,%s,%s)
        
        """,params=(nombre,apellido,biografia))


    except connector.Error as e:
        raise(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        cur.close()
        conn.close()

def edit_persona(id_persona,nombre,apellido,biografia):
    try:
        conn = connector.connect(**db_config)
        cur = conn.cursor()
        cur.execute("""
        
        UPDATE persona 
        SET nombre=%s,apellido=%s,biografia=%s
        WHERE id=%s
        """,params=(nombre,apellido,biografia,id_persona))


    except connector.Error as e:
        raise(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        cur.close()
        conn.close()

def get_persona_data(id_persona=None):

    try:
        conn = connector.connect(**db_config)
        cur = conn.cursor()

        if id_persona:
            cur.execute(f"""
        SELECT nombre,apellido,biografia
        FROM persona WHERE id={id_persona}
        """)

        else:
            cur.execute("""
        SELECT id,CONCAT(nombre,' ',apellido)
        FROM persona
        """)

        data = cur.fetchall()
        return data
    except connector.Error as e:
        raise(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        cur.close()
        conn.close()

def delete_persona(id_persona):

    try:
        conn = connector.connect(**db_config)
        cur = conn.cursor()

        cur.execute(f"""
        DELETE FROM persona WHERE id = {id_persona}
        """)
    except connector.Error as e:
        raise(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        cur.close()
        conn.close()
