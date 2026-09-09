# app/ui/__init__.py

from .dashboard import Dashboard
from .timetable_view import TimetableView
from .teacher_view import TeacherView
from .room_view import RoomView
from .search_filter import SearchFilter
from .manual_edit import ManualEdit
from .export import Export
from .ai_assistant import AIAssistant

# Handle potential DOM manipulation issues
# - Ensure elements exist before attempting to remove them
# - Use modern methods like `.remove()` instead of `.removeChild()`
# - Wrap DOM operations in try...catch blocks to handle errors gracefully