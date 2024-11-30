import subprocess
import pandas
import joblib
#url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py"
#subprocess.run(["wget", url])
#url2 = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv"
#subprocess.run(["wget",url2])
def install_package(package_name):
        try:
                subprocess.run(["pip", "install", package_name], check=True)
                print(f"Package '{package_name}' installed successfully.")
        except subprocess.CalledProcessError:
                print(f"Failed to install package '{package_name}'.")
install_package("statsmodels")
import statsmodels.formula.api as smf
data = pandas.read_csv('doggy-boot-harness.csv.1')
print(data.head())
model = smf.ols(formula = "boot_size ~ harness_size",data = data).fit()
print("Model trained!")
joblib.dump(model, './avalanche_dog_boot_model.pkl')
def load_model_and_predict(harness_size) : 
	model_loaded = joblib.load('./avalanche_dog_boot_model.pkl')
	print("We have loaded a model with the following parameters")
	print(model_loaded.params)
	inputs = {"harness_size" : [harness_size]}
	predicted_boot_size = model_loaded.predict(inputs)[0]
	return predicted_boot_size
harness_size = float(input("Enter the harness size : "))
predicted_boot_size = load_model_and_predict(harness_size)
print("The predicted boot size is : ",predicted_boot_size)



