import json

class Database:

    def add_data(self,name,email,password):

        with open('db.json','r') as rf:
            database = json.load(rf)

        if email in database:
            return 0
        else:
            database[email] = [name,password]
            with open('db.json','w') as wf:
                json.dump(database,wf)
            return 1

    def search(self,email,password):

        with open('db.json','r') as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0


