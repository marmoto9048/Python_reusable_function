from Read_Save import save
from nlgeval import compute_metrics

metrics_dict = compute_metrics(hypothesis='predict-100.txt',references=['reference.txt'])# #
# input_file_path = "test-100.txt"
print('metrics_dict',metrics_dict)
output_file_path = "results.txt"
save(output_file_path, metrics_dict)










