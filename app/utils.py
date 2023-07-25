



def create_data_struct(data_path):
    data = []
    with open(data_path,"+rb") as f:
        [data.append({
            "text": row.split(",")[0],
            "score": row.split(",")[1],
            "suggestion": row.split(",")[2]
        }) for row in f.readlines()]

    return data

def insert_data_mongo(db):
    
    pass

