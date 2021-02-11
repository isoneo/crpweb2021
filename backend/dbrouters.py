from django.conf import settings


class DBRouter(object):
    def db_for_read(self, model, **hints):
        return getattr(model, "_DATABASE", "default")

    def db_for_write(self, model, **hints):
        return getattr(model, "_DATABASE", "default")

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the master/slave pool.
        """
        db_list = ('default')
        return obj1._state.db in db_list and obj2._state.db in db_list

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'core':
            if model_name in ['Ihs_well','Capex_by_well']:
                return False
            elif model_name in ['Cme_settlement_prices']:
                return False
            elif model_name[:3] == 'Ssi':
                return False
        return True