from db.run_sql import run_sql

from models.museum import Museum
from models.work import Work
import repositories.museum_repository as museum_repository

# Write your functions here
def select_all():
    result = run_sql("SELECT * FROM works")
    works = []
    for row in result:
        title = row['title']
        artist = row['artist']
        year = row['year']
        museum = museum_repository.select(row['museum_id'])
        id = row['id']
        works.append(Work(title, artist, year, museum, id))
    return works

def save(work):
    sql = "INSERT INTO works (title, artist, year, museum_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [work.title, work.artist, work.year, work.museum.id]
    result = run_sql(sql, values)
    work.id = result[0]["id"]

def select(id):
    result = run_sql("SELECT * FROM works WHERE id = (%s)", [id])
    if len(result) > 0:
        result = result[0]
        museum = museum_repository.select(result["museum_id"])
        return Work(result["title"], result["artist"], result["year"], museum, result['id'])
    return None

def update(work):
    sql = "UPDATE works SET (title, artist, year, museum_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [work.title, work.artist, work.year, work.museum.id, work.id]
    run_sql(sql, values)

def delete(id):
    run_sql("DELETE FROM works WHERE id = %s", [id])