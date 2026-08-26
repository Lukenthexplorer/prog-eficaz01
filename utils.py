import sqlite3

class BancoDados:
    def __init__(self):
        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                favorita INTEGER NOT NULL DEFAULT 0
            )
        """)
        conexao.commit()
        conexao.close()

    def add_note(self, title, details):
        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO note (title, content)
            VALUES (?, ?)
        """, (title, details))

        conexao.commit()
        conexao.close()

    def get_notes(self):
        conexao = sqlite3.connect("banco.db")
        conexao.row_factory = sqlite3.Row

        cursor = conexao.cursor()

        cursor.execute("""
            SELECT * FROM note
            ORDER BY favorita DESC, id ASC
        """)

        notas = cursor.fetchall()

        conexao.close()

        return notas

    def get_note(self, id):
        conexao = sqlite3.connect("banco.db")
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT * FROM note WHERE id = ?
        """, (id,))

        nota = cursor.fetchone()
        conexao.close()
        return nota

    def remove_note(self, id):
        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM note
            WHERE id = ?
        """, (id,))

        conexao.commit()
        conexao.close()

    def edit_note(self, id, title, details):
        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE note
            SET title = ?, content = ?
            WHERE id = ?
        """, (title, details, id))

        conexao.commit()
        conexao.close()

    def toggle_favorite(self, id):
        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE note
            SET favorita = CASE WHEN favorita = 1 THEN 0 ELSE 1 END
            WHERE id = ?
        """, (id,))

        conexao.commit()
        conexao.close()