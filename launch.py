from main import Part
import time


# --------------launch-------------
# cpu_list = Part(part_type="CPU", name="AMD", property="cores")

# print(cpu_list.get_all_parts())
# print(cpu_list.get_property())
# print(cpu_list.get_all_properties())

# moth_list = Part(part_type="Motherboard", name="Quiet", property="price")
# print(moth_list.get_property())
# print(moth_list.get_all_properties())

get_cpu = Part(part_type="CPU", name="Ryzen 5", cores=12)

print(get_cpu.get_part())
time.sleep(1)
# print(get_cpu.update_part(name="Ryzen 5"))
print(get_cpu.update_part(speed=8000))
time.sleep(1)
print(get_cpu.get_part())

new_cpu = Part(
    part_type="CPU", name="Ryzen 100", cores=1200, price=15000, manufacturer="AMD"
)

print(new_cpu.add_part())
time.sleep(1)
print(new_cpu.get_part())
