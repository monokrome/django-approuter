from django.conf import settings


routes = getattr(settings, 'DATABASE_APP_ROUTES', {})
default_db = getattr(settings, 'DATABASE_NAME', 'default')


class AppRouter(object):
    """ Provides app-specific database routing.

    Uses the 'DATABASE_APP_ROUTERS` setting as a map of app labels to
    the database names where the action should apply.

    """

    def get_database(self, model):
        """ Return the name of the database to be used for the given model. """

        app_label = model._meta.app_label

        if app_label in routes:
            return routes[app_label]

        return default_db

    def db_for_write(self, model, **hints):
        return self.get_database(model)

    def db_for_read(self, model, **hints):
        return self.get_database(model)

    def allow_relation(self, left, right, **hints):
        left_db = self.get_database(left)
        right_db = self.get_database(right)

        return left_db is right_db

    def allow_migrate(self, db, model):
        return True

    def allow_syncdb(self, db, model):
        if model._meta.app_label == 'south':
            return True

        elif db == self.get_database(model):
            return True

        return False