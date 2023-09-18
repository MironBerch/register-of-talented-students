from celery import shared_task


@shared_task
def import_students_celery_task(filepath):
    """Create celery task for import students from excel document."""
    from .input import import_students

    #try:
    import_students(filepath=filepath)
#    except:  # noqa: E722
#        pass
