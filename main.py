
import os
import pyinputplus as pyip

def process_file(filename):
    inbred = 0
    total = 0
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            DNA = line.split()
            total += 1
            if DNA[4] != '0' and DNA[5] != '0':
                if DNA[4] == DNA[5]:
                    inbred += 1
    
    if total > 0:
        fraction = (inbred / total) * 100
        rounded = round(fraction, 2)
        print(f"{filename} has {total} markers")
        print(f"{filename.replace('.txt', '')} is {rounded}% inbred\n")

def stretchCalculation(file):
    with open(file, "r") as output:
        inbred = 0
        stretch = 0
        location = ""
        lines = output.readlines()
        for line in lines:
            DNA = line.split()
            if DNA[4] != '0' and DNA[5] != '0':
                if DNA[4] == DNA[5]:
                    inbred += 1
                    if inbred > stretch:
                        stretch = inbred
                        location = DNA[1]
                else:
                    inbred = 0
    print(f"{file}'s longest stretch of inbreeding was {stretch} loci long and ended at {location}\n")

def biggestDawg(txt_files):
    inbred = 0
    large = 0
    bestStretch = 0
    bestName = ""
    for file in txt_files:
        large = 0
        with open (file, "r") as output:
            lines = output.readlines()
            for line in lines:
                DNA = line.split()
                if DNA[4] != 0 and DNA[5] != 0:
                    if DNA[4] == DNA[5]:
                        inbred += 1
                    if DNA[4] != DNA[5]:
                        if inbred >= 250:
                            large += 1
                            if large > bestStretch:
                                bestStretch = large
                                bestName = file
                        inbred = 0

    print(f"{bestName} has the highest quantity of long stretches of inbreeding with {bestStretch} stretches of 250+ inbred loci")

def main():
    txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    
    if not txt_files:
        print("No .txt files found in the current directory.")
        return
        
    print(f"Processing {len(txt_files)} files...\n")
    for file in txt_files:
        process_file(file)
        stretchCalculation(file)

    biggestDawg(txt_files)

    

if __name__ == "__main__":
    main()
