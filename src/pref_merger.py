import configparser

def merge(Pref_file,Spec_file):
    cfg_p = configparser.ConfigParser()
    cfg_s = configparser.ConfigParser()
    cfg_p.read(Pref_file)
    cfg_s.read(Spec_file)
    for st in cfg_s.sections():
        if st in cfg_p.sections():
            for key in cfg_s[st]:
                cfg_p[st][key] = cfg_s[st][key]
        else:
            cfg_p[st] = {}
            for key in cfg_s[st]:
                cfg_p[st][key] = cfg_s[st][key]
    
    with open(Pref_file, 'w') as configfile:
        cfg_p.write(configfile)
