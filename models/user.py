def userEntity(item) -> dict:
    return {
    "id": str(item["_id"]),
    "name": item["name"],
    "email": item["email"],
    "phone": item["phone"],
    "address": item["address"],
    "username": item["username"],
    "password": item["password"],
    "status": item["status"],
    "createdTime": item["createdTime"],
    "createdBy": item["createdBy"],
    "updatedTime": item["updatedTime"],
    "updatedBy": item["updatedBy"]   
    }
    
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]