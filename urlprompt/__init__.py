from django.db.backends.signals import connection_created
def activate_wal(sender, connection, **kwargs):
    """Enable integrity constraint with sqlite."""
    if connection.vendor == 'sqlite':
        cursor = connection.cursor()
        cursor.execute('PRAGMA journal_mode=wal;')

connection_created.connect(activate_wal)
