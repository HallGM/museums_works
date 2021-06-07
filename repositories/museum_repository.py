from db.run_sql import run_sql

from models.work import Work
from models.museum import Museum

# Write your functions here
def select_all():
    result = run_sql("SELECT * FROM museums")
    museums = [Museum(row["name"], row["address"], row["id"]) for row in result]
    return museums

def save(museum):
    sql = "INSERT INTO museums (name, address) VALUES (%s, %s) RETURNING *"
    result = run_sql(sql, [museum.name, museum.address])
    museum.id = result[0]["id"]

def select(id):
    result = run_sql("SELECT * FROM museums WHERE id = (%s)", [id])
    if len(result) > 0:
        result = result[0]
        return Museum(result["name"], result["address"], result["id"])
    return None

def update(museum):
    sql = "UPDATE museums SET (name, address) = (%s, %s) WHERE id = %s"
    run_sql(sql, [museum.name, museum.address, museum.id])

def delete(id):
    run_sql("DELETE FROM museums WHERE id = %s", [id])
