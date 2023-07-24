"""Phase 1: Create a class that would represent pc parts. 
It should contain basic methods to retreive items name, price, colour (if applicable).
PC part list can be found here: https://pcpartpicker.com/list/
The every separate part should have at least 3-4 methods to gather this part specific data (example: CPU - brand , speed, power usuage etc.)
At this stage, dictionary data structures can work as Database. 
OOP abstraction, inheritance and encapsulation must be presented in a code base. 
Unit tests must be written for the methods."""
"what is cli_utilities? get_correct_pipeline"

"""Phase 2: 
Add logging to all necessary functionality to see the data flow (with logger config.).
Add exception handling , describe your own exceptions if necessary. 
Create functions that would update current datasets (database). 
Add functions that would parse durrent datasets(database) by specific parameters (CPU name = 'AMD') 
Use  List, Dict comprehentions to get parsed data."""

import app
from typing import List, Dict, Any


class PcParts:
    def __init__(self, part_type: str, **kwargs):
        self.part_type = part_type
        self.kwargs = kwargs

    def get_all(self):
        results = app.find_part(query={})
        return results

    def get_data(self):
        results = app.find_part(query={"part_type": self.part_type})
        return results

    def add_part(self):
        results = app.create_part({"part_type": self.part_type, **self.kwargs})
        return results


class Part(PcParts):
    def __init__(self, part_type: str, **kwargs):
        super().__init__(part_type)
        self.kwargs = kwargs

    def get_all_parts(self):
        results = self.get_all()
        for part in results:
            return f"{part['part_type']} {part}"

    def get_property(self):
        if "property" in self.kwargs:
            results = self.get_data()
            prop = self.kwargs.get("property")
            for part in results:
                return f"{part['part_type']} {part['name']}, {part[prop]} {prop}"

    def get_all_properties(self):
        results = list(self.get_data())
        result = results[0]
        props = []
        for key, value in result.items():
            if key != "_id":
                props.append(key)
        # print(props)
        return props


# class CpuCooler(PcParts):
#     def __init__(self, name, **kwargs):
#         super().__init__(part_type="CPU Cooler")
#         self.name = name

#     def get_all_parts(self):
#         results = self.get_data()
#         for parts in results:
#             print(f"CPU Cooler {parts}")


# --------------launch-------------
cpu_list = Part(part_type="CPU", name="AMD", property="cores")

cpu_list.get_all_parts()
cpu_list.get_property()
cpu_list.get_all_properties()

moth_list = Part(part_type="Motherboard", name="Quiet", property="price")
moth_list.get_property()
moth_list.get_all_properties()
