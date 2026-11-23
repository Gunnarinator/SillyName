def verify_un(db, un):
    return un in db.keys()

def verify_pw(db,un,pw):
    return db[un] == pw