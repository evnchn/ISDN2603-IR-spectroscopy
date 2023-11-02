import_string = \
'''
import matplotlib.pyplot as plt # matplotlib
import sys
'''

### LINK START! (https://github.com/evnchn/linkstart.py)
for line in import_string.splitlines():
    if "import" in line:
        # print(line) custom behaviour
        try:
            exec(line)
        except:
            if "#" in line:
                package_name = line.split("#")[-1]
            else:
                splits = line.split("import")
                if "from" in line:
                    package_name = splits[0].replace("from","")
                else:
                    package_name = splits[1]
            package_name = package_name.strip()
            print("Installing {}...".format(package_name))    
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            try:
                exec(line)
            except:
                print("Failed to install {}".format(package_name))
### DONE

def read_specimen_data(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.count(",") == 1:
                numbers = line.split(",")
                try:
                    numbers = [float(num) for num in numbers]
                    data.append(numbers)
                except ValueError:
                    pass

    return data

def plot_data(data, title="Specimen.dat"):
    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    ax = plt.gca()
    ax.set_xlim([max(x), min(x)])
    plt.show()

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print(f"Try {sys.argv[0]} [filename]")
    filename = input("Drag>")

result = read_specimen_data(filename)

plot_data(result, filename)