import threading
import time
from datetime import datetime
from plyer import notification

class ReminderService:
    """
    Service class for managing reminders and desktop notifications.
    """

    def __init__(self):
        """
        Initialize the ReminderService with an empty list of reminders.
        """
        self.reminders = []
        self.notification_thread = None
        self.running = False

    def add_reminder(self, text, reminder_time):
        """
        Add a new reminder to the list.

        Args:
            text (str): The reminder text.
            reminder_time (datetime): The time when the reminder should be triggered.
        """
        reminder = {
            'text': text,
            'time': reminder_time,
            'notified': False
        }
        self.reminders.append(reminder)
        
        # Start the notification thread if not already running
        if not self.running:
            self.start_notification_service()

    def get_all_reminders(self):
        """
        Get all reminders.

        Returns:
            list: A list of all reminders.
        """
        return self.reminders

    def get_pending_reminders(self):
        """
        Get all pending (not yet notified) reminders.

        Returns:
            list: A list of pending reminders.
        """
        return [r for r in self.reminders if not r['notified']]

    def start_notification_service(self):
        """
        Start the background thread for checking and sending notifications.
        """
        if not self.running:
            self.running = True
            self.notification_thread = threading.Thread(target=self._check_reminders, daemon=True)
            self.notification_thread.start()

    def stop_notification_service(self):
        """
        Stop the notification service.
        """
        self.running = False

    def _check_reminders(self):
        """
        Background method to continuously check for reminders that need to be triggered.
        """
        while self.running:
            current_time = datetime.now()
            for reminder in self.reminders:
                if not reminder['notified'] and current_time >= reminder['time']:
                    self._send_notification(reminder['text'])
                    reminder['notified'] = True
            time.sleep(30)  # Check every 30 seconds

    def _send_notification(self, message):
        """
        Send a desktop notification.

        Args:
            message (str): The notification message.
        """
        try:
            notification.notify(
                title="Reminder",
                message=message,
                timeout=10
            )
        except Exception as e:
            print(f"Failed to send notification: {e}")

    def remove_reminder(self, index):
        """
        Remove a reminder by index.

        Args:
            index (int): The index of the reminder to remove.
        """
        if 0 <= index < len(self.reminders):
            del self.reminders[index]

    def clear_all_reminders(self):
        """
        Clear all reminders.
        """
        self.reminders.clear()

