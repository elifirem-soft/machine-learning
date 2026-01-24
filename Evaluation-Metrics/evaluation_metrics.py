print ("---------- #Example code for calculation quality metrics -------")
print ()
TN = 7 
print(" FN FP TP pre acc rec F1")

for FN in range(0, 7):
    for FP in range(0, FN+1):
        TP = 100- FN- FP- TN
        accuracy = (TP + TN)/(TP + TN + FP + FN)
        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        f1_score = 2 * precision * recall / (precision + recall)

print(f"{FN:9.2f}{FP:9.2f}{TP:9.2f}", end="")
print(f"{precision:9.2f}{accuracy:9.2f}{recall:9.2f}{f1_score:9.2f}")