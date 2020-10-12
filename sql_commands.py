def create_main_table():
    """
    Function create table in DB SQLite3
    :return:
    """
    result = """
    CREATE TABLE IF NOT EXISTS parser_data(
                 ID INTEGER PRIMARY KEY
               , floor_plan TEXT
               , floor INTEGER
               , area REAL
               , status TEXT
               , price INTEGER
               , type TEXT
               , link TEXT
               , terrace REAL
               );
    """
    return result