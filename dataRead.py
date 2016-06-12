# -*- coding: utf-8 -*-
import pickle
import os.path


def read_profile():

    if (os.path.isfile("toolscraft.data")):
        pass
    else:
        write_profile([])

    with open("toolscraft.data", "rb") as data_file:
        mdp = pickle.Unpickler(data_file)
        profiles = mdp.load()
        return profiles
    return False


def write_profile(profile_list):
    with open("toolscraft.data", "wb") as data_file:
        mp = pickle.Pickler(data_file)
        mp.dump(profile_list)