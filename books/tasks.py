from celery import shared_task

@shared_task
def send_book_notification(book_title):
    print(f"[CELERY] Отправлю уведомление : создана книга '{book_title}'")
    return f"Уведомление о книге '{book_title}' отправлено"

