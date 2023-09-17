from celery import shared_task


@shared_task
def import_students_celery_task(path):
    """Create celery task for import students from excel document."""
    from .input import import_students

    try:
        import_students(path=path)
    except:  # noqa: E722
        pass
