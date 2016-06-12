import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from profile_window import ProfileWindow

if __name__ == "__main__":
    profwin = ProfileWindow()
    Gtk.main()