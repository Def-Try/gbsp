import vdf

import pprint

class VMF:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as handle:
            kvalues = vdf.loads(handle.read(),
                                merge_duplicate_keys=False,
                                mapper=vdf.VDFDict)
            self.worlddata = kvalues['world']
            self.entdata = kvalues.get_all_for('entity')
            self.rawdata = kvalues

    # def __vvmf_parse__(self, kvalues: vdf.VDFDict, indent=0):
    #     for k,v in kvalues.items():
    #         print("  "*indent+k, end="")
    #         if isinstance(v, vdf.VDFDict):
    #             print()
    #             self.__vvmf_parse__(v, indent+1)
    #         else:
    #             print(v)
