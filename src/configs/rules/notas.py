redrex = {
    "name": "RedRex",
    "table_areas": ['70, 560,498,279'],
    "columns": ['70, 105, 160, 230, 285, 340, 380, 446'],
    "fix": True,
    "small_table_areas": ['381, 275,484,185'],
    "small_columns": ['381, 446'],
    "small_fix": False,
    "small_sanitize": False,
    "header_table_areas": ['290, 613,454,579'],
    "header_columns" : ['290, 360'],
    "header_fix": True,
    "strip_text": './n',
    "flavor": "stream",
    "password": None,
    "pages": "1-end"
}

jornada = {
    "name": "Jornada",
    "table_areas": ['66, 560,498,283'],
    "columns": ['75, 103, 164, 222, 285, 340, 380, 448'],
    "fix": True,
    "small_table_areas": ['100, 275,498,235'],
    "small_columns": ['105, 153, 212, 280'],
    "small_fix": True,
    "small_sanitize": True,
    "header_table_areas": ['290, 613,454,579'],
    "header_columns" : ['290, 360'],
    "header_fix": True,
    "strip_text": './n',
    "flavor": "stream",
    "password": None,
    "pages": "1-end"
}



rules_dict = {
    "jornada": jornada,
    "redrex": redrex,
}
