from db.pool import pool


def fetch_level(level_id):
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT * FROM levels
        WHERE level_id={level_id} 
        """
    )
    [level] = cursor.fetchall()
    connection.close()
    pool.putconn(connection)
    return level
