import pandas
import matplotlib.pyplot as plt
dataset = pandas.read_csv('doggy-boot-harness.csv.1')
del dataset["sex"]
del dataset["age_years"]
data_smaller_paws = dataset[dataset.boot_size < 40].copy()
data_smaller_paws['harness_size_imperial'] = data_smaller_paws.harness_size / 2.54
plt.scatter(data_smaller_paws["harness_size_imperial"], data_smaller_paws["boot_size"])
plt.xlabel("harness_size_imperial")
plt.ylabel("boot_size")
plt.title("Boot_harness_size_imperial")
plt.savefig("boot.png")

