# -*- coding: utf-8 -*-
import gi
import dataRead
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#  from dataRead import read_profile

versions = ["1.7.10", "1.8", "1.8.1", "1.9", "1.9.4"]

# ["Name of profile", "version"],
profile_list_l = dataRead.read_profile()
profile_list_gui = Gtk.ComboBoxText()


class ProfileWindow(Gtk.Window):

    def __init__(self):
        window = Gtk.Window()
        window.set_title("ToolsCraft - Profile")
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect("delete-event", Gtk.main_quit)

        #Boxs

        main_box = Gtk.Box()
        main_box.set_spacing(2)
        main_box.set_orientation(Gtk.Orientation.HORIZONTAL)
        window.add(main_box)

        lbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        lbox.set_spacing(5)
        main_box.add(lbox)

        rbox = Gtk.Box()
        rbox.set_spacing(15)
        rbox.set_orientation(Gtk.Orientation.VERTICAL)
        main_box.add(rbox)

        #Items

        profile_label = Gtk.Label("Choose a profile :")
        lbox.add(profile_label)

        for profile in profile_list_l:
            profile_list_gui.append_text(profile[0])

        profile_list_gui.set_entry_text_column(0)
        lbox.add(profile_list_gui)

        open_profile = Gtk.Button("Choose this profile")
        open_profile.connect_after("clicked", self.on_open_clicked)
        lbox.add(open_profile)

        create = Gtk.Button("Create a new profile")
        create.connect_after("clicked", self.create_new_profile)
        lbox.add(create)

        delete = Gtk.Button("Delete this profile")
        delete.connect_after("clicked", self.delete_profile)
        lbox.add(delete)

        window.show_all()

    def on_open_clicked(self, button):
        # To implement ! (Open the mod window !)
        pass

    def create_new_profile(self, button):
        CreationWindow()
        Gtk.main()
        Gtk.main_quit()

    def delete_profile(self, button):
        # To implement ! (Open the mod window !)
        pass


class CreationWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Create a new profile - ToolsCraft")
        self.connect("delete-event", Gtk.main_quit)
        box = Gtk.Box(spacing=5, orientation=Gtk.Orientation.HORIZONTAL)
        self.add(box)

        lb = Gtk.Label("Choose options for your new profile :")
        box.add(lb)

        self.name = Gtk.Entry()
        box.add(self.name)

        self.versions_list = Gtk.ComboBoxText()
        for version in versions:
            self.versions_list.append_text(version)
        box.add(self.versions_list)

        create = Gtk.Button("Create this profile !")
        create.connect_after("clicked", self.add_profile)
        cancel = Gtk.Button("Cancel  !")
        cancel.connect_after("clicked", self.cancel)

        box.add(create)
        box.add(cancel)

        self.show_all()

    def add_profile(self, button):
        print("salut")
        for profile in profile_list_l:
            if(self.name.get_text() in profile):
                print("DONT ADD")
                Gtk.main_quit()
                quit()
        print("Adding")
        profile_list_l.append([self.name.get_text(),
        self.versions_list.get_active_text()])

        count = 0
        for profile in profile_list_l:
            profile_list_gui.remove(count)
            count += 1

        for profile in profile_list_l:
            profile_list_gui.append_text(profile[0])
        dataRead.write_profile(profile_list_l)

    def cancel(self, button):
        ProfileWindow()
        Gtk.main()
        Gtk.main_quit()