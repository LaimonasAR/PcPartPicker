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
import logging
import logging.config
from pymongo.errors import OperationFailure

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
logger = logging.getLogger("sLogger")
# logger.debug("This is a debug message")

# logger.warning("Zero was entered instead of X or O")  # example, remmove this


class PcParts:
    def __init__(self, part_type: str, **kwargs):
        self.part_type = part_type
        self.kwargs = kwargs

    def get_all(self):
        results = app.find_part(query={})
        return results

    def get_data(self, **kwargs):
        results = app.find_part(query={"part_type": self.part_type, **kwargs})
        return results

    def add_part(self):
        results = app.create_part({"part_type": self.part_type, **self.kwargs})
        return results

    def update_part(self, **kwargs):
        results = app.update_part(
            query={"part_type": self.part_type, **self.kwargs},
            update={**kwargs},
        )
        return results


class Part(PcParts):
    def __init__(self, part_type: str, **kwargs):
        super().__init__(part_type)
        self.kwargs = kwargs

    def get_all_parts(self):
        results = self.get_all()
        for part in results:
            logger.info("All parts found")
            return f"{part['part_type']} {part}"

    def get_property(self):
        if "property" in self.kwargs:
            results = self.get_data()
            prop = self.kwargs.get("property")
            for part in results:  # bad, fix this shit
                return f"{part['part_type']} {part['name']}, {part[prop]} {prop}"

    def get_all_properties(self):
        results = list(self.get_data())
        result = results[0]
        props = []
        for key, value in result.items():
            if key != "_id":
                props.append(key)
        # print(props)
        logger.info("Part properties found")
        return props

    def update_part(self, **kwargs):
        return super().update_part(**kwargs)

    def get_part(self):
        results = self.get_data(**self.kwargs)
        return results

    def add_part(self):
        return super().add_part()

# class CpuCooler(PcParts):
#     def __init__(self, name, **kwargs):
#         super().__init__(part_type="CPU Cooler")
#         self.name = name

#     def get_all_parts(self):
#         results = self.get_data()
#         for parts in results:
#             print(f"CPU Cooler {parts}")
