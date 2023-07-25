



def create_data_struct(data_path):
    data = []
    with open(data_path,"+r",encoding="UTF-8") as f:
        [data.append({
            "text": row.split(",")[0],
            "score": row.split(",")[1],
            "suggestion": row.split(",")[2]
        }) for row in f.readlines()]

    return data

def insert_data_mongo(db):
    
    pass


create_data_struct("/home/fama/Desktop/dbtiming/app/data.csv")