import datetime

import mariadb

class Database:
    def __init__(self):
        self.connection = mariadb.connect(
            user=database_ids.user,
            password=database_ids.password,
            host=database_ids.host,
            port=database_ids.port,
            database=database_ids.database
        )
        self.cursor = self.connection.cursor()

    def find_token(self, token: str):
        query = "SELECT id_joueur, token, time FROM tokens WHERE token = ?"
        self.cursor.execute(query, (token,))
        result = self.cursor.fetchone()
        current_timestamp = datetime.datetime.now().timestamp()
        if result:
            if current_timestamp - result[2] < 20:
                return True, result[0]
            else:
                query = "DELETE FROM tokens WHERE token = ?"
                self.cursor.execute(query, (token,))
        return False, None
    
    def updateArmy(self, idpartie, coord, nb_troupe):  # Met à jour le nombre de troupe sur une case
        idcase = getCase(idpartie, coord)[2]
        query = "UPDATE etat_partie SET nb_pions VALUES ? WHERE id_partie = ? AND id_case = ? ;"
        self.cursor.execute(query, (nb_troupe, idpartie, idcase))

     def recupere_bdd(self,table,nom_champ,D):  # renvoie les valeurs sous forme de tuple de la bdd en fonction de la table et nom de champ en paramètre
        if D != dict():
            for nb_element in range
            query = "SELECT ? FROM ? WHERE ? = ?;"
            self.cursor.execute(query,(nom_champ,table,where_champ,where_condition))
            valeur = self.cursor.fetchall()
            return valeur
        else:
            query = "SELECT ? FROM ? ;"
            self.cursor.execute(query(nom_champ,table))
            valeur = self.cursor.fetchall()
            return valeur
            
    def enregistrer_bdd(self, D):  # d => dict, faudra ptet modifier après, y'a ptet des erreurs dans la récupération des données
        for table in D:
            self.cursor.execute("SELECT id FROM ? ;", (table,))
            nb_ids = list(self.cursor)
            self.connection.commit()

            while len(nb_ids[0]) < len(table['id']):

                self.cursor.execute("INSERT INTO ? ? VALUES ? ;", (table, table.keys(), (table[column][len(nb_ids[0])] for column in table),))
                self.connection.commit()


                self.cursor.execute("SELECT id FROM ? ;", (table,))
                nb_ids = list(self.cursor)
                self.connection.commit()

            for column in table:
                for id_entry in range(0, len(column.values())):

                    self.cursor.execute("UPDATE ? SET ? = ? WHERE id = ?;", (table, column, column[id_entry]), id_entry, )
                    self.connection.commit()
    
    def updateProperty(self, idpartie, idcase, id_new_owner):  # Lorsqu'un joueur prend un pays
        query = "UPDATE id_joueur FROM etat_partie VALUES ? WHERE id_case = ? AND id_partie = ?;"
        self.cursor.execute(query, (id_new_owner, idcase, idpartie))
        
