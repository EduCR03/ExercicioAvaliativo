class AulaDB:
    def create(self, auladb):
        return self.collection.insert_one(auladb).insert_id

    def read(self):
        return self.collection.find()

    def update(self, assunto, professorNome):
        return self.collection.update_one(
            {"nome": assunto},
            {
                "$set": {"assunto": assunto,
                         "professor": professorNome
                         }
            }
        ).modified_count

    def delete(self, assunto):
        return self.db.aula.delete_one({"nome": assunto}).deleted_count
    pass