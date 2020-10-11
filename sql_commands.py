def create_main_table():
    """
    Function create table in DB SQLite3
    :return:
    """
    result = """
    CREATE TABLE IF NOT EXISTS parser_data(
                 ID INT PRIMARY KEY
               , floor_plan TEXT
               , floor INT
               , area REAL
               , status TEXT
               , price INT
               , type TEXT
               , link TEXT
               , terrace REAL
               );
    """
    return result