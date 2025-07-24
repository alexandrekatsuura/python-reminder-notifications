import pytest
from datetime import datetime, timedelta
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.reminder_service import ReminderService

class TestReminderService:
    """
    Test class for ReminderService functionality.
    """

    def setup_method(self):
        """
        Set up a fresh ReminderService instance for each test.
        """
        self.service = ReminderService()

    def test_add_reminder(self):
        """
        Test adding a reminder to the service.
        """
        reminder_time = datetime.now() + timedelta(hours=1)
        self.service.add_reminder("Test reminder", reminder_time)
        
        reminders = self.service.get_all_reminders()
        assert len(reminders) == 1
        assert reminders[0]['text'] == "Test reminder"
        assert reminders[0]['time'] == reminder_time
        assert reminders[0]['notified'] == False

    def test_get_all_reminders(self):
        """
        Test retrieving all reminders.
        """
        reminder_time1 = datetime.now() + timedelta(hours=1)
        reminder_time2 = datetime.now() + timedelta(hours=2)
        
        self.service.add_reminder("First reminder", reminder_time1)
        self.service.add_reminder("Second reminder", reminder_time2)
        
        reminders = self.service.get_all_reminders()
        assert len(reminders) == 2

    def test_get_pending_reminders(self):
        """
        Test retrieving only pending (not notified) reminders.
        """
        reminder_time = datetime.now() + timedelta(hours=1)
        self.service.add_reminder("Pending reminder", reminder_time)
        
        # Mark one reminder as notified
        self.service.reminders[0]['notified'] = True
        
        pending = self.service.get_pending_reminders()
        assert len(pending) == 0

    def test_remove_reminder(self):
        """
        Test removing a reminder by index.
        """
        reminder_time = datetime.now() + timedelta(hours=1)
        self.service.add_reminder("To be removed", reminder_time)
        
        assert len(self.service.get_all_reminders()) == 1
        
        self.service.remove_reminder(0)
        assert len(self.service.get_all_reminders()) == 0

    def test_remove_reminder_invalid_index(self):
        """
        Test removing a reminder with an invalid index.
        """
        reminder_time = datetime.now() + timedelta(hours=1)
        self.service.add_reminder("Test reminder", reminder_time)
        
        # Try to remove with invalid index
        self.service.remove_reminder(10)
        assert len(self.service.get_all_reminders()) == 1

    def test_clear_all_reminders(self):
        """
        Test clearing all reminders.
        """
        reminder_time1 = datetime.now() + timedelta(hours=1)
        reminder_time2 = datetime.now() + timedelta(hours=2)
        
        self.service.add_reminder("First reminder", reminder_time1)
        self.service.add_reminder("Second reminder", reminder_time2)
        
        assert len(self.service.get_all_reminders()) == 2
        
        self.service.clear_all_reminders()
        assert len(self.service.get_all_reminders()) == 0

    def test_notification_service_start_stop(self):
        """
        Test starting and stopping the notification service.
        """
        assert self.service.running == False
        
        self.service.start_notification_service()
        assert self.service.running == True
        
        self.service.stop_notification_service()
        assert self.service.running == False

