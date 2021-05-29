from django.urls import path
from .views import *

urlpatterns = [
    path('', onlinewriting, name="onlinewriting"),
    path('post-project', onlinewriting_post_project, name="post_project"),
    path('pending-orders/', onlinewriting_orders_pending, name="pending_orders"),
    path('completed-orders/', onlinewriting_orders_completed, name="completed_orders"),
    path('revisions-orders/', onlinewriting_orders_revisions, name="revision_orders"),
    path('rated-orders/', onlinewriting_orders_rated, name="rated_orders"),
    path('feedback-orders/', onlinewriting_orders_feedback, name="feedback_orders"),

    path('payment-bonuses/', onlinewriting_payments_bonuses, name="payments_bonuses"),
    path('payment-history/', onlinewriting_payments_history, name="payments_history"),
    path('payment-upcoming/', onlinewriting_payments_upcoming, name="payments_upcoming"),
]
