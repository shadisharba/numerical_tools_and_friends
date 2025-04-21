import json

thesis = {  "supervisor" : "Shadi Alameddin", \
            "email"      : "alameddin@mib.uni-stuttgart.de", \
            "year"       : 2021, \
            "month"      : 7, \
            "day"        : 15, \
            "bsc"        : True, \
            "msc"        : True, \
            "simtech_pa" : True, \
            "simtech_fm" : True, \
            "commas_sl"  : True, \
            "title"      : "Testing heterogeneous materials with indentation tests", \
            "project"    : [    "DVS - AiF - IGF 21079N - BMWi",
                                "Simtech PN3A-3",
                                "EXC 2075 -- 390740016",
                                "DFG FR2702/8-1 -- 406068690" ],
            "keywords"   : [    "LS-Dyna",
                                "indentation test",
                                "modeling",
                                "python",
                                "thermo-mechanics",
                                "multiscale simulation" ],
            "collaborators": [  "DAE - Felix Fritzen",
                                "BIAS - Anika Langenbeck",
                                "BIAS - Annika Bohlen",
                                "MLZ - Michael Hofmann" ] }

# Note: Tags for thesis compatibility
# bsc         -->  BSc. thesis
# msc         -->  MSc. thesis
# simtech_pa  -->  SimTech Projektarbeit
# simtech_fm  -->  SimTech Forschungsmodul
# commas_sl   -->  COMMAS seminar lecture

s = json.dumps(thesis, indent=4)

print(s)